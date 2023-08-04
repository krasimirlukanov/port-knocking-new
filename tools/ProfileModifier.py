import tkinter
from tkinter import *
from tools.IPChecker import IPChecker
from tools.JsonFile import JsonFile


class ProfileModifier:
    def __init__(self):
        self.json_file = JsonFile()
        self.ip_checker = IPChecker()

    def new_profile(self, profile_name, ip, ports: list):
        if not self.check_if_profile_exists(profile_name) and self.ip_checker.check_if_ip_valid(ip):
            profiles = self.json_file.load_json('profiles.json')

            profiles[profile_name] = {}
            profiles[profile_name]['host'] = ip
            profiles[profile_name]['ports'] = ports

            self.json_file.save_json('profiles.json', profiles)

    def delete_profile_ui(self, listbox):
        text = None
        idxs = listbox.curselection()

        if idxs:
            for pos in idxs:
                text = listbox.get(pos)
                listbox.delete(pos)

            profiles = self.json_file.load_json('profiles.json')
            profiles.pop(text)
            self.json_file.save_json('profiles.json', profiles)
        else:
            tkinter.messagebox.showerror("Error!", "Please select a profile and try again!")

    def open_profile(self, second_screen, listbox, ports):
        second_screen.edit_mode = True
        text = None
        idxs = listbox.curselection()
        if idxs:
            for pos in idxs:
                text = listbox.get(pos)
            profiles = self.json_file.load_json("profiles.json")

            second_screen.ip_entry.insert(0, profiles[text]["host"])
            ports.clear()
            for i in profiles[text]['ports']:
                second_screen.listbox.insert(END, str(i))
            second_screen.profile_name_entry.insert(0, text)
            second_screen.current_profile = text
        else:
            tkinter.messagebox.showerror("Error!", "Please select a profile and try again!")

    def check_if_profile_exists(self, profile_name):
        profiles = self.json_file.load_json('profiles.json')

        for i in profiles:
            if i == profile_name:
                return True
        return False
