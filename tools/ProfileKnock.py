import tkinter
import tkinter.messagebox


class ProfileKnock:
    def __init__(self, listbox, json_man, knock_man, ports):
        self.listbox = listbox
        self.json_man = json_man
        self.knock_man = knock_man
        self.ports = ports

    def knock(self):
        idxs = self.listbox.curselection()
        if not idxs:
            tkinter.messagebox.showerror("Error!", "Please select a profile and try again!")
        for pos in idxs:
            text = self.listbox.get(pos)

            profiles = self.json_man.load_json("profiles.json")

            ip = profiles[text]["host"]
            self.ports.clear()
            for port in profiles[text]["ports"]:
                self.ports.append(port)

            self.knock_man.knock(ip, self.ports)
            tkinter.messagebox.showinfo("Ok!", "Knocking!")
