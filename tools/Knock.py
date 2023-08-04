import socket
import select
from tkinter import messagebox
import tkinter


class Knock:
    def __init__(self, ip_checker):
        self.ip_checker = ip_checker

    def knock(self, ip, ports: list):
        if self.ip_checker.check_if_ip_valid(ip):
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setblocking(False)
                sock.settimeout(0.2)

                sock.connect_ex((ip, port))
                select.select([sock], [sock], [sock], 0)

                sock.close()
            tkinter.messagebox.showinfo("Ok!", "Knocking!")
        else:
            tkinter.messagebox.showerror("Error!", "Invalid IP Address!")
