import tkinter as tk
from gl import *
from .main_window import *


class ChannelChooseWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__chooseLabel = None
        self.__listBox = None
        self.__scrollBar = None
        self.__confirmButton = None
        self.__window_create()

    def __window_create(self):
        gl.cur_se = 0
        self.title("Choose a Channel")
        self.geometry("400x255")
        self.__chooseLabel = tk.Label(self,
                                      text="Choose a Channel from the List")
        self.__scrollBar = tk.Scrollbar(self)
        # 由于需要将滚动条绑定给listBox
        # 因此脱离pack函数直接先进行pack
        self.__scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.__listBox = tk.Listbox(self,
                                    yscrollcommand=self.__scrollBar.set)
        self.get_and_insert()
        self.__confirmButton = tk.Button(self,
                                         text="Confirm",
                                         command=self.on_click)
        self.pack_all()

    def pack_all(self):
        self.__chooseLabel.pack()
        self.__listBox.pack(side=tk.TOP, fill=tk.BOTH)
        self.__confirmButton.pack()

    def get_and_insert(self):
        # Get
        gl.cn_dict = ChannelDAO.get_channel_list()
        # Insert
        for i in range(1, len(gl.cn_dict)):
            self.__listBox.insert(tk.END, list(gl.cn_dict.values())[i])

    def on_click(self):
        gl.cur_se = 2
        gl.cur_cn = ChannelDAO.get_record(self.get_dict_key(self.__listBox.get(
            self.__listBox.curselection()[0]))[0])[0]
        self.destroy()

    @staticmethod
    def get_dict_key(value):
        return [k for k, v in gl.cn_dict.items() if v == value]
