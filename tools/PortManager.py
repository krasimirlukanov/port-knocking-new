import tkinter
from tkinter import *


class PortManager:
    def __init__(self, listbox, port_entry):
        self.listbox = listbox
        self.port_entry = port_entry

    def add_port(self):
        if self.port_entry.get():
            try:
                self.listbox.insert(self.listbox.size(), self.port_entry.get())
                self.port_entry.delete(0, END)
            except ValueError:
                tkinter.messagebox.showerror("Error!", "Invalid Port!")
                self.port_entry.delete(0, END)

    def delete_port(self):
        self.listbox.delete(tkinter.ANCHOR)

    def get_ports_list(self):
        return [int(i) for i in list(self.listbox.get(0, END))]
