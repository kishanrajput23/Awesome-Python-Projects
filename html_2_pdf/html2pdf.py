#!/usr/bin/python
# import modules

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import datetime
import pdfkit

# create the main window

win = tk.Tk()
win.title('HTML to PDF Converter')
win.resizable(False, False)
win.geometry('300x150')


# select

def sel():
    filetypes = (('HTML', '*.htm'), ('All files', '*.*'))
    fn = fd.askopenfilenames(title='Open files', initialdir='/',
                             filetypes=filetypes)
    showinfo(title='Selected Files', message=fn)
    return fn


fname = sel()


# convert

def con(fname):
    x = datetime.datetime.now()
    pdfkit.from_url(fname, 'convert_on_' + x + '.pdf')


openbtn = ttk.Button(win, text='Open', command=sel)
conv = ttk.Button(win, text='Convert', command=con)
openbtn.pack(expand=True)
conv.pack(expand=True)
win.mainloop()
