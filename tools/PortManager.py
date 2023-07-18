import tkinter
from tkinter import *


class PortManager:
    def __init__(self, listbox, port_entry, ports):
        self.listbox = listbox
        self.port_entry = port_entry
        self.ports = ports

    def add_port(self):
        if self.port_entry.get():
            try:
                self.listbox.insert(self.listbox.size(), self.port_entry.get())
                self.ports.append(int(self.port_entry.get()))
                self.port_entry.delete(0, END)
            except ValueError:
                tkinter.messagebox.showerror("Error!", "Invalid Port!")
                self.port_entry.delete(0, END)

    def delete_port(self):
        self.listbox.delete(tkinter.ANCHOR)
        content = self.listbox.get(0, END)
        self.ports.clear()
        for i in range(len(content)):
            self.ports.append(int(content[i]))
            print(self.ports)
