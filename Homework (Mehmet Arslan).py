name= input("please enter your name :")
surname=input("please enter your surname :")
i=0
while i < 3 :
    check_name=input("please enter your name again :")
    check_surname=input("please enter your surname again :")
    if name==check_name and surname==check_surname :
        print("Welcome")
        i=5
    elif name != check_name or surname != check_surname :
            i = i +1
    if i==3 :
        print("Please try again later")
        exit()

courses=[]
for j in range (5):
    courses.append(input("Please enter the course name which you take :"))
    if '' in courses :
        courses.remove('')
def check_count_of_courses(t):
    if len(t)<3:
        return("You failed in class")
    else :
        return("Please choose one of the courses for evaluating letter grade")
print(check_count_of_courses(courses))

chosen_course=input("Please enter the course name :")
print("Please enter the grades of {} course".format(chosen_course))
grades={}
grades["midterm exam"]=int(input("midterm exam :"))
grades["Final"]=int(input("Final :"))
grades["Project"]=int(input("Project :"))
last_grade= grades["midterm exam"]*0.3 + grades["Final"] * 0.5 + grades["Project"] * 0.2
if last_grade > 90 :
    print("You get AA from {} course.".format(chosen_course))
elif last_grade >70 :
    print("You get BB from {} course.".format(chosen_course))
elif last_grade >50 :
    print("You get CC from {} course.".format(chosen_course))
elif last_grade >30 :
    print("You get DD from {} course.".format(chosen_course))
else :
    print("You get FF from {} course,and you FAİLED from this course.".format(chosen_course))
        
