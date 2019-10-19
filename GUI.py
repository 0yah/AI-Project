from tkinter import *
from timetable import week

#generate the timetable, populate and arrange the values
def new_values():
    week_timetable = week()
    for idx,item in enumerate(week_timetable):
        #print("\n{}:{}:".format(idx,weekdays[idx]))
        for count,value in enumerate(item):
            #Creates a textfield
            values = Entry(root)
            #Add the values to the Input TextField
            values.insert(END, value)
            #arrange the Input textfield and their values to the grid for display
            values.grid(row=idx, column=count)
            #print(r)


root=Tk()
root.title("Timetable")
sizex = 1200
sizey = 400
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))


new_values()

b = Button(root, text="Generate",command =new_values) 
b.grid(row=7,column=0)

root.mainloop()