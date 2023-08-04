from tkinter import *


class LoadProfiles:
    def __init__(self, json_man, listbox):
        self.json_man = json_man
        self.listbox = listbox

    def load_profile_names(self):
        profiles = self.json_man.load_json("profiles.json")

        for i in profiles:
            self.listbox.insert(END, i)
