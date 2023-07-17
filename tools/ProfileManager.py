from tools.IPManager import IPManager
from tools.JsonManager import JsonManager


class ProfileManager:
    def __init__(self):
        self.json_man = JsonManager()
        self.ip_man = IPManager()

    def new_profile(self, profile_name, ip, ports: list):
        if not self.check_if_profile_exists(profile_name) and self.ip_man.check_if_ip_valid(ip):
            profiles = self.json_man.load_json('tools/profiles.json')

            profiles[profile_name] = {}
            profiles[profile_name]['host'] = ip
            profiles[profile_name]['ports'] = ports

            self.json_man.save_json('tools/profiles.json', profiles)

    def delete_profile(self, profile_name):
        profiles = self.json_man.load_json('tools/profiles.json')
        profiles.pop(profile_name)
        self.json_man.save_json('tools/profiles.json', profiles)

    def check_if_profile_exists(self, profile_name):
        profiles = self.json_man.load_json('tools/profiles.json')

        for i in profiles:
            if i == profile_name:
                return True
        return False