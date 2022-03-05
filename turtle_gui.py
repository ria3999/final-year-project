import turtle
import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("GUI")
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=600, height=400)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("grey")
        self.button = tk.Button(self.master, text="Get Dimension", command=self.press,bd=10,bg="black",fg="white",justify="left",padx=10,pady=10,relief="sunken")
        self.button.pack()
        self.button.place(x=325, y=325)
        self.button1 = tk.Button(self.master, text="Get Distance", command=self.press,bd=10,bg="black",fg="white",justify="left",padx=10,pady=10,relief="sunken")
        self.button1.pack()
        self.button1.place(x=125, y=325)
        #self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
        #self.my_lovely_turtle.color("green")

    def do_stuff(self):
        for color in ["red", "yellow", "green"]:
            self.my_lovely_turtle.color(color)
            self.my_lovely_turtle.right(120)

    def press(self):
        self.do_stuff()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
