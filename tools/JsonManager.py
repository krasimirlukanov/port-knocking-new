import json


class JsonManager:
    @staticmethod
    def load_json(file_name):
        with open(f"{file_name}", 'r') as f:
            content = json.load(f)
            return content

    @staticmethod
    def save_json(file_name, content):
        with open(f"{file_name}", 'w') as f:
            json.dump(content, f)
