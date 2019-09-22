# WEB服务器与Tornado

# 1.http服务器的真相

HTTP 协议是建立在 TCP 协议之上的短连接协议。

它利用了 TCP 协议的可靠性，用来传输超文本 (HTML)，通信一次连接一次，通信完成后 TCP 连接关闭。

所以如果想创建一个 HTTP Server 需要通过 Socket 搭建一个 服务端程序。

## 1.1简单的HTTP server

```
import socket

ADDR = ('0.0.0.0', 80)

RESPONSE = b'''
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1 style="text-align: center;">Hello World</h1>
    </body>
</html>
'''

listen_socket = socket.socket()  # 建立 SOCK 连接
listen_socket.bind(ADDR)         # 绑定 IP:端口
listen_socket.listen(100)        # 开始监听

print('Server is running: %s:%s ...' % ADDR)

while True:
    client_socket, client_address = listen_socket.accept()  # 接受客户端的连接
    print('client request from %s:%s' % client_address)
    request = client_socket.recv(1024)  # 接收客户端数据

    http_response = RESPONSE

    client_socket.sendall(http_response)
    client_socket.close()
```

# 2.web框架

随着技术的发展，我们每天的要处理的信息量都在爆炸新的增加。传统的静态页面技术早已跟不上时代需求，因而催生了动态页面技术。

所谓动态页面，即所有的页面用程序来生成，以细节实现上的不同，又可分为“前端动态页面”和“后端动态页面”。

我们在 Web 前端阶段所学 Ajax、VUE 等技术，就是前端动态页面。而今后我们所学的主要是后端动态页面技术，甚至是两者结合使用。

![server](./img/WebServer.png)



## 2.1常见框架

| Web Framework | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| **Django**    | 全能型框架, 大而全, 插件丰富, 文档丰富, 社区活跃, 适合快速开发, 内部耦合比较紧 |
| **Flask**     | 微型框架, 适合新手学习, 极其灵活, 便于二次开发和扩展, 生态环境好, 插件丰富 |
| **Tornado**   | 异步处理, 事件驱动 (epoll), 性能优异                         |
| Bottle        | 单文件框架, 结构紧凑，适合初学者阅读源码，了解 Web 原理      |
| web.py        | 代码优美, 适合学习源码                                       |
| Falcon        | 性能优异适合写 API 接口                                      |
| Quixote       | 一个爷爷级别的框架，著名的豆瓣网用的便是这个                 |
| Sanic         | 后起之秀，性能秒杀以上所有前辈，但没有前辈们稳定。           |



# 3.tornado入门

Tornado 最大的特点就是他实现了一个 “异步非阻塞” 的 HTTP Server，性能非常优异。

## 3.1安装

```
pip install tornado
```

```
代码：
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

## 3.2启动参数

```
from tornado.options import parse_command_line, define, options

define("host", default='0.0.0.0', help="主机地址", type=str)
define("port", default=8888, help="主机端口", type=int)

parse_command_line()
print('你传入的 host: %s' % options.host)
print('你传入的 port: %s' % options.port)
```

## 3.3路由处理

```
import tornado.ioloop
from tornado.web import RequestHandler, Application

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("欢迎进入主页")

class BookHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("你想看的书应有尽有")

app = Application([
    ('/', HomeHandler),
    ('/book/', BookHandler),
])

app.listen(8000)
tornado.ioloop.IOLoop.current().start()
```

## 3.4处理GET和POST请求

```
class StoryHandler(tornado.web.RequestHandler):
    stories = {1: '小红帽', 2: '皮诺曹', 3: '阿拉丁神灯'}

    def get(self):
        story_id = self.get_argument('story_id')
        story = self.stories[story_id]
        self.write("你想看 %s 的故事" % story)

    def post(self):
        pass
```

### Http的请求方法

| Method  | Description                                                  |
| ------- | ------------------------------------------------------------ |
| POST    | 向指定资源提交数据进行处理请求, 数据被包含在请求体中。       |
| GET     | 请求指定的页面信息，并返回实体主体。                         |
| PUT     | 从客户端向服务器传送的数据取代指定的文档的内容。             |
| DELETE  | 请求服务器删除指定的页面。                                   |
| HEAD    | 类似于 GET 请求，只不过返回的响应中没有具体的内容，用于获取报头 |
| PATCH   | 是对 PUT 方法的补充，用来对已知资源进行局部更新 。           |
| OPTIONS | 列举服务器支持的请求方法                                     |





# 数据库sqlalchemy与模板

# 1.ORM对象关系映射

![](./img/orm.png)

ORM 全称是：Object Relational Mapping (对象关系映射)。其主要作用是在编程中把面向对象的概念跟数据库中表的概念对应起来。

举例来说就是，我定义一个类，那就对应着一张表，这个类的实例，就对应着表中的一条记录。

面向对象编程把所有实体看成对象（object），关系型数据库则是采用实体之间的关系（relation）连接数据。
很早就有人提出，关系也可以用对象表达，这样的话，就能使用面向对象编程，来操作关系型数据库。

ORM 的优点：

- 数据模型都在一个地方定义，更容易更新和维护，也利于重用代码。
- ORM 有现成的工具，很多功能都可以自动完成，比如数据预处理、事务等等。
- 它迫使你使用 MVC 架构，ORM 就是天然的 Model，最终使代码更清晰。
- 基于 ORM 的业务代码比较简单，代码量少，语义性好，容易理解。
- 你不必编写性能不佳的 SQL。

Python下常用的 ORM 有: Django-ORM、SQLAlchemy、Peewee 等

### 1.1 sqlalchemy示例

```
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base

