import random

subject = [1,2,3,4,5,6]
#1 - Math
#2 - English
#3 - Kiswahili
#4 - Science
#5 - Socail Studies
#6 - Religious Education

def day():
    day_attempt = 0
    final = []
    while len(final) != 6:
        guess = random.choice(subject)
        day_attempt += 1
        if guess not in final:
            final.append(guess)
    day_table = []
    for item in range(0,6):
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
    

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    
def week():    
    attempts=[]
    week_table = []

    for i in range(0,5):
        table,attempt = day()
        table.insert(0,weekdays[i])
        week_table.append(table)
        attempts.append(attempt)
    return attempts,week_table

days_attempt,week_timetable = week()
print(week_timetable)