import tkinter
import tkinter.messagebox


class ProfileKnock:
    def __init__(self, listbox, json_man, knock):
        self.listbox = listbox
        self.json_man = json_man
        self.knocker = knock

    def profile_knock(self):
        idxs = self.listbox.curselection()
        if idxs:
            for pos in idxs:
                text = self.listbox.get(pos)

                profiles = self.json_man.load_json("profiles.json")

                ip = profiles[text]["host"]
                ports = [port for port in profiles[text]["ports"]]
                self.knocker.knock_button_command()
                tkinter.messagebox.showinfo("Ok!", "Knocking!")
        else:
            tkinter.messagebox.showerror("Error!", "Please select a profile and try again!")
