import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2\[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


class IPManager:
    @staticmethod
    def check_if_ip_valid(ip):
        return True if re.search(regex, ip) else False
