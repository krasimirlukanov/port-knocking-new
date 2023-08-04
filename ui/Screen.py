import tkinter
from tools.IPChecker import IPChecker
from tools.JsonFile import JsonFile
from tools.Knock import Knock
from tools.ProfileModifier import ProfileModifier
from tools.PortManager import PortManager


class Screen:
    def __init__(self, root):
        self.root = root
        self.frame = tkinter.Frame(self.root)

        self.json_file = JsonFile()
        self.profile_modifier = ProfileModifier()
        self.ip_checker = IPChecker()
        self.knocker = Knock(self.ip_checker)

    def start(self):
        self.frame.pack()
