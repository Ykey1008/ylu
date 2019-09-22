import logging
import uuid
import datetime
from base64 import urlsafe_b64encode as b64encode
from base64 import urlsafe_b64decode as b64decode

import tornado.escape
import tornado.websocket

from logics import MsgHistory


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html", notice=False)

    def post(self):
        username = self.get_argument('username').strip()
        if not username:
            # 如果未传 username，还会到原来的页面，并给用户提示
            self.render("home.html", notice=True)

        # 将用户名进行 base64 编码，并存储在 cookie 中
        b64_username = b64encode(username.encode('utf8'))
        self.set_cookie('username', b64_username)

        self.render(
            "chat.html",
            messages=ChatSocketHandler.history.all(),
            clients=ChatSocketHandler.members,
            username=username
        )


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    members = set()         # 所有成员的连接池
    history = MsgHistory()  # 历史消息对象
    client_id = 0           # 客户端计数器

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self):
        '''与客户端连接时进行的处理'''
        # 设置客户端 ID
        ChatSocketHandler.client_id += 1
        self.client_id = ChatSocketHandler.client_id

        # 从 Cookie 中取出用户名
        b64_name = self.get_cookie('username')
        if not b64_name:
            # 如果用户没有 cookie 给他一个默认名称
            self.username = "游客%d" % self.client_id
        else:
            # 将 cookie 中的 base64 编码的姓名进行解码，然后赋值
            self.username = b64decode(b64_name).decode('utf8')

        # 将用户连接添加到连接池
        ChatSocketHandler.members.add(self)

        # 定义登陆消息，并向其他用户进行广播
        message = {
            "id": str(uuid.uuid4()),
            "type": "online",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        ChatSocketHandler.broadcast(message)

    def on_close(self):
        '''断开连接时的处理'''
        # 首先从连接池中删除自身对象
        ChatSocketHandler.members.remove(self)

        # 向所有用户广播离开的消息
        message = {
            "id": str(uuid.uuid4()),
            "type": "offline",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        ChatSocketHandler.broadcast(message)

    @classmethod
    def broadcast(cls, message):
        logging.info("sending message to %d members", len(cls.members))
        for member in cls.members:
            try:
                member.write_message(message)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        '''发送消息'''
        logging.info("got message %r", message)

        parsed = tornado.escape.json_decode(message)  # 将客户端传来的消息进行 json 解码

        # 组装消息结构
        self.username = parsed["username"]
        message = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
            "type": "message",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        message["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=message)
        )

        ChatSocketHandler.history.add(message)
        ChatSocketHandler.broadcast(message)
