from sqlobject import *
from DAO.Connection import base_conn
from Classes import Comment


class CommentTable(SQLObject):
    _connection = base_conn.get_connection()
    _connection.debug = True
    commentId = StringCol(length=40, notNone=True)
    videoId = StringCol(length=40, notNone=True)
    textOriginal = StringCol(notNone=True)
    authorName = StringCol(notNone=True)
    authorUrl = StringCol(notNone=True)
    authorId = StringCol(length=40, notNone=True)
    publishedAt = DateTimeCol(notNone=False)
    updatedAt = DateTimeCol(notNone=False)
    timeIn = TimestampCol()


class CommentDAO:
    @staticmethod
    def add_comment(*args):
        if len(args) == 1:
            if isinstance(args[0], Comment):
                return CommentDAO.__add_comment_o(comment_object=args[0])
            else:
                print('Error：传入对象类型错误 应为Comment 传入' + type(args[0]))
                return -1
        elif len(args) == 8:
            return CommentDAO.__add_comment_p(comment_id=args[0], video_id=args[1],
                                              text_original=args[2],
                                              author_name=args[3], author_url=args[4], author_id=args[5],
                                              published_at=args[6], updated_at=args[7])
        else:
            print('Error：参数不全时请使用传入实例对象的方式进行调用')
            return -1

    @staticmethod
    def __add_comment_o(comment_object):
        return CommentTable(commentId=Comment.get_comment_id(comment_object),
                            videoId=Comment.get_video_id(comment_object),
                            textOriginal=Comment.get_text_original(comment_object),
                            authorName=Comment.get_author_display_name(comment_object),
                            authorUrl=Comment.get_author_channel_url(comment_object),
                            authorId=Comment.get_author_channel_id(comment_object),
                            publishedAt=Comment.get_published_at(comment_object),
                            updatedAt=Comment.get_updated_at(comment_object)).id

    @staticmethod
    def __add_comment_p(comment_id, video_id, text_original, author_name, author_url, author_id, published_at,
                        updated_at):
        return CommentTable(commentId=comment_id, videoId=video_id, textOriginal=text_original,
                            authorName=author_name, authorUrl=author_url, authorId=author_id,
                            publishedAt=published_at, updatedAt=updated_at).id

    @staticmethod
    def delete_comment(rid):
        var = CommentTable.get(rid)
        CommentTable.delete(rid)
        return var

    @staticmethod
    def get_record(video_id):
        record_list = list(CommentTable.select(CommentTable.q.videoId == video_id))
        object_list = []
        for r in record_list:
            temp = Comment(r.commentId, r.videoId, r.textOriginal,
                           r.authorName, r.authorUrl, r.authorId,
                           r.publishedAt, r.updatedAt, r.timeIn)
            object_list.append(temp)
        return object_list
