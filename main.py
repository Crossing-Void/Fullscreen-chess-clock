from Tkinter_template.Assets.project_management import create_menu
from Tkinter_template.Assets.music import Music
from Tkinter_template.base import Interface
from modules.main_effect import Effect
import time

Interface.rate = 1.0


class Main(Interface):
    def __init__(self, title: str, icon=None, default_menu=True):
        super().__init__(title, icon, default_menu)
        self.Musics = Music()
        # adjust 20 pixel
        self.dashboard['height'] = int(self.dashboard['height']) - 20
        self.dashboard_side = int(self.dashboard['width']), int(
            self.dashboard['height'])
        self.canvas['height'] = int(self.canvas['height']) - 20
        self.canvas_side = int(self.canvas['width']), int(
            self.canvas['height'])

        self.__create_menu_bar()

        Effect(self).enter()
    def __create_menu_bar(self):
        self.top_menu.add_cascade(label="New", menu=create_menu(self.top_menu))


if __name__ == "__main__":
    main = Main("Chess Clock", "favicon.ico", False)
    
    while True:
        try:
            main.canvas.update()
            time.sleep(0.01)
        except:
            
            1 / 0