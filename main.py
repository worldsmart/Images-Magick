import tkinter as tk
from tkinter import filedialog
import os
from convertor import Convertor


class Main(tk.Frame):

    def __init__(self, frame):
        super().__init__(root)
        self.frame = frame
        self.app = tk.Frame(frame, bg='Gray')
        self.app.pack()

        self.target = False
        self.img = False
        self.convertor = False

        self.menu = tk.Menu(frame)
        frame.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.funcmenu = tk.Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.menu.add_cascade(label='Functions', menu=self.funcmenu)

        self.filemenu.add_cascade(label='Select', command=self.select)
        self.filemenu.add_cascade(label='Save', command=self.save)
        self.filemenu.add_cascade(label='Save as', command=self.saveAs)
        self.filemenu.entryconfigure(1, state=tk.DISABLED)
        self.filemenu.entryconfigure(2, state=tk.DISABLED)
        self.filemenu.add_separator()
        self.filemenu.add_cascade(label='Exit', command=self.close)

        self.funcmenu.add_cascade(label='Resize', command=self.resize)
        self.funcmenu.add_cascade(label='Blur', command=self.blur)

        tk.Frame(self.app, width=700, height=0).grid(row=0, column=0)

        tk.Canvas(self.app, width=700, height=400, bg='Gray', bd=0).grid(row=1, column=0)

    def close(self):
        self.frame.destroy()

    def select(self):
        self.convertor = Convertor(filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg", "*.jpg"), ("png", "*.png"), ("all files", "*.*"))))

        if self.target:
            self.target.destroy()
        self.target = tk.Label(self.app, text='TExt', image=self.convertor.tkImg)
        self.target.grid(row=1, column=0)
        self.filemenu.entryconfigure(1, state=tk.NORMAL)
        self.filemenu.entryconfigure(2, state=tk.NORMAL)

    def saveAs(self):
        self.convertor.saveAs(filedialog.asksaveasfilename(defaultextension='.png', initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"))))

    def save(self):
        self.convertor.save()

    def resize(self):
        Resize(self.convertor.resize, self.updateImg)

    def blur(self):
        Blur(self.convertor.blur, self.updateImg)

    def updateImg(self):
        if self.target:
            self.target.destroy()
        self.target = tk.Label(self.app, text='TExt', image=self.convertor.tkImg)
        self.target.grid(row=1, column=0)


class Resize(tk.Toplevel):

    def __init__(self, cb, update):
        super().__init__(root)
        self.title('Resize')
        self.resizable(False, False)

        self.cb = cb
        self.upd = update

        self.x = tk.IntVar()
        self.y = tk.IntVar()

        tk.Frame(self, width=300).grid(row=0, column=1, columnspan=5)

        tk.Label(self, text='X:').grid(row=1, column=1, padx=4, pady=4)
        tk.Label(self, text='Y:').grid(row=2, column=1, padx=4)
        tk.Entry(self, textvariable=self.x).grid(row=1, column=2, columnspan=4, padx=4, pady=4)
        tk.Entry(self, textvariable=self.y).grid(row=2, column=2, columnspan=4, padx=4)

        tk.Button(self, text='Resize', command=self.resize).grid(row=3, column=4, padx=4, pady=4)
        tk.Button(self, text='Close', command=self.destroy).grid(row=3, column=5, padx=4)

        self.grab_set()
        self.focus_set()

    def resize(self):
        self.cb(int(self.x.get()), int(self.y.get()))
        self.upd()
        self.destroy()


class Blur(tk.Toplevel):

    def __init__(self, cb, update):
        super().__init__(root)
        self.title('Blur')
        self.resizable(False, False)

        self.cb = cb
        self.upd = update

        self.x = tk.IntVar()

        tk.Frame(self, width=300).grid(row=0, column=1, columnspan=5)

        tk.Label(self, text='R:').grid(row=1, column=1, padx=4, pady=4)
        tk.Entry(self, textvariable=self.x).grid(row=1, column=2, columnspan=4, padx=4, pady=4)

        tk.Button(self, text='Blur', command=self.resize).grid(row=3, column=4, padx=4, pady=4)
        tk.Button(self, text='Close', command=self.destroy).grid(row=3, column=5, padx=4)

        self.grab_set()
        self.focus_set()

    def resize(self):
        self.cb(int(self.x.get()))
        self.upd()
        self.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Caster")
    root.resizable(False, False)
    root.iconphoto(False, tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), 'icon.png')))
    initial = Main(root)
    root.mainloop()
