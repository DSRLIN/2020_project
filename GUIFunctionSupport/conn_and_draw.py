# 将集成绘图功能
# 横轴为时间 纵轴为各量
# 图形为折线图
# 频道所需要的图：时间-观看 时间-总播放 时间-视频数 3合1
# 视频所需要的图：时间-观看 时间-赞 时间-踩 时间-评论数 4合1
from datetime import datetime
from datetime import timedelta

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

import gl
from Classes import *
from DAO import ChannelDAO, VideoDAO


def get_cn_data_n_draw(time):
    # 0 = 24h
    # 1 = 7d
    # 2 = 1m
    if time == 0:
        res = ChannelDAO.get_record(gl.cur_cn.get_channel_id())
        if len(res) is not 0:
            for i in res:
                if i.get_in_time() > datetime.now() + timedelta(hours=24):
                    res.remove(i)
            return draw_cn(res)
        else:
            return None
    elif time == 1:
        res = ChannelDAO.get_record(gl.cur_cn.get_channel_id())
        if len(res) is not 0:
            for i in res:
                if i.get_in_time() > datetime.now() + timedelta(days=7):
                    res.remove(i)
            return draw_cn(res)
        else:
            return None
    elif time == 2:
        res = ChannelDAO.get_record(gl.cur_cn.get_channel_id())
        if len(res) is not 0:
            for i in res:
                if i.get_in_time() > datetime.now() + timedelta(days=30):
                    res.remove(i)
            return draw_cn(res)
        else:
            return None
    else:
        print("Fatal Error!")


def get_vd_data_n_draw(time):
    # 0 = 24h
    # 1 = 7d
    # 2 = 1m
    if time == 0:
        res = VideoDAO.get_record(gl.cur_vd.get_video_id())
        if len(res) is not 0:
            for i in res:
                if i.get_in_time() > datetime.now() + timedelta(hours=24):
                    res.remove(i)
            return draw_vd(res)
        else:
            return None
    elif time == 1:
        res = VideoDAO.get_record(gl.cur_vd.get_video_id())
        if len(res) is not 0:
            for i in res:
                if i.get_in_time() > datetime.now() + timedelta(days=7):
                    res.remove(i)
            return draw_vd(res)
        else:
            return None
    elif time == 2:
        res = VideoDAO.get_record(gl.cur_vd.get_video_id())
        if len(res) is not 0:
            for i in res:
                if i.get_in_time() > datetime.now() + timedelta(days=30):
                    res.remove(i)
            return draw_vd(res)
        else:
            return None
    else:
        print("Fatal Error!")


def draw_vd(res_list: list):
    fig = plt.Figure(figsize=(9, 5.4), dpi=100)
    x_data = []
    y_data1 = []
    y_data2 = []
    y_data3 = []
    y_data4 = []
    ft = fm.FontProperties(fname=r"Deng.ttf")
    for i in res_list:
        i: Video
        x_data.append(i.get_in_time())
        y_data1.append(i.get_view_count())
        y_data2.append(i.get_like_count())
        y_data3.append(i.get_dislike_count())
        y_data4.append(i.get_comment_count())
    line1, = fig.add_subplot(221).plot(x_data, y_data1,
                                       color='red', linewidth=2.0,
                                       linestyle='--')
    axa = fig.gca()
    axa.spines['right'].set_color('none')
    axa.spines['top'].set_color('none')
    line2, = fig.add_subplot(222).plot(x_data, y_data2,
                                       color='green', linewidth=2.0,
                                       linestyle='-')
    axb = fig.gca()
    axb.spines['right'].set_color('none')
    axb.spines['top'].set_color('none')
    line3, = fig.add_subplot(223).plot(x_data, y_data3,
                                       color='blue', linewidth=2.0,
                                       linestyle='-.')
    axc = fig.gca()
    axc.spines['right'].set_color('none')
    axc.spines['top'].set_color('none')
    line4, = fig.add_subplot(224).plot(x_data, y_data4,
                                       color='purple', linewidth=2.0,
                                       linestyle=':')
    axd = fig.gca()
    axd.spines['right'].set_color('none')
    axd.spines['top'].set_color('none')
    fig.legend(handles=[line1, line2, line3, line4],
               labels=["观看曲线", "赞曲线", "踩曲线", "评论曲线"],
               prop=ft, loc='upper right')
    fig.suptitle(t="视频数据分析", fontproperties=ft)
    return fig


def draw_cn(res_list: list):
    fig = plt.Figure(figsize=(9, 5.4), dpi=100)
    x_data = []
    y_data1 = []
    y_data2 = []
    y_data3 = []
    ft = fm.FontProperties(fname=r"Deng.ttf")
    for i in res_list:
        i: Channel
        x_data.append(i.get_in_time())
        y_data1.append(i.get_view_count())
        y_data2.append(i.get_subscriber_count())
        y_data3.append(i.get_view_count())
    line1, = fig.add_subplot(221).plot(x_data, y_data1,
                                       color='red', linewidth=2.0,
                                       linestyle='--')
    axa = fig.gca()
    axa.spines['right'].set_color('none')
    axa.spines['top'].set_color('none')
    line2, = fig.add_subplot(222).plot(x_data, y_data2,
                                       color='green', linewidth=2.0,
                                       linestyle='-')
    axb = fig.gca()
    axb.spines['right'].set_color('none')
    axb.spines['top'].set_color('none')
    line3, = fig.add_subplot(223).plot(x_data, y_data2,
                                       color='blue', linewidth=2.0,
                                       linestyle='-.')
    axc = fig.gca()
    axc.spines['right'].set_color('none')
    axc.spines['top'].set_color('none')
    fig.legend(handles=[line1, line2, line3],
               labels=["订阅曲线", "播放曲线", "视频数曲线"],
               prop=ft, loc='upper right')
    fig.suptitle(t="频道数据分析", fontproperties=ft)
    return fig
