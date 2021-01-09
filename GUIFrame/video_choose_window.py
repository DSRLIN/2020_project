import gl
from .main_window import *
import tkinter as tk
from DAO import VideoDAO
from gl import *


class VideoChooseWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__chooseLabel = None
        self.__listBox = None
        self.__scrollBar = None
        self.__confirmButton = None

        self.__window_create()

    def __window_create(self):
        gl.cur_se = 0
        self.title("Choose a Video")
        self.geometry("400x255")
        self.__chooseLabel = tk.Label(self,
                                      text="Choose a Video from the List")
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
        gl.vd_dict = VideoDAO.get_video_list()
        # Insert
        for i in range(1, len(gl.vd_dict)):
            self.__listBox.insert(tk.END, list(gl.vd_dict.values())[i])

    def on_click(self):
        gl.cur_se = 1
        gl.cur_vd = VideoDAO.get_record(self.get_dict_key(self.__listBox.get(
            self.__listBox.curselection()[0]))[0])[0]
        self.destroy()

    @staticmethod
    def get_dict_key(value):
        return [k for k, v in gl.vd_dict.items() if v == value]
