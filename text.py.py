import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
import tkinter.scrolledtext as tkst
import os
from tkinter import simpledialog
import fileinput


class OpenEdit:

    def __init__(self):

        # Root Frame widget

        self.root = Tk()

        sb = Scrollbar(self.root)
        sb.pack(side=RIGHT,fill=Y)


        # Menu panel in frame

        menubar = Menu(self.root)

        topframe = Frame(self.root)
        topframe.pack(side=TOP, anchor=W, fill=X)

        self.root['bg'] = 'white'
        new = PhotoImage(file='newpage.png')
        a = Button(topframe, image=new, command=self.new)
        a.pack(padx=5, pady=10,side = LEFT)

        open_photo = PhotoImage(file="open.png")
        b = Button(topframe, image=open_photo, command=self.open)
        b.pack(padx=5, pady=10,side = LEFT)

        save_photo = PhotoImage(file="Save-icon.png")
        c = Button(topframe, image=save_photo, command=self.save)
        c.pack(padx=5, pady=10, side=LEFT)

        cut_photo = PhotoImage(file="cut.png")
        d = Button(topframe, image=cut_photo, command=self.cut)
        d.pack(padx=5, pady=10, side=LEFT)

        copy_photo = PhotoImage(file="copy.png")
        e = Button(topframe, image=copy_photo, command=self.copy)
        e.pack(padx=5, pady=10, side=LEFT)

        paste_photo = PhotoImage(file="Paste.png")
        f = Button(topframe, image=paste_photo, command=self.paste)
        f.pack(padx=5, pady=10, side=LEFT)

        search_photo = PhotoImage(file="Search.png")
        g = Button(topframe, image=search_photo, command=self.find)
        g.pack(padx=5, pady=10, side=LEFT)

        # File menu,for open,save,save as and quit

        filemenu = Menu(menubar)
        editmenu = Menu(menubar)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="Open", command=self.open)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Save as", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        #Edit menu including Cut, Copy and Paste
        editmenu = Menu(menubar)
        editmenu.add_command(label="Cut", command=self.cut)
        editmenu.add_command(label="copy", command=self.copy)
        editmenu.add_command(label="Paste", command=self.paste)
        editmenu.add_command(label="Find", command=self.find)
        menubar.add_cascade(label="Edit", menu=editmenu)

        # About menu for show about us and help

        aboutmenu = Menu(menubar)
        aboutmenu.add_command(label="About", command=self.about)
        aboutmenu.add_command(label="Help", command=self.help)
        menubar.add_cascade(label="About", menu=aboutmenu)

        # Returning defined setting for GUI

        self.root.config(menu=menubar)





        #Setting up the title of the widget

        self.root.title("Text_Editor")

        # Adding Text Widget in the GUI

        self.text = Text(self.root)

        # This line allows it to be resized

        self.text.pack(expand=YES, fill=BOTH)

        self.root.mainloop()


        #Defining new method

    def new(self):
        self.root.title("Text_Editor")
        self.file = None
        self.text.delete(1.0,END)

    #Defining open method

    def open(self):

        self.file = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.file == "":

            #no file to open

            self.file = None
        else:

            #try to open the file
            #set the window title

            self.root.title(os.path.basename(self.file) + " - Text_Editor")
            self.text.delete(1.0,END)

            file = open(self.file,"r")

            self.text.insert(1.0,file.read())

            file.close()


    #Defining save method
    def save(self):
        fileName = self.file
        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    #Defining save_as method

    def save_as(self):

        fileName = filedialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def find(self):
        word = simpledialog.askstring("Find....", "Enter text:")
        self.text.tag_delete("search")
        if word:
            countvar = tkinter.StringVar()
            f = self.text.search(word, "1.0", count=countvar)
            starting_index = f
            ending_index = "{}+{}c".format(starting_index, countvar.get())
            self.text.tag_add("search", starting_index, ending_index)
            self.text.tag_configure("search", background="skyblue", foreground="red")
            return True
        else:
            return None


    #Defining cut method

    def cut(self):
        self.text.event_generate("<<Cut>>")

    #Defining copy method

    def copy(self):
        self.text.event_generate("<<Copy>>")

     #Defining paste method
    def paste(self):
        self.text.event_generate("<<Paste>>")

    #Defining about method

    def about(self):
        messagebox.showinfo("Text_Editor","Created by: CHANDAN BATEJA")

    #Defining help method

    def help(self):
        messagebox.showinfo("Help","This is help")


#Starting the instance of the class OpenEdit
OpenEdit()
