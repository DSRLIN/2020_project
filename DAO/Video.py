from sqlobject import *
from DAO.Connection import base_conn
from Classes import Video


class VideoTable(SQLObject):
    _connection = base_conn.get_connection()
    _connection.debug = True
    videoId = StringCol(length=40, notNone=True)
    channelId = StringCol(length=40, notNone=True)
    title = StringCol(notNone=True)
    description = StringCol(notNone=False)
    publishedAt = DateTimeCol(notNone=False)
    viewCount = IntCol(notNone=False)
    likeCount = IntCol(notNone=False)
    dislikeCount = IntCol(notNone=False)
    commentCount = IntCol(notNone=False)
    timeIn = TimestampCol()


class VideoDAO:
    @staticmethod
    def add_video(*args):
        if len(args) == 1:
            if isinstance(args[0], Video):
                return VideoDAO.__add_video_o(video_object=args[0])
            else:
                print('Error：传入对象类型错误 应为Video 传入' + type(args[0]))
                return -1
        elif len(args) == 9:
            return VideoDAO.__add_video_p(video_id=args[0], channel_id=args[1],
                                          title=args[2], description=args[3], published_at=args[4],
                                          view_count=args[5], like_count=args[6],
                                          dislike_count=args[7], comment_count=args[8])
        else:
            print('Error：参数不全时请使用传入实例对象的方式进行调用')
            return -1

    @staticmethod
    def __add_video_o(video_object):
        return VideoTable(videoId=Video.get_video_id(video_object),
                          channelId=Video.get_channel_id(video_object),
                          title=Video.get_title(video_object),
                          description=Video.get_description(video_object),
                          publishedAt=Video.get_published_at(video_object),
                          viewCount=Video.get_view_count(video_object),
                          likeCount=Video.get_like_count(video_object),
                          dislikeCount=Video.get_dislike_count(video_object),
                          commentCount=Video.get_comment_count(video_object)).id

    @staticmethod
    def __add_video_p(video_id, channel_id, title, description, published_at, view_count, like_count, dislike_count,
                      comment_count):
        return VideoTable(videoId=video_id, channelId=channel_id,
                          title=title, description=description, publishedAt=published_at,
                          viewCount=view_count, likeCount=like_count, dislikeCount=dislike_count,
                          commentCount=comment_count).id

    @staticmethod
    def delete_video(rid):
        var = VideoTable.get(rid)
        VideoTable.delete(rid)
        return var

    @staticmethod
    def get_record(video_id):
        record_list = list(VideoTable.select(VideoTable.q.videoId == video_id))
        object_list = []
        for r in record_list:
            temp = Video(r.videoId, r.channelId, r.title, r.description, r.publishedAt,
                         r.viewCount, r.likeCount, r.dislikeCount, r.commentCount, r.timeIn)
            object_list.append(temp)
        return object_list

    @staticmethod
    def get_video_list():
        video_list = list(VideoTable.select(distinct=True))
        dictionary = {}
        for v in video_list:
            dictionary[v.videoId] = v.title
        return dictionary
