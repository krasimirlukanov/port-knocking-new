import tkinter.messagebox
from .SecondScreen import SecondScreen
from .Screen import Screen
from tkinter import *
from functools import partial

ports = []


class MainScreen(Screen):
    def __init__(self, root):
        super().__init__(root=root)
        self.frame.pack()
        self.second_screen = SecondScreen(self.root, self)

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

        self.knock_btn = Button(self.frame, text="Knock", width=10, height=2, command=self.knock)

        self.new_profile_btn.pack()
        self.open_profile_btn.pack()
        self.del_profile_btn.pack()
        self.knock_btn.pack()

        self.load_profile_names()

    def open_profile(self):
        self.profile_man.open_profile(self.second_screen, listbox=self.listbox, ports=ports)
        self.switch_page(self.second_screen)

    def knock(self):
        idxs = self.listbox.curselection()
        if not idxs:
            tkinter.messagebox.showerror("Error!", "Please select a profile and try again!")
        for pos in idxs:
            text = self.listbox.get(pos)

            profiles = self.json_man.load_json("tools/profiles.json")

            ip = profiles[text]["host"]
            ports.clear()
            for port in profiles[text]["ports"]:
                ports.append(port)

            self.knock_man.knock(ip, ports)
            tkinter.messagebox.showinfo("Ok!", "Knocking!")

    def load_profile_names(self):
        profiles = self.json_man.load_json("tools/profiles.json")

        for i in profiles:
            self.listbox.insert(END, str(i))
