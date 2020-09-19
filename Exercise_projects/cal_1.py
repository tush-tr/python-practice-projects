from tkinter import *
import calendar
root = Tk()
root.title("My first gui app")
year = 2020
mycal = calendar.calendar(year)
cal_year = Label(root, text = mycal, font = "Consolas 10 bold")
cal_year.pack()
root.mainloop()