# 建立连接与数据库的连接
engine = create_engine('mysql+pymysql://seamile:54188@localhost:3306/sh1905')
Base = declarative_base(bind=engine)  # 创建模型的基础类
Session = sessionmaker(bind=engine)


class User(Base):
    '''User 模型'''
    __tablename__ = 'user'  # 该模型对应的表名

    id = Column(Integer, primary_key=True)  # 定义 id 字段
    name = Column(String(20), unique=True)  # 定义姓名字段
    birthday = Column(Date)                 # 定义生日字段
    money = Column(Float, default=0.0)      # 定义金钱字段


Base.metadata.create_all(checkfirst=True)  # 创建表

session = Session()
# 定义一些对象
bob = User(name='bob', birthday=datetime.date(1990, 3, 21), money=234)
tom = User(name='tom', birthday=datetime.date(1995, 9, 12))
lucy = User(name='lucy', birthday=datetime.date(1998, 5, 14), money=300)
jam = User(name='jam', birthday=datetime.date(1994, 3, 9), money=58)
alex = User(name='alex', birthday=datetime.date(1992, 3, 17), money=99)
eva = User(name='eva', birthday=datetime.date(1987, 7, 28), money=175)
rob = User(name='rob', birthday=datetime.date(1974, 2, 5), money=274)
ella = User(name='ella', birthday=datetime.date(1999, 5, 26), money=394)

# 增加数据
session.add_all([bob, tom, lucy, jam])  # 在 Session 中记录操作
session.commit()                        # 提交到数据库中执行

# 删除数据
session.delete(jam)  # 记录删除操作
session.commit()     # 提交到数据库中执行

# 修改数据
tom.money = 270   # 修改数据
session.commit()  # 提交到数据库中执行

# 查询数据
u_query = session.query(User)  # 先定义表的查询对象

# 直接获取主键(ID)为 5 的数据
user = u_query.get(5)
print(user.id, user.name)

# 使用 filter_by 按条件查询
user = u_query.filter_by(id=7).one()
print(user.id, user.name, user.birthday)

# 使用 filter 进行范围查询，并对结果进行排序
users = u_query.filter(User.id>2).order_by('birthday')
for u in users:
    print(u.name, u.birthday, u.money)

# 根据查询结果进行更新
users = u_query.filter(User.id>2)
users.update({'money': User.money - 1}, synchronize_session=False)
sessiom.commit()

# 按数量取出数据: limit / offset
users = u_query.limit(3).offset(4)
for u in users:
    print(u.id, u.name)

# 计数
num = u_query.filter(User.money>200).count()
print(num)

# 检查是否存在
exists = q.filter_by(name='Seamile').exists()
result = session.query(exists).scalar()
print(result)
```

# 2 tornado模板系统

模板系统是为了更快速、更方便的生产大量的页面而设计的一套程序。

借助模板系统，我们可以先写好页面大概的样子，然后预留好数据的位置，再然后将我们需要的数据，按照既定规则拼到模板中的指定位置，然后渲染出完整页面。

现代的模板系统已经相当成熟，甚至可以通过 `if...else`、`for` 等语句在模板中写出简单的逻辑控制。

## 2.1 模板与静态文件的路径配置

定义 app 时，在 Application 中定义, 可以是想对路径, 也可以是绝对路径

```
app = Application(
    template_path = 'templates',  # 模版路径
    static_path = 'statics'       # 静态文件路径
)
```

## 2.2 模板的变量

在模板中，变量和表达式使用 `{{ ... }}` 包围，可以写入任何的 Python 表达式或者变量

```
<!DOCTYPE html>
<html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <title>Templates</title>
    </head>

    <body>
        <div>你好 {{ name }}，欢迎回来！</div>
        <div>猜一猜，3 x 2 等于几？</div>
        <div>我就不告诉你等于 {{ 3 * 2 }}</div>
    </body>
</html>
```

## 2.3 从python中传递过参数

```
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = 'Tom'
        say = "Hello, world"
        self.render('index.html', name=name, say=say)
```

## 2.4 模板中的if...else

模板中的控制语句使用 `{% ... %}` 包围，如下所示

```
<p>
    根据您的条件我们进行了筛选
    {% if 条件 %}
        <div>第 1 条数据</div>
        <div>第 2 条数据</div>
        <div>。。。</div>
    {% else %}
        <div>抱歉我们没有找到合适的内容</div>
    {% end %}
</p>
```

## 2.5 模板中的for循环

python程序中

```
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        students = ["Lucy", "Tom", "Bob"]
        self.render("student.html", students=students)
```

页面中

```
<html>
  <head>
    <title>学生信息</title>
  </head>
  <body>
    <ul>
      {% for student in students %}
          <li>{{ student.name }}</li>
      {% end %}
    </ul>
  </body>
</html>
```

## 2.6 静态文件

```
├── main.py
├── statics
│   └── img
│       └── coder.jpg
└── templates
    └── index.html
```

在模板中使用静态文件时，静态文件的路径这样写:

```
<img class="avatar" src="/static/img/coder.jpg" />
```

## 2.7 模板继承

网站中，大多数页面都是同样的结构和风格，我们没有必要在所有页面中把相同的样式重复的写很多遍。

Tornado 为我们提供了模板的继承机制，只需要写好父模板，然后让其他模板继承一下即可

父模板文件名经常定义为 "base.html"

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %} 通用标题 {% end %}</title>
</head>
<body>
    {% block body %}{% end %}
</body>
</html>
```

子代码

```
{% extends "base.html" %}

{% block title %} 子页面的标题 {% end %}

{% block body %}
<div>
    子页面里的内容
    Bala Bala
</div>
{% end %}
```

