import tkinter as tk
import webview


class FullScreenBrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WingerIT IntelliTest")

        # Set the window to full screen
        self.root.attributes('-fullscreen', True)
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.quit_fullscreen)

        # Remove the window title bar and borders
        self.root.overrideredirect(True)

        # Set the window icon
        self.set_icon()

        # Create a Frame to hold the browser
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create a browser window
        self.create_browser()

    def set_icon(self):
        # Set the icon for the Tkinter window
        # For cross-platform compatibility use .png file
        icon = tk.PhotoImage(file='logo.png')  # Change 'icon.png' to your file path
        self.root.iconphoto(True, icon)

    def create_browser(self):
        # Create a webview window and embed it in the Tkinter frame
        self.browser = webview.create_window("WingerIT IntelliTest", "https://winger-it-software.github.io/MCQ-Test/",
                                             width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(),
                                             resizable=True)
        webview.start(self.browser, gui='tkinter')

    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', True)

    def quit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        self.root.overrideredirect(False)  # Restore the window decorations


if __name__ == "__main__":
    root = tk.Tk()
    app = FullScreenBrowserApp(root)
    root.mainloop()
