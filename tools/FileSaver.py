from ui import SecondScreen
from tkinter import *
import tkinter


class FileSaver:
    def __init__(self, main_screen, second_screen, profile_man, json_man, profile_name_entry, ip_entry, profile_editor):
        self.main_screen = main_screen
        self.second_screen: SecondScreen = second_screen

        self.profile_man = profile_man
        self.profile_editor = profile_editor
        self.json_man = json_man

        self.profile_name_entry = profile_name_entry
        self.ip_entry = ip_entry

    def save_file(self):
        if not self.second_screen.edit_mode:
            if not self.profile_man.check_if_profile_exists(self.profile_name_entry.get()):
                profiles = self.json_man.load_json("profiles.json")

                profiles[self.profile_name_entry.get()] = {}
                profiles[self.profile_name_entry.get()]["host"] = self.ip_entry.get()
                profiles[self.profile_name_entry.get()]["ports"] = [
                    int(i) for i in list(self.second_screen.listbox.get(0, END))
                ]

                self.json_man.save_json("profiles.json", profiles)

                self.second_screen.profile_update.update_profiles(self.profile_name_entry.get())
            else:
                tkinter.messagebox.showerror("Error!", "A profile with that name already exists!")
        else:
            self.profile_editor.save_changes()
