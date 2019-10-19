#This is where all test are conducted before implementation

from tkinter import *
from timetable import week


days_attempt,week_timetable = week()

def new_values():
    days_attempt,week_timetable = week()
    for idx,item in enumerate(week_timetable):
        #print("\n{}:{}:".format(idx,weekdays[idx]))
        for count,r in enumerate(item):
            values = Entry(root)
            values.insert(END, r)
            values.grid(row=idx, column=count)
            #print(r)


root=Tk()

sizex = 1200
sizey = 400
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))


weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

for idx,item in enumerate(week_timetable):
    #print("\n{}:{}:".format(idx,weekdays[idx]))
    for count,r in enumerate(item):
        values = Entry(root)
        values.insert(END, r)
        values.grid(row=idx, column=count,)
        #print(r)




b = Button(root, text="New Timetable",command =new_values) 
b.grid(row=7,column=0)



root.mainloop()