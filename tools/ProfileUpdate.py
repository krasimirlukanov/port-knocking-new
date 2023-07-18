from tkinter import *


class ProfileUpdate:
    def __init__(self, main_screen):
        self.main_screen = main_screen

    def update_profiles(self, profile_name):
        self.main_screen.listbox.insert(END, profile_name)
