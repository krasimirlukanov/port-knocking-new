import tkinter


class ProfileSaver:
    def __init__(self, main_screen, second_screen, ip_entry, profile_name_entry, file_saver, profile_editor, listbox):
        self.main_screen = main_screen
        self.second_screen = second_screen

        self.ip_entry = ip_entry
        self.profile_name_entry = profile_name_entry
        self.file_saver = file_saver
        self.profile_editor = profile_editor
        self.listbox = listbox

    def save_profile(self):
        if self.ip_entry.get():
            if self.profile_name_entry.get():
                if self.listbox.size() > 0:
                    self.file_saver.save_file()
                    self.second_screen.switch_page(self.main_screen)
                else:
                    tkinter.messagebox.showerror("Error!", "Please provide some ports!")
            else:
                tkinter.messagebox.showerror("Error!", "Please provide profile name!")
        else:
            tkinter.messagebox.showerror("Error!", "Please provide an IP Address!!")
