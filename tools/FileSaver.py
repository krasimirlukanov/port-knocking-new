from screens import SecondScreen
from tkinter import *
import tkinter


class FileSaver:
    def __init__(self, main_screen, second_screen, profile_man, json_man, profile_name_entry, ip_entry, ports):
        self.main_screen = main_screen
        self.second_screen: SecondScreen = second_screen

        self.profile_man = profile_man
        self.json_man = json_man

        self.profile_name_entry = profile_name_entry
        self.ip_entry = ip_entry

        self.ports = ports

    def save_file(self):
        if not self.second_screen.edit_mode:
            if not self.profile_man.check_if_profile_exists(self.profile_name_entry.get()):
                profiles = self.json_man.load_json("profiles.json")

                print(self.profile_name_entry.get())
                profiles[self.profile_name_entry.get()] = {}
                profiles[self.profile_name_entry.get()]["host"] = self.ip_entry.get()
                profiles[self.profile_name_entry.get()]["ports"] = self.ports

                self.json_man.save_json("profiles.json", profiles)

                self.second_screen.profile_update.update_profiles(self.profile_name_entry.get())
            else:
                tkinter.messagebox.showerror("Error!", "A profile with that name already exists!")
        else:
            profiles = self.json_man.load_json("profiles.json")

            profiles[self.profile_name_entry.get()] = profiles.pop(self.second_screen.current_profile)
            profiles[self.profile_name_entry.get()]['host'] = self.ip_entry.get()
            profiles[self.profile_name_entry.get()]['ports'] = self.ports

            self.json_man.save_json("profiles.json", profiles)

            idx = self.main_screen.listbox.get(0, END).index(self.second_screen.current_profile)
            self.main_screen.listbox.delete(idx)
            self.main_screen.listbox.insert(idx, self.profile_name_entry.get())
            self.second_screen.switch_page(self.main_screen)
            self.second_screen.edit_mode = False
