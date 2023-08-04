from tkinter import *


class ProfileEditor:
    def __init__(self, main_screen, second_screen, profile_modifier, json_man, profile_name_entry, ip_entry):
        self.json_man = json_man
        self.main_screen = main_screen
        self.second_screen = second_screen
        self.profile_modifier = profile_modifier
        self.profile_name_entry = profile_name_entry
        self.ip_entry = ip_entry

    def save_changes(self):
        profiles = self.json_man.load_json("profiles.json")

        profiles[self.profile_name_entry.get()] = profiles.pop(self.second_screen.current_profile)
        profiles[self.profile_name_entry.get()]['host'] = self.ip_entry.get()
        profiles[self.profile_name_entry.get()]['ports'] = [
            int(i) for i in list(self.second_screen.listbox.get(0, END))
        ]

        self.json_man.save_json("profiles.json", profiles)

        idx = self.main_screen.listbox.get(0, END).index(self.second_screen.current_profile)
        self.main_screen.listbox.delete(idx)
        self.main_screen.listbox.insert(idx, self.profile_name_entry.get())
        self.second_screen.switch_page(self.main_screen)
        self.second_screen.edit_mode = False
