import socket
import select
from tools.JsonManager import JsonManager


class KnockManager:
    def __init__(self):
        self.json_man = JsonManager()

    @staticmethod
    def knock(ip, ports: list):
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(False)
            sock.settimeout(0.2)

            sock.connect_ex((ip, port))
            select.select([sock], [sock], [sock], 0)

            sock.close()

    def profile_knock(self, profile_name):
        profiles = self.json_man.load_json("tools/profiles.json")
        for i in profiles:
            if i == profile_name:
                self.knock(profiles[profile_name]['host'], profiles[profile_name]['ports'])
                return
        raise Exception("A profile with this name does not exist.")
