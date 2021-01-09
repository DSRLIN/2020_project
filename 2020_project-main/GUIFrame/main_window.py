import tkinter as tk
from time import sleep

from GUIFunctionSupport import *
import gl
from .channel_input_window import ChannelInputWindow
from .new_conn_window import *
from .channel_input_window import *
from .channel_choose_window import *
from .new_conn_window import NewConnectionWindow
from .video_input_window import *
from .video_choose_window import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainWindow(tk.Tk):
    def __init__(self, main_name: str):
        # 变量集
        super().__init__()
        self.__label = None  # 测试标签
        self.__draw = False
        self.__menu_bar = None
        self.init_window_name = main_name
        # 详见图
        self.__window_frame_topA = None
        self.__window_frame_topB = None
        self.__window_frame_leftA = None
        self.__window_frame_leftB = None
        self.__window_frame_rightA = None
        self.__window_frame_rightB = None
        # 虽然非开发者也不一定看得见
        self.__topALabel = None
        self.__topBLabel = None
        self.__leftACanvas = None
        self.__leftBEntLabel = None
        self.__leftBText = None
        self.rightALabelA = None
        self.rightALabelB = None
        self.rightALabelC = None
        self.rightALabelD = None
        self.__rightBButtonA = None
        self.__rightBButtonB = None
        self.__rightBButtonC = None
        self.__rightBButtonD = None
        # self.__window = tk.Tk()
        self.__click = 0
        # 变量集完
        self.window_create()

    def window_create(self):
        self.title(self.init_window_name)
        self.geometry("1280x800")
        # 测试部分
        # self.__label = tk.Label(self.__window, text=" ")
        # self.__label.pack()
        # 测试部分完
        self.__menu_bar_create()
        self.main_window_frames()
        self.things_on_frames()
        self.__start()

    def __menu_bar_create(self):
        self.__menu_bar = tk.Menu(self)
        config_bar = tk.Menu(self.__menu_bar, tearoff=0)
        analyze_bar = tk.Menu(self.__menu_bar, tearoff=0)
        self.__menu_bar.add_cascade(label='Config', menu=config_bar)
        config_bar.add_command(label='New Connection',
                               command=self.new_conn)
        config_bar.add_command(label='Use Current Config',
                               command=self.use_curr_conf)
        config_bar.add_separator()
        config_bar.add_command(label='Save Current Config to File',
                               command=self.save_curr_conf)

        self.__menu_bar.add_cascade(label='Analyze', menu=analyze_bar)
        analyze_bar_sub = tk.Menu(analyze_bar, tearoff=0)
        analyze_bar.add_cascade(label='Analyze Video',
                                menu=analyze_bar_sub)
        analyze_bar_sub.add_command(label='Choose From Database',
                                    command=self.choose_vd)
        analyze_bar_sub.add_command(label='Input a Video ID',
                                    command=self.new_vd_analyze)
        analyze_bar_sub_channel = tk.Menu(analyze_bar, tearoff=0)
        analyze_bar.add_cascade(label='Analyze Channel',
                                menu=analyze_bar_sub_channel)
        analyze_bar_sub_channel.add_command(label='Choose From Database',
                                            command=self.choose_cn)
        analyze_bar_sub_channel.add_command(label='Input a Channel ID',
                                            command=self.new_cn_analyze)
        analyze_bar.add_separator()
        # api被拒了 看起来没得爬了
        # 之后看看手动能不能爬一两条来
        analyze_bar_sub_tweet = tk.Menu(analyze_bar, tearoff=0)
        analyze_bar.add_cascade(label='Get a New Tweet',
                                menu=analyze_bar_sub_tweet)
        analyze_bar_sub_tweet.add_command(label='Input Source',
                                          command=self.__empty_func)
        tweet_sub = tk.Menu(analyze_bar_sub_tweet, tearoff=0)
        analyze_bar_sub_tweet.add_cascade(label='Choose From List',
                                          menu=tweet_sub)
        # 在这两条注释内添加tag/@
        tweet_sub.add_command(label='@realDonaldTrump（尊）',
                              command=self.__empty_func)
        tweet_sub.add_command(label='#桐生ココ',
                              command=self.__empty_func)
        tweet_sub.add_command(label='#みかじ絵',
                              command=self.__empty_func)
        tweet_sub.add_command(label='#holoJPmeme',
                              command=self.__empty_func)
        tweet_sub.add_command(label='# ホロライブアイドル道',
                              command=self.__empty_func)
        # 结束
        self.config(menu=self.__menu_bar)

    def main_window_frames(self):
        self.__window_frame_topA = tk.Frame(self,
                                            bg="red",
                                            height=20,
                                            width=960)
        self.__window_frame_topA.place(x=0, y=0, anchor=tk.NW)
        self.__window_frame_topB = tk.Frame(self,
                                            bg="green",
                                            height=20,
                                            width=320)
        self.__window_frame_topB.place(x=960, y=0, anchor=tk.NW)
        self.__window_frame_leftA = tk.Frame(self,
                                             bg="yellow",
                                             height=600,
                                             width=960)
        self.__window_frame_leftA.place(x=0, y=20, anchor=tk.NW)
        self.__window_frame_leftB = tk.Frame(self,
                                             bg="blue",
                                             height=200,
                                             width=960)
        self.__window_frame_leftB.place(x=0, y=620, anchor=tk.NW)
        self.__window_frame_rightA = tk.Frame(self,
                                              bg="purple",
                                              height=540,
                                              width=320)
        self.__window_frame_rightA.place(x=960, y=20, anchor=tk.NW)
        self.__window_frame_rightB = tk.Frame(self,
                                              bg="cyan",
                                              height=360,
                                              width=320)
        self.__window_frame_rightB.place(x=960, y=560, anchor=tk.NW)

    def things_on_frames(self):
        self.__topALabel = tk.Label(self.__window_frame_topA,
                                    text="Analyze Part")
        self.__topBLabel = tk.Label(self.__window_frame_topB,
                                    text="Function Part")
        self.__topALabel.pack()
        self.__topBLabel.pack()
        self.__leftBEntLabel = tk.Label(self.__window_frame_leftB,
                                        text="Logs")
        self.__leftBEntLabel.place(x=0, y=0,
                                   anchor=tk.NW)
        self.__leftBText = tk.Text(self.__window_frame_leftB,
                                   width=135,
                                   height=11
                                   )
        self.__leftBText.place(x=2, y=26,
                               anchor=tk.NW)
        self.rightALabelA = tk.Label(self.__window_frame_rightA,
                                     text="Undefined",
                                     justify=tk.LEFT,
                                     wraplength=300)
        self.rightALabelB = tk.Label(self.__window_frame_rightA,
                                     text="Undefined",
                                     justify=tk.LEFT,
                                     wraplength=300)
        self.rightALabelC = tk.Label(self.__window_frame_rightA,
                                     text="Undefined",
                                     justify=tk.LEFT,
                                     wraplength=300)
        self.rightALabelD = tk.Label(self.__window_frame_rightA,
                                     text="Undefined",
                                     justify=tk.LEFT,
                                     wraplength=300)
        self.rightALabelA.place(x=10, y=10,
                                anchor=tk.NW)
        self.rightALabelB.place(x=10, y=70,
                                anchor=tk.NW)
        self.rightALabelC.place(x=10, y=130,
                                anchor=tk.NW)
        self.rightALabelD.place(x=10, y=190,
                                anchor=tk.NW)
        self.__rightBButtonA = tk.Button(self.__window_frame_rightB,
                                         text="Last 24 Hours",
                                         height=2, width=15,
                                         command=self.click_a)
        self.__rightBButtonB = tk.Button(self.__window_frame_rightB,
                                         text="Last 7 Days",
                                         height=2, width=15,
                                         command=self.click_b)
        self.__rightBButtonC = tk.Button(self.__window_frame_rightB,
                                         text="Last Month",
                                         height=2, width=15,
                                         command=self.click_c)
        self.__rightBButtonD = tk.Button(self.__window_frame_rightB,
                                         text="Clear All",
                                         height=2, width=15,
                                         command=self.click_d)
        self.__rightBButtonA.place(x=30, y=40, anchor=tk.NW)
        self.__rightBButtonB.place(x=175, y=40, anchor=tk.NW)
        self.__rightBButtonC.place(x=30, y=150, anchor=tk.NW)
        self.__rightBButtonD.place(x=175, y=150, anchor=tk.NW)

    def __start(self):
        self.mainloop()

    def __empty_func(self):
        self.__click += 1

    def new_conn(self):
        n = NewConnectionWindow()
        self.wait_window(n)
        if gl.input_conn:
            self.rightALabelA.config(text="Host:" + str(gl.dbc.get_conn_info()[2]))
            self.rightALabelB.config(text="Instance:" + str(gl.dbc.get_conn_info()[3]))
            self.rightALabelC.config(text="Connected")
            self.rightALabelD.config(text="")
        else:
            self.rightALabelA.config(text="Connection Failed")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def choose_vd(self):
        if gl.dbc.get_connection_status():
            gl.cur_vd = None
            v = VideoChooseWindow()
            self.wait_window(v)
            if gl.cur_vd is None:
                self.rightALabelA.config(text="This Video is Not in the Database!")
                self.rightALabelB.config(text="")
                self.rightALabelC.config(text="")
                self.rightALabelD.config(text="")
            else:
                self.rightALabelA.config(text="Video Name:" + gl.cur_vd.get_title())
                self.rightALabelB.config(text="Video Publish Time:\n" +
                                              str(gl.cur_vd.get_published_at()))
                self.rightALabelC.config(text="Video Description:\n" +
                                              gl.cur_vd.get_description())
                self.rightALabelD.config(text="")
        else:
            self.rightALabelA.config(text="You Need to Connect to a Database First!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def choose_cn(self):
        if gl.dbc.get_connection_status():
            gl.cur_cn = None
            c = ChannelChooseWindow()
            self.wait_window(c)
            if gl.cur_cn is None:
                self.rightALabelA.config(text="This Channel is Not in the Database!")
                self.rightALabelB.config(text="")
                self.rightALabelC.config(text="")
                self.rightALabelD.config(text="")
            else:
                self.rightALabelA.config(text="Channel Name:" + gl.cur_cn.get_title())
                self.rightALabelB.config(text="Channel Create Time:\n" +
                                              str(gl.cur_cn.get_published_at()))
                self.rightALabelC.config(text="Channel Description:\n" +
                                              gl.cur_cn.get_description())
                self.rightALabelD.config(text="")
        else:
            self.rightALabelA.config(text="You Need to Connect to a Database First!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def new_vd_analyze(self):
        if gl.dbc.get_connection_status():
            gl.cur_vd = None
            v = VideoInputWindow()
            self.wait_window(v)
            if gl.cur_vd is None:
                self.rightALabelA.config(text="This Video is Not in the Database!")
                self.rightALabelB.config(text="")
                self.rightALabelC.config(text="")
                self.rightALabelD.config(text="")
            else:
                self.rightALabelA.config(text="Video Name:" + gl.cur_vd.get_title())
                self.rightALabelB.config(text="Video Publish Time:\n" +
                                              str(gl.cur_vd.get_published_at()))
                self.rightALabelC.config(text="Video Description:\n" +
                                              gl.cur_vd.get_description())
                self.rightALabelD.config(text="")
        else:
            self.rightALabelA.config(text="You Need to Connect to a Database First!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def new_cn_analyze(self):
        if gl.dbc.get_connection_status():
            gl.cur_cn = None
            c = ChannelInputWindow()
            self.wait_window(c)
            if gl.cur_cn is None:
                self.rightALabelA.config(text="This Channel is Not in the Database!")
                self.rightALabelB.config(text="")
                self.rightALabelC.config(text="")
                self.rightALabelD.config(text="")
            else:
                self.rightALabelA.config(text="Channel Name:" + gl.cur_cn.get_title())
                self.rightALabelB.config(text="Channel Create Time:\n" +
                                              str(gl.cur_cn.get_published_at()))
                self.rightALabelC.config(text="Channel Description:\n" +
                                              gl.cur_cn.get_description())
                self.rightALabelD.config(text="")
        else:
            self.rightALabelA.config(text="You Need to Connect to a Database First!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def use_curr_conf(self):
        res = db_conn_with_conf()
        if res:
            self.rightALabelA.config(text="Host:" + str(gl.dbc.get_conn_info()[2]))
            self.rightALabelB.config(text="Instance:" + str(gl.dbc.get_conn_info()[3]))
            self.rightALabelC.config(text="Connected")
            self.rightALabelD.config(text="")
        else:
            self.rightALabelA.config(text="Connection Failed")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def save_curr_conf(self):
        res = save_conf_to_file()
        if res:
            self.rightALabelA.config(text="Config File Saved")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")
        else:
            self.rightALabelA.config(text="Config File Save Failed")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def click_a(self):
        if gl.cur_se == 0:
            self.rightALabelA.config(text="You Need to Choose a Video/Channel!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")
        elif gl.cur_se == 1:
            if self.__draw is False:
                self.__draw = True
                fig = get_vd_data_n_draw(0)
                self.__leftACanvas = FigureCanvasTkAgg(fig, master=self.__window_frame_leftA)
                self.__leftACanvas.draw()
                self.__leftACanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        elif gl.cur_se == 2:
            # cn
            if self.__draw is False:
                self.__draw = True
                fig = get_cn_data_n_draw(0)
                self.__leftACanvas = FigureCanvasTkAgg(fig, master=self.__window_frame_leftA)
                self.__leftACanvas.draw()
                self.__leftACanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        else:
            self.rightALabelA.config(text="Fatal Error!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def click_b(self):
        if gl.cur_se == 0:
            self.rightALabelA.config(text="You Need to Choose a Video/Channel!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")
        elif gl.cur_se == 1:
            if self.__draw is False:
                self.__draw = True
                fig = get_vd_data_n_draw(1)
                self.__leftACanvas = FigureCanvasTkAgg(fig, master=self.__window_frame_leftA)
                self.__leftACanvas.draw()
                self.__leftACanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        elif gl.cur_se == 2:
            # cn
            self.__draw = True
            fig = get_cn_data_n_draw(1)
            self.__leftACanvas = FigureCanvasTkAgg(fig, master=self.__window_frame_leftA)
            self.__leftACanvas.draw()
            self.__leftACanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            pass
        else:
            self.rightALabelA.config(text="Fatal Error!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def click_c(self):
        if gl.cur_se == 0:
            self.rightALabelA.config(text="You Need to Choose a Video/Channel!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")
        elif gl.cur_se == 1:
            if self.__draw is False:
                self.__draw = True
                fig = get_vd_data_n_draw(2)
                self.__leftACanvas = FigureCanvasTkAgg(fig, master=self.__window_frame_leftA)
                self.__leftACanvas.draw()
                self.__leftACanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        elif gl.cur_se == 2:
            # cn
            self.__draw = True
            fig = get_cn_data_n_draw(2)
            self.__leftACanvas = FigureCanvasTkAgg(fig, master=self.__window_frame_leftA)
            self.__leftACanvas.draw()
            self.__leftACanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            pass
        else:
            self.rightALabelA.config(text="Fatal Error!")
            self.rightALabelB.config(text="")
            self.rightALabelC.config(text="")
            self.rightALabelD.config(text="")

    def click_d(self):
        gl.cur_se = 0
        self.__leftACanvas.get_tk_widget().pack_forget()
        self.__draw = False
        self.rightALabelA.config(text="")
        self.rightALabelB.config(text="")
        self.rightALabelC.config(text="")
        self.rightALabelD.config(text="")

