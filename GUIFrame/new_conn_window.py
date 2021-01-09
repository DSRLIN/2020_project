from .main_window import *
import tkinter as tk
from gl import *


class NewConnectionWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__user_label = None
        self.__passwd_label = None
        self.__host_label = None
        self.__instance_label = None
        self.__user_text = None
        self.__user_ent = None
        self.__passwd_text = None
        self.__passwd_ent = None
        self.__host_text = None
        self.__host_ent = None
        self.__instance_text = None
        self.__instance_ent = None
        self.__confirm_button = None

        self.__window_create()

    def __window_create(self):
        self.title("New Connection")
        self.geometry("400x220")
        gl.input_conn = False
        self.__user_label = tk.Label(self,
                                     text="User Name for DB:")
        self.__passwd_label = tk.Label(self,
                                       text="Password for DB:")
        self.__host_label = tk.Label(self,
                                     text="Host Address:")
        self.__instance_label = tk.Label(self,
                                         text="Instance Name:")
        self.__user_text = tk.StringVar()
        self.__user_ent = tk.Entry(self,
                                   textvariable=self.__user_text)
        self.__user_text.set("")
        self.__passwd_text = tk.StringVar()
        self.__passwd_ent = tk.Entry(self,
                                     textvariable=self.__passwd_text)
        self.__passwd_text.set("")
        self.__host_text = tk.StringVar()
        self.__host_ent = tk.Entry(self,
                                   textvariable=self.__host_text)
        self.__host_text.set("")
        self.__host_ent.insert(0, "localhost")
        self.__instance_text = tk.StringVar()
        self.__instance_ent = tk.Entry(self,
                                       textvariable=self.__instance_text)
        self.__instance_text.set("")
        self.__instance_ent.insert(0, "YDA_RES")
        self.__confirm_button = tk.Button(self,
                                          text="Confirm",
                                          command=self.on_click)
        self.pack_all()

    def pack_all(self):
        self.__user_label.pack()
        self.__user_ent.pack()
        self.__passwd_label.pack()
        self.__passwd_ent.pack()
        self.__host_label.pack()
        self.__host_ent.pack()
        self.__instance_label.pack()
        self.__instance_ent.pack()
        self.__confirm_button.pack()

    def on_click(self):
        u = self.__user_ent.get()
        p = self.__passwd_ent.get()
        h = self.__host_ent.get()
        i = self.__instance_ent.get()
        db_dict["user"] = u
        db_dict["password"] = p
        db_dict["host"] = h
        db_dict["instance"] = i
        gl.input_conn = db_conn_with_input()
        self.destroy()
