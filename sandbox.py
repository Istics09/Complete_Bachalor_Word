import tkinter as tk
import tkinter.font as tkFont

class CreateToolTip:
    """
    Tooltip létrehozása egy widgethez. A tooltip pozíciója a widget elhelyezkedésétől függ:
    - Bal oldali widget esetén a tooltip jobbra jelenik meg.
    - Jobb oldali widget esetén a tooltip balra jelenik meg.
    """
    def __init__(self, widget, text="widget info"):
        self.waittime = 500  # késleltetés ms-ban
        self.wraplength = 180  # alapértelmezett tördelési hossz (pixelben)
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def showtip(self, event=None):
        # Lekérjük a widget relatív pozícióját
        bbox = self.widget.bbox("insert")
        if bbox:
            x_rel, y_rel, cx, cy = bbox
        else:
            # Ha nincs 'insert', akkor alapértelmezett értékek
            x_rel, y_rel = 0, 0

        # Widget abszolút koordinátái
        abs_x = self.widget.winfo_rootx()
        abs_y = self.widget.winfo_rooty()

        # Képernyő szélessége
        screen_width = self.widget.winfo_screenwidth()

        # Döntés: ha a widget a képernyő bal felén van, a tooltip jobbra, ha jobb felén, akkor balra.
        if abs_x < screen_width / 2:
            x_offset = 25   # bal oldali widget => tooltip jobbra
        else:
            x_offset = -200  # jobb oldali widget => tooltip balra; ezt az értéket igény szerint módosíthatod

        tooltip_x = abs_x + x_rel + x_offset
        tooltip_y = abs_y + y_rel + 30

        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry(f"+{tooltip_x}+{tooltip_y}")

        # Dinamikus wraplength beállítás a szöveg szélessége alapján
        font = tkFont.Font(font=self.widget.cget("font"))
        text_width = font.measure(self.text)
        max_width = 300  # Maximum szélesség
        if text_width > max_width:
            wraplength = max_width
        else:
            wraplength = text_width + 10

        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         wraplength=wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        if self.tw:
            self.tw.destroy()
        self.tw = None

# Példa használat
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Tooltip elhelyezés példa")

    # Bal oldali menü
    left_menu = tk.Frame(root, width=200, bg="#2c3e50")
    left_menu.pack(side="left", fill="y")
    left_btn = tk.Button(left_menu, text="Bal menü gomb", font=('Helvetica', 12))
    left_btn.pack(padx=10, pady=10)
    CreateToolTip(left_btn, "Ez a tooltip jobbra fog megjelenni, mert a gomb a bal oldali menüben van.")

    # Jobb oldali menü
    right_menu = tk.Frame(root, width=200, bg="#34495e")
    right_menu.pack(side="right", fill="y")
    right_btn = tk.Button(right_menu, text="Jobb menü gomb", font=('Helvetica', 12))
    right_btn.pack(padx=10, pady=10)
    CreateToolTip(right_btn, "Ez a tooltip balra fog megjelenni, mert a gomb a jobb oldali menüben van.")

    root.mainloop()
