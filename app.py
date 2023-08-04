from tkinter import Tk
from ui.MainScreen import MainScreen

window = Tk()
window.title("Port Knocker")
window.geometry("400x450")
window.resizable(False, False)
app = MainScreen(window)
window.mainloop()
