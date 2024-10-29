from tkinter import *

class MyFrame(Frame):
        def __init__(self, master):
                super(MyFrame, self).__init__(master)
                self.grid()
                self.create_widgets()

        def create_widgets(self):
                # create first button
                self.bttn_clicks = 0
                self.bttn1 = Button(self, text = "I do nothing! ")
                self.bttn1.grid(row =0, column= 0)
                # create second button
                self.bttn2 = Button(self)
                self.bttn2.grid(row =0, column= 1, columnspan= 4)

                self.bttn2.configure(text = " Button2");
                self.bttn2["text"]= "Total Clicks: 0"
                self.bttn2["command"] = self.update_count

                self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
                self.secret_txt.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        def update_count(self):
                self.bttn_clicks += 1
                self.bttn2["text"] = "Total Clicks: " + str(self.bttn_clicks)


def show_window_class():
        root = Tk()
        root.title("Simple GUI")
        root.geometry("500x300")
        # create a frame in the window to hold other widgets
        frame = MyFrame(root)
        frame.grid()

        root.mainloop()

def show_window():
        root = Tk()
        root.title("Simple GUI")
        root.geometry("500x300")
        # create a frame in the window to hold other widgets
        frame = Frame(root)
        frame.grid()

        lbl = Label(frame, text = "I'm a label!")
        lbl.grid()

        bttn1 = Button(frame, text = "I do nothing!")
        bttn1.grid()
        bttn1.configure(text = "New name")

        root.mainloop()

