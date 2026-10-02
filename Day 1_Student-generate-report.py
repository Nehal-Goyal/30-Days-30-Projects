details_of_students = {1 : { 'Full-Name' : 'Nehal Goyal' , 
                     'Roll-No' : '23ABC2345' ,
                     'Degree' : 'B.Tech' ,
                     'Section' : 'M2' ,
                     'Subject' :  {
                        'EM': {
                        'Name':'Engineering Maths' ,
                        'Marks' : 85
                        },
                        'PY': {
                        'Name':'Python' ,
                        'Marks' : 83
                        },
                        'DSA': {
                        'Name':'Data Structures and Algorithms' ,
                        'Marks' : 88
                        },
                        'SEPM': {
                        'Name':'Software Development' ,
                        'Marks' : 78
                        },
                        'FLAT': {
                        'Name':'Finite Automata and Theory' ,
                        'Marks' : 90
                        },
                     },

}
}
student_no = int(input("Enter the no of the student for the report card(1,2,3,4): "))

student = details_of_students[student_no]

for key , value in student.items():
    if key != 'Subject':
        print(key, ' : ', value)
        
for sub_code , sub_details in details_of_students[student_no]['Subject'].items():
    print(sub_code ,sub_details['Name'], ' : ', sub_details["Marks"])





# print(*details_of_students[student_no].items())
# print(student_details['num'][2])