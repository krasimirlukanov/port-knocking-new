import tkinter.messagebox
from .Screen import Screen
from tkinter import *
from functools import partial

ports = []


class SecondScreen(Screen):
    def __init__(self, root, main_screen):
        super().__init__(root=root)
        self.main_screen = main_screen

        self.edit_mode = False
        self.current_profile = ""
        self.text = Label(self.frame, text="IP Address:", width=20, anchor="nw")
        self.text.pack()

        self.ipEntry = Entry(self.frame)
        self.ipEntry.pack()

        self.emptyLabel1 = Label(self.frame, height=1)
        self.emptyLabel1.pack()

        self.text2 = Label(self.frame, text="Ports:", width=20, anchor="nw")
        self.text2.pack()

        self.listbox = Listbox(self.frame, width=20, height=5)
        self.listbox.pack()

        self.emptyLabel2 = Label(self.frame, height=1)
        self.emptyLabel2.pack()

        self.emptyLabel3 = Label(self.frame, text="Add Port:", width=20, anchor="nw")
        self.emptyLabel3.pack()

        self.port = Entry(self.frame, width=20)
        self.port.pack()

        self.emptyLabel4 = Label(self.frame, height=1)
        self.emptyLabel4.pack()

        self.text3 = Label(self.frame, text="Profile Name:", width=20, anchor="nw")
        self.text3.pack()

        self.profile_name = Entry(self.frame)
        self.profile_name.pack()

        self.button = Button(self.frame, text="Add Port",
                             command=partial(PortManager(self.listbox, self.port).add_port),
                             width=10)
        self.button.pack()

        self.button2 = Button(self.frame, text="Knock", command=self.knock, width=10)
        self.button2.pack()

        self.button3 = Button(self.frame, text="Delete",
                              command=partial(PortManager(self.listbox, self.port).delete_port),
                              anchor="center", width=10)
        self.button3.pack()

        self.save = Button(self.frame, text="Save", command=self.save_profile, width=10)
        self.save.pack()

        self.back = Button(self.frame, text="Go Back", command=partial(self.switch_page, self.main_screen), anchor="center", width=10)
        self.back.pack()

    def switch_page(self, screen):
        self.ipEntry.delete(0, END)
        self.port.delete(0, END)
        self.listbox.delete(0, END)
        self.profile_name.delete(0, END)
        self.frame.pack_forget()
        self.main_screen.start_page()

    def save_profile(self):
        if self.ipEntry.get():
            if self.profile_name.get():
                if len(ports) > 0:
                    self.save_file()
                    self.switch_page(self.main_screen)
                else:
                    tkinter.messagebox.showerror("Error!", "Please provide some ports!")
            else:
                tkinter.messagebox.showerror("Error!", "Please provide profile name!")
        else:
            tkinter.messagebox.showerror("Error!", "Please provide an IP Address!!")

    def save_file(self):
        if not self.edit_mode:
            if not self.profile_man.check_if_profile_exists(self.profile_name.get()):
                profiles = self.json_man.load_json("tools/profiles.json")

                profiles[self.profile_name.get()] = {}
                profiles[self.profile_name.get()]["host"] = self.ipEntry.get()
                profiles[self.profile_name.get()]["ports"] = ports

                self.json_man.save_json("tools/profiles.json", profiles)

                self.update_profiles(self.profile_name.get())
            else:
                tkinter.messagebox.showerror("Error!", "A profile with that name already exists!")
        else:
            print("nein")
            profiles = self.json_man.load_json("tools/profiles.json")

            profiles[self.profile_name.get()] = profiles.pop(self.current_profile)
            profiles[self.profile_name.get()]['host'] = self.ipEntry.get()
            profiles[self.profile_name.get()]['ports'] = ports

            self.json_man.save_json("tools/profiles.json", profiles)

            idx = self.main_screen.listbox.get(0, END).index(self.current_profile)
            self.main_screen.listbox.delete(idx)
            self.main_screen.listbox.insert(idx, self.profile_name.get())
            self.switch_page(self.main_screen)
            self.edit_mode = False

    def knock(self):
        if self.ip_man.check_if_ip_valid(self.ipEntry.get()):
            self.knock_man.knock(self.ipEntry.get(), ports=ports)
            tkinter.messagebox.showinfo("Ok!", "Knocking!")
        else:
            tkinter.messagebox.showerror("Error!", "Invalid IP Address!")

    def update_profiles(self, profile_name):
        self.main_screen.listbox.insert(END, profile_name)


class PortManager:
    def __init__(self, listbox, port_entry):
        self.listbox = listbox
        self.port_entry = port_entry

    def add_port(self):
        if self.port_entry.get():
            try:
                self.listbox.insert(self.listbox.size(), self.port_entry.get())
                ports.append(int(self.port_entry.get()))
                self.port_entry.delete(0, END)
            except ValueError:
                tkinter.messagebox.showerror("Error!", "Invalid Port!")
                self.port_entry.delete(0, END)

    def delete_port(self):
        self.listbox.delete(tkinter.ANCHOR)
        content = self.listbox.get(0, END)
        ports.clear()
        for i in range(len(content)):
            ports.append(int(content[i]))
            print(ports)
