import tkinter as tk

class GUIApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("GUI Application")

        self.label = tk.Label(master, text="Hello, GUI!")
        self.label.pack()

        self.button = tk.Button(master, text="Click Me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApplication(root)
    root.mainloop()
