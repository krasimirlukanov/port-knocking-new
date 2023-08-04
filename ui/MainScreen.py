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

        self.port_knock_text = Label(self.frame, text="Port Knocker", anchor="nw")
        self.port_knock_text.pack()

        self.author_text = Label(self.frame, text="by Krasimir Lukanov for ToolDomains")
        self.author_text.pack()

        self.profiles_text = Label(self.frame, text="Saved Profiles", anchor="nw")
        self.profiles_text.pack()

        self.port_knock_text.config(font=("Ariel", 15), anchor="nw")
        self.author_text.config(font=("Ariel", 10), anchor="nw")
        self.profiles_text.config(font=("Ariel", 10), anchor="nw")

        self.scrollbar = Scrollbar(self.frame)
        self.listbox = Listbox(self.frame, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack()

        self.new_profile_btn = Button(self.frame, text="New Profile", width=10, height=2,
                                      command=partial(self.switch_page, self.second_screen))
        self.edit_profile_btn = Button(self.frame, text="Edit Profile", width=10, height=2,
                                       command=self.open_profile)
        self.del_profile_btn = Button(self.frame, text="Delete Profile", width=10, height=2,
                                      command=partial(self.profile_modifier.delete_profile_ui, self.listbox))

        self.profile_knock = ProfileKnock(self.listbox, self.json_file, self.knocker)
        self.knock_btn = Button(self.frame, text="Knock", width=10, height=2, command=self.profile_knock.profile_knock)

        self.new_profile_btn.pack()
        self.edit_profile_btn.pack()
        self.del_profile_btn.pack()
        self.knock_btn.pack()

        self.profile_loader = LoadProfiles(self.json_file, self.listbox)
        self.profile_loader.load_profile_names()

    def open_profile(self):
        self.profile_modifier.open_profile(self.second_screen, listbox=self.listbox, ports=ports)
        self.switch_page(self.second_screen)
