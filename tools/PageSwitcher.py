class PageSwitcher:
    def __init__(self, frame):
        self.frame = frame

    def switch_page(self, screen):
        self.frame.forget()
        screen.start()
