from sqlobject import *
from DAO.Connection import base_conn
from Classes import Channel


class ChannelTable(SQLObject):
    _connection = base_conn.get_connection()
    _connection.debug = True
    channelId = StringCol(length=40, notNone=True)
    title = StringCol(notNone=True)
    description = StringCol(notNone=False)
    publishedAt = DateTimeCol(notNone=False)
    viewCount = IntCol(notNone=False)
    subscriberCount = IntCol(notNone=False)
    videoCount = IntCol(notNone=False)
    timeIn = TimestampCol()


class ChannelDAO:
    @staticmethod
    def add_channel(*args):
        if len(args) == 1:
            if isinstance(args[0], Channel):
                return ChannelDAO.__add_channel_o(channel_object=args[0])
            else:
                print('Error：传入对象类型错误 应为Channel 传入' + type(args[0]))
                return -1
        elif len(args) == 7:
            return ChannelDAO.__add_channel_p(channel_id=args[0], title=args[1], description=args[2],
                                              published_at=args[3],
                                              view_count=args[4], subscriber_count=args[5], video_count=args[6])
        else:
            print('Error：参数不全时请使用传入实例对象的方式进行调用')
            return -1

    @staticmethod
    def __add_channel_o(channel_object):
        return ChannelTable(channelId=Channel.get_channel_id(channel_object),
                            title=Channel.get_title(channel_object),
                            description=Channel.get_description(channel_object),
                            publishedAt=Channel.get_published_at(channel_object),
                            viewCount=Channel.get_view_count(channel_object),
                            subscriberCount=Channel.get_subscriber_count(channel_object),
                            videoCount=Channel.get_video_count(channel_object)).id

    @staticmethod
    def __add_channel_p(channel_id, title, description, published_at, view_count, subscriber_count, video_count):
        return ChannelTable(channelId=channel_id, title=title, description=description, publishedAt=published_at,
                            viewCount=view_count, subscriberCount=subscriber_count, videoCount=video_count).id

    @staticmethod
    def delete_channel(rid):
        var = ChannelTable.get(rid)
        ChannelTable.delete(rid)
        return var

    @staticmethod
    def get_record(channel_id):
        record_list = list(ChannelTable.select(ChannelTable.q.channelId == channel_id))
        object_list = []
        for r in record_list:
            temp = Channel(r.channelId, r.title, r.description, r.publishedAt,
                           r.viewCount, r.subscriberCount, r.videoCount, r.timeIn)
            object_list.append(temp)
        return object_list

    @staticmethod
    def get_channel_list():
        channel_list = list(ChannelTable.select(distinct=True))
        dictionary = {}
        for c in channel_list:
            dictionary[c.channelId] = c.title
        return dictionary
