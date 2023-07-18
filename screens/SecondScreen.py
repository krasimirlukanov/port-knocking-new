import tkinter.messagebox
from tkinter import *

from tools.FileSaver import FileSaver
from tools.PageSwitcher import PageSwitcher
from tools.ProfileSaver import ProfileSaver
from tools.ProfileUpdate import ProfileUpdate
from .Screen import Screen
from tools.PortManager import PortManager

from functools import partial


ports = []


class SecondScreen(Screen, PageSwitcher):
    def __init__(self, root, main_screen):
        super().__init__(root=root)

        self.main_screen = main_screen

        self.edit_mode = False
        self.current_profile = ""
        self.text = Label(self.frame, text="IP Address:", width=20, anchor="nw")
        self.text.pack()

        self.ip_entry = Entry(self.frame)
        self.ip_entry.pack()

        self.emptyLabel1 = Label(self.frame, height=1)
        self.emptyLabel1.pack()

        self.text2 = Label(self.frame, text="Ports:", width=20, anchor="nw")
        self.text2.pack()

        self.listbox = Listbox(self.frame, width=20, height=5)
        self.listbox.pack()

        self.emptyLabel2 = Label(self.frame, height=1)
        self.emptyLabel2.pack()

        self.emptyLabel3 = Label(self.frame, text="Add Port:", width=20, anchor="nw")
        self.emptyLabel3.pack()

        self.port = Entry(self.frame, width=20)
        self.port.pack()

        self.emptyLabel4 = Label(self.frame, height=1)
        self.emptyLabel4.pack()

        self.text3 = Label(self.frame, text="Profile Name:", width=20, anchor="nw")
        self.text3.pack()

        self.profile_name_entry = Entry(self.frame)
        self.profile_name_entry.pack()

        self.button = Button(self.frame, text="Add Port",
                             command=partial(PortManager(self.listbox, self.port, ports).add_port),
                             width=10)
        self.button.pack()

        self.button2 = Button(self.frame, text="Knock", command=self.knock, width=10)
        self.button2.pack()

        self.button3 = Button(self.frame, text="Delete",
                              command=partial(PortManager(self.listbox, self.port, ports).delete_port),
                              anchor="center", width=10)
        self.button3.pack()

        self.file_saver = FileSaver(self.main_screen, self, self.profile_man, self.json_man, self.profile_name_entry,
                                    self.ip_entry, ports)
        self.profile_saver = ProfileSaver(self.main_screen, self, self.ip_entry, self.profile_name_entry,
                                          self.file_saver, ports)

        self.profile_update = ProfileUpdate(self.main_screen)

        self.save = Button(self.frame, text="Save", command=self.profile_saver.save_profile, width=10)
        self.save.pack()

        self.back = Button(self.frame, text="Go Back", command=partial(self.switch_page, self.main_screen),
                           anchor="center", width=10)
        self.back.pack()

    def switch_page(self, screen: Screen):
        self.ip_entry.delete(0, END)
        self.port.delete(0, END)
        self.listbox.delete(0, END)
        self.profile_name_entry.delete(0, END)
        self.frame.pack_forget()
        screen.start()

    def knock(self):
        if self.ip_man.check_if_ip_valid(self.ip_entry.get()):
            self.knock_man.knock(self.ip_entry.get(), ports=ports)
            tkinter.messagebox.showinfo("Ok!", "Knocking!")
        else:
            tkinter.messagebox.showerror("Error!", "Invalid IP Address!")
