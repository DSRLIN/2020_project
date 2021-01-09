# -*- encoding:utf-8 -*-
from datetime import datetime
from jsonpath import jsonpath
from .time_converter import convert_time, channel_time
import re


class Channel:

    def __init__(self, *args):
        if len(args) == 8:
            self.__init_from_details(args[0], args[1],
                                     args[2], args[3],
                                     args[4], args[5],
                                     args[6], args[7])
            self.self_check()
        elif len(args) == 1:
            self.__init_from_json(args[0])

    def __init_from_details(self,
                            channel_id, title,
                            description, published_at,
                            view_count, subscriber_count,
                            video_count, in_time):
        """不得相信用户"""
        self.__channelId = channel_id
        self.__title = title
        self.__description = description
        self.__publishedAt = published_at
        self.__viewCount = view_count
        self.__subscriberCount = subscriber_count
        self.__videoCount = video_count
        self.__inTime = in_time
        self.self_check()
        self.standardization()

    def __init_from_json(self, video_json):
        """从json初始化"""
        self.__channelId = jsonpath(video_json, "$..id")[0]
        self.__title = jsonpath(video_json, "$..title")[0]
        self.__description = jsonpath(video_json, "$..description")[0]
        pre_json_time = jsonpath(video_json, "$..publishedAt")[0]
        self.__publishedAt = channel_time(pre_json_time)
        self.__viewCount = jsonpath(video_json, "$..viewCount")[0]
        self.__subscriberCount = jsonpath(video_json, "$..subscriberCount")[0]
        self.__videoCount = jsonpath(video_json, "$..videoCount")[0]
        self.__inTime = datetime.now()
        self.self_check()
        self.standardization()

    def self_check(self):
        """需要检查publishedAt"""
        # 使用re
        # 若返回完整的表达式则证明没有修改
        if type(self.__publishedAt) is datetime:
            return
        res = re.search(
                "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
                self.__publishedAt)
        if res is None:
            return
        elif self.__publishedAt == res.group(0):
            self.__publishedAt = convert_time(self.__publishedAt)

    def standardization(self):
        if type(self.__publishedAt) is datetime:
            return
        self.__publishedAt = datetime.strptime(self.__publishedAt,
                                               "%Y-%m-%d %H:%M:%S")
        self.__viewCount = int(self.__viewCount)
        self.__subscriberCount = int(self.__subscriberCount)
        self.__videoCount = int(self.__videoCount)

    def get_channel_id(self):
        return self.__channelId

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_published_at(self):
        return self.__publishedAt

    def get_view_count(self):
        return self.__viewCount

    def get_subscriber_count(self):
        return self.__subscriberCount

    def get_video_count(self):
        return self.__videoCount

    def get_in_time(self):
        return self.__inTime

    def set_channel_id(self, channel_id):
        self.__channelId = channel_id

    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_published_at(self, published_at):
        self.__publishedAt = published_at

    def set_view_count(self, view_count):
        self.__viewCount = view_count

    def set_subscriber_count(self, subscriber_count):
        self.__subscriberCount = subscriber_count

    def set_video_count(self, video_count):
        self.__videoCount = video_count

    def set_in_time(self, in_time):
        self.__inTime = in_time
