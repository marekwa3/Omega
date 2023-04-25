import tkinter as tk
from tkinter import ttk

class Tooltip:
    def __init__(self,widget,text):
        self.widget=widget
        self.text=text
        self.tipwindow=None

    def show_tip(self):
        if self.tipwindow or not self.text:
            return
        x,y,cx,cy=self.widget.bbox("insert")
        x+=self.widget.winfo_rootx()+25
        y+=self.widget.winfo_rooty()+20
        self.tipwindow=tw=tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d"%(x,y))
        label=ttk.Label(
            tw,text=self.text,justify=tk.LEFT,
            background="#ffffe0",relief=tk.SOLID,borderwidth=1,
            font=("tahoma","8","normal")
            )
        label.pack(ipadx=1)

    def hide_tip(self):
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow=None



