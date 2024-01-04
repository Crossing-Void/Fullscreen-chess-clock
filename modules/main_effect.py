from Tkinter_template.Assets.project_management import canvas_reduction
from Tkinter_template.Assets.extend_widget import EffectButton
from Tkinter_template.Assets.soundeffect import play_sound
from Tkinter_template.Assets.image import tk_image
from Tkinter_template.Assets.font import font_get
import time

class Effect:
    button_name = ("Start", "Foooo", "Barrr", "Karti")
    def __init__(self, main):
        self.main = main
        self.c = self.main.canvas
        self.cs = self.main.canvas_side
    
    def __execute_commend(self, command: str):
        play_sound("main/press")

    
    def enter(self):
        def e(e):
            self.c["cursor"] = "icon"
            play_sound("main/enter")

        def l(e):
            self.c["cursor"] = "arrow"

        canvas_reduction(self.c, self.cs, self.main.Musics, "main.png")

        # create alphabat
        alphabat = ["H", "E", "S", "S", "L", "O", "C", "K"]
        width = 52 * 2.5
        for i in range(len(alphabat)):
            self.c.create_image(self.cs[0]//2 - width//2 + width*(i%4), 100 + width * (i//4), 
                                image=tk_image(f"{alphabat[i]}.png", int(width), dirpath="images\\main"), 
                                state="hidden", tags=("main", f"main-alphabat-{i}"))
        for i in range(17):
            self.c.create_image(self.cs[0]//2 - width*2 + i*15, 
                                100 + width / 2 - i*10, 
                                    image=tk_image("C.png", int(width*2), int(width*2), dirpath="images\\main"), 
                                    state="hidden", tags=("main", f"main-alphabat-head-{i}"))
        
        # showing
        for i in range(len(alphabat)):
            self.c.itemconfig(f"main-alphabat-{i}", state="normal")
            time.sleep(0.15)
            self.c.update()
            if i == 3:
                time.sleep(0.4)
        for i in range(16, -1, -1):
            self.c.itemconfig(f"main-alphabat-head-{i}", state="normal")
            self.c.update()
            time.sleep(0.02)
            if i == 0:
                break
            self.c.delete(f"main-alphabat-head-{i}")

        # button
        up_boundary, down_boundary = self.cs[1]*0.55, self.cs[1] - 50
        diff_boundary = (down_boundary - up_boundary) / (len(self.__class__.button_name) - 1)
        for i in range(len(self.__class__.button_name)):
            self.c.create_window(self.cs[0]//2, up_boundary + i*diff_boundary, 
                                 window=EffectButton(("#ff6b87", "#0000CD"), "main/enter", self.c, 
                                                     text=self.__class__.button_name[i], font=font_get(26),
                                                     bg="#DEB887", 
                                                     command=lambda n=self.__class__.button_name[i]: self.__execute_commend(n)))
        
        # setting
        
        
        self.c.create_image(self.cs[0]-20, self.cs[1]-20, anchor="se", 
                            image=tk_image("setting.png", 120, 120, dirpath="images\\system"), tags=("main", "setting"))
        self.c.tag_bind("setting", "<Enter>", e)
        self.c.tag_bind("setting", "<Leave>", l)
        self.c.tag_bind("setting", "<Button-1>", lambda e: self.__execute_commend("setting"))


        
