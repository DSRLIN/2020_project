# Designed for Database
# Should Not Appear in User Part
from time import sleep

from NoVTBs import *
from gl import *


def get_data_of_video(video_id, quantities, time_sec):
    quant = 0
    while quant < quantities:
        # Test Part
        print(str(quant + 1) + " data with " + str(time_sec) + "s as time gap")
        # Test Part End
        tmpVideo = Video(video_raw_data(gen_video_param(video_id, apiKey)))
        tmpComment = Comment(
            comment_raw_data(gen_comment_param(video_id, apiKey)))
        VideoDAO.add_video(tmpVideo)
        CommentDAO.add_comment(tmpComment)
        sleep(time_sec)
        quant += 1


def get_data_of_channel(channel_id, quantities, time_sec):
    quant = 0
    while quant < quantities:
        # Test Part
        print(str(quant + 1) + " data with " + str(time_sec) + "s as time gap")
        # Test Part End
        tmpChannel = Channel(channel_raw_data(gen_channel_param(channel_id, apiKey)))
        ChannelDAO.add_channel(tmpChannel)
        sleep(time_sec)
        quant += 1
