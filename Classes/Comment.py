# -*- encoding:utf-8 -*-
from datetime import datetime
from jsonpath import jsonpath
from .time_converter import convert_time
import re


class Comment:

    def __init__(self, *args):
        if len(args) == 9:
            self.__init_from_details(args[0], args[1],
                                     args[2], args[3],
                                     args[4], args[5],
                                     args[6], args[7],
                                     args[8])
        elif len(args) == 1:
            self.__init_from_json(args[0])

    def __init_from_details(self,
                            comment_id, video_id,
                            text_original, author_display_name,
                            author_channel_url, author_channel_id,
                            published_at, updated_at,
                            in_time):
        self.__commentId = comment_id
        self.__videoId = video_id
        self.__textOriginal = text_original
        self.__authorDisplayName = author_display_name
        self.__authorChannelUrl = author_channel_url
        self.__authorChannelId = author_channel_id
        self.__publishedAt = published_at
        self.__updatedAt = updated_at
        self.__inTime = in_time
        self.self_check()
        self.standardization()

    def __init_from_json(self, video_json):
        """从json初始化"""
        self.__commentId = jsonpath(video_json, "$..id")[0]
        self.__videoId = jsonpath(video_json, "$...videoId")[0]
        self.__textOriginal = jsonpath(video_json, "$...textOriginal")[0]
        self.__authorDisplayName = jsonpath(video_json, "$...authorDisplayName")[0]
        self.__authorChannelUrl = jsonpath(video_json, "$...authorChannelUrl")[0]
        self.__authorChannelId = jsonpath(video_json, "$...value")[0]
        pre_json_time = jsonpath(video_json, "$...publishedAt")[0]
        self.__publishedAt = convert_time(pre_json_time)
        pre_json_time = jsonpath(video_json, "$...updatedAt")[0]
        self.__updatedAt = convert_time(pre_json_time)
        self.__inTime = datetime.now()
        self.self_check()
        self.standardization()

    def self_check(self):
        """需要检查publishedAt与updatedAt"""
        # 使用re
        # 若返回完整的表达式则证明没有修改
        if type(self.__publishedAt) is datetime:
            return
        resA = re.search(
            "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
            self.__publishedAt)
        if resA is None:
            return
        elif self.__publishedAt == resA.group(0):
            self.__publishedAt = convert_time(self.__publishedAt)

        if type(self.__updatedAt) is datetime:
            return
        resB = re.search(
            "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
            self.__updatedAt)
        if resB is None:
            return
        elif self.__updatedAt == resB.group(0):
            self.__updatedAt = convert_time(self.__updatedAt)

    def standardization(self):
        if type(self.__publishedAt) is datetime:
            return
        self.__publishedAt = datetime.strptime(self.__publishedAt,
                                               "%Y-%m-%d %H:%M:%S")
        if type(self.__updatedAt) is datetime:
            return
        self.__updatedAt = datetime.strptime(self.__updatedAt,
                                             "%Y-%m-%d %H:%M:%S")

    def get_comment_id(self):
        return self.__commentId

    def get_video_id(self):
        return self.__videoId

    def get_text_original(self):
        return self.__textOriginal

    def get_author_display_name(self):
        return self.__authorDisplayName

    def get_author_channel_url(self):
        return self.__authorChannelUrl

    def get_author_channel_id(self):
        return self.__authorChannelId

    def get_published_at(self):
        return self.__publishedAt

    def get_updated_at(self):
        return self.__updatedAt

    def get_in_time(self):
        return self.__inTime

    def set_comment_id(self, comment_id):
        self.__commentId = comment_id

    def set_video_id(self, video_id):
        self.__videoId = video_id

    def set_text_original(self, text_original):
        self.__textOriginal = text_original

    def set_author_display_name(self, author_display_name):
        self.__authorDisplayName = author_display_name

    def set_author_channel_url(self, author_channel_url):
        self.__authorChannelUrl = author_channel_url

    def set_author_channel_id(self, author_channel_id):
        self.__authorChannelId = author_channel_id

    def set_published_at(self, published_at):
        self.__publishedAt = published_at

    def set_updated_at(self, updated_at):
        self.__updatedAt = updated_at

    def set_in_time(self, in_time):
        self.__inTime = in_time
