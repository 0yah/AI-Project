import random

subject = [1,2,3,4,5,6]
#1 - Math
#2 - English
#3 - Kiswahili
#4 - Science
#5 - Socail Studies
#6 - Religious Education

#Generate the timetable for one day
def day():
    day_attempt = 0
    final = []
    while len(final) != 6:
        guess = random.choice(subject)
        day_attempt += 1 #Number of tries before the allowed combination
        #Dont allow double lessons inthe timetable
        if guess not in final:
            final.append(guess)

    day_table = []
    for item in range(0,6):
        #Change the subject codes to their string equivalent for displaying
        if(final[item] == 1):
            day_table.append("Mathematics")
        elif(final[item] == 2):
            day_table.append("English")
        elif(final[item] == 3):
            day_table.append("Swahili")
        elif(final[item] == 4):
            day_table.append("Science")
        elif(final[item] == 5):
            day_table.append("Social Studies")
        elif(final[item] == 6):
            day_table.append("Religious Education")
        
        
    return day_table,day_attempt
    
#Days of the week
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

#Schedule to be followed
timeschedule = ["","8:00-9:00","9:00-10:00","10:00-10:30","10:30-11:30","11:30-12:300","12:30-14:00","14:00-15:00","15:00-16:00","Attempts"]

#Appends the timetable for each day to create the timetable for the week
def week():    
    attempts=[]

    week_table = []
    week_table.append(timeschedule)
    for i in range(0,5):
        table,attempt = day()
        
        #Append the day of the week 
        table.insert(0,weekdays[i])
        #Append a break between two lessons
        table.insert(3,"Break")    
        #Append a Lunch session between two lessons 
        table.insert(6,"Lunch")    

        #Append the day's timetable to the week
        week_table.append(table)
        
        #Append the number of tries before the combination was reached
        table.append(attempt)
    return week_table


