import tkinter as tk

import gl
from gl import *


class ChannelInputWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__inputLabel = None
        self.__inputText = None
        self.__inputEnt = None
        self.__confirmButton = None

        self.__window_create()

    def __window_create(self):
        gl.cur_se = 0
        self.title("Input a Channel ID")
        self.geometry("300x85")
        gl.cn_in = ""
        self.__inputLabel = tk.Label(self,
                                     text="Input the Channel ID here:")
        self.__inputText = tk.StringVar()
        self.__inputEnt = tk.Entry(self,
                                   textvariable=self.__inputText)
        self.__inputText.set("")
        self.__confirmButton = tk.Button(self,
                                         text="Confirm",
                                         command=self.on_click)
        self.pack_all()

    def pack_all(self):
        self.__inputLabel.pack()
        self.__inputEnt.pack()
        self.__confirmButton.pack()

    def on_click(self):
        gl.cur_se = 2
        gl.cn_in = self.__inputEnt.get()
        res = ChannelDAO.get_record(gl.cn_in)
        if len(res) == 0:
            gl.cur_cn = None
        else:
            gl.cur_cn = ChannelDAO.get_record(gl.cn_in)[0]
        self.destroy()


