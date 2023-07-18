import tkinter
from tools.IPManager import IPManager
from tools.JsonManager import JsonManager
from tools.KnockManager import KnockManager
from tools.ProfileManager import ProfileManager


class Screen:
    def __init__(self, root):
        self.root = root
        self.frame = tkinter.Frame(self.root)

        self.json_man = JsonManager()
        self.profile_man = ProfileManager()
        self.ip_man = IPManager()
        self.knock_man = KnockManager()

    def start(self):
        self.frame.pack()
