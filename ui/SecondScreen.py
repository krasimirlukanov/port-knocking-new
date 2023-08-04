import tkinter.messagebox
from tkinter import *
from tools.FileSaver import FileSaver
from tools.PageSwitcher import PageSwitcher
from tools.ProfileEditor import ProfileEditor
from tools.ProfileSaver import ProfileSaver
from tools.ProfileUpdate import ProfileUpdate
from .Screen import Screen
from tools.PortManager import PortManager

from functools import partial


class SecondScreen(Screen, PageSwitcher):
    def __init__(self, root, main_screen):
        super().__init__(root=root)

        self.main_screen = main_screen
        self.edit_mode = False
        self.current_profile = ""
        self.text = Label(self.frame, text="IP Address:", width=20, anchor="nw")
        self.text.pack()

        self.ip_entry = Entry(self.frame)
        self.ip_entry.pack()

        self.empty_text_4 = Label(self.frame, height=1)
        self.empty_text_4.pack()

        self.ports_text = Label(self.frame, text="Ports:", width=20, anchor="nw")
        self.ports_text.pack()

        self.listbox = Listbox(self.frame, width=20, height=5)
        self.listbox.pack()

        self.empty_text_2 = Label(self.frame, height=1)
        self.empty_text_2.pack()

        self.empty_text_3 = Label(self.frame, text="Add Port:", width=20, anchor="nw")
        self.empty_text_3.pack()

        self.port_entry = Entry(self.frame, width=20)
        self.port_entry.pack()

        self.empty_text_4 = Label(self.frame, height=1)
        self.empty_text_4.pack()

        self.profile_name_text = Label(self.frame, text="Profile Name:", width=20, anchor="nw")
        self.profile_name_text.pack()

        self.profile_name_entry = Entry(self.frame)
        self.profile_name_entry.pack()

        self.port_manager = PortManager(self.listbox, self.port_entry)
        self.add_port_btn = Button(self.frame, text="Add Port",
                                   command=partial(PortManager(self.listbox, self.port_entry).add_port), width=10)
        self.add_port_btn.pack()
        self.knock_btn = Button(self.frame, text="Knock", command=self.knock_button_command,
                                width=10)
        self.knock_btn.pack()

        self.delete_port_btn = Button(self.frame, text="Delete",
                                      command=partial(PortManager(self.listbox, self.port_entry).delete_port),
                                      anchor="center", width=10)
        self.delete_port_btn.pack()

        self.profile_editor = ProfileEditor(self.main_screen, self, self.profile_modifier, self.json_file,
                                            self.profile_name_entry, self.ip_entry)
        self.file_saver = FileSaver(self.main_screen, self, self.profile_modifier, self.json_file,
                                    self.profile_name_entry, self.ip_entry, self.profile_editor)

        self.profile_saver = ProfileSaver(self.main_screen, self, self.ip_entry, self.profile_name_entry,
                                          self.file_saver, self.profile_editor, self.listbox)

        self.profile_update = ProfileUpdate(self.main_screen)

        self.save_btn = Button(self.frame, text="Save", command=self.profile_saver.save_profile, width=10)
        self.save_btn.pack()

        self.back = Button(self.frame, text="Go Back", command=partial(self.switch_page, self.main_screen),
                           anchor="center", width=10)
        self.back.pack()

    def switch_page(self, screen: Screen):
        self.ip_entry.delete(0, END)
        self.port_entry.delete(0, END)
        self.listbox.delete(0, END)
        self.profile_name_entry.delete(0, END)
        self.frame.pack_forget()
        screen.start()
        self.edit_mode = False

    def knock_button_command(self):
        self.knocker.knock(self.ip_entry.get(), self.port_manager.get_ports_list())
