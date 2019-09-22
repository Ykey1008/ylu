import json

from redis import Redis

rds = Redis()


class MsgHistory:
    key = 'chat_history'
    size = 100

    @classmethod
    def add(cls, msg):
        '''记录一条历史消息'''
        json_msg = json.dumps(msg)         # 将消息转化成 json 字符串
        rds.rpush(cls.key, json_msg)       # 将消息推入 Redis 的 List 中
        rds.ltrim(cls.key, -cls.size, -1)  # 将多余的消息截掉

    @classmethod
    def all(cls):
        '''取出所有的历史消息'''
        all_msg = []
        for json_msg in rds.lrange(cls.key, -cls.size, -1):
            msg = json.loads(json_msg)
            all_msg.append(msg)
        return all_msg
