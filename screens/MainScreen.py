from tools.LoadProfiles import LoadProfiles
from tools.PageSwitcher import PageSwitcher
from tools.ProfileKnock import ProfileKnock
from .SecondScreen import SecondScreen
from .Screen import Screen
from tkinter import *
from functools import partial

ports = []


class MainScreen(Screen, PageSwitcher):
    def __init__(self, root):
        super().__init__(root=root)
        self.frame.pack()
        self.second_screen: SecondScreen = SecondScreen(self.root, self)

        self.label = Label(self.frame, text="Port Knocker", anchor="nw")
        self.label.pack()

        self.label2 = Label(self.frame, text="by Krasimir Lukanov for ToolDomains")
        self.label2.pack()

        self.label3 = Label(self.frame, text="Saved Profiles", anchor="nw")
        self.label3.pack()

        self.label.config(font=("Ariel", 15), anchor="nw")
        self.label2.config(font=("Ariel", 10), anchor="nw")
        self.label3.config(font=("Ariel", 10), anchor="nw")

        self.scrollbar = Scrollbar(self.frame)
        self.listbox = Listbox(self.frame, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack()

        self.new_profile_btn = Button(self.frame, text="New Profile", width=10, height=2,
                                      command=partial(self.switch_page, self.second_screen))
        self.open_profile_btn = Button(self.frame, text="Edit Profile", width=10, height=2,
                                       command=self.open_profile)
        self.del_profile_btn = Button(self.frame, text="Delete Profile", width=10, height=2,
                                      command=partial(self.profile_man.del_profile, self.listbox))

        self.profile_knock = ProfileKnock(self.listbox, self.json_man, self.knock_man, ports)
        self.knock_btn = Button(self.frame, text="Knock", width=10, height=2, command=self.profile_knock.knock)

        self.new_profile_btn.pack()
        self.open_profile_btn.pack()
        self.del_profile_btn.pack()
        self.knock_btn.pack()

        profile_loader = LoadProfiles(self.json_man, self.listbox)
        profile_loader.load_profile_names()

    def open_profile(self):
        self.profile_man.open_profile(self.second_screen, listbox=self.listbox, ports=ports)
        self.switch_page(self.second_screen)
