#Program By: Suchita Yadav
#Roll no.73
#List Assingement No:19
 #store the attendence of student in a list(1==present,0=absent)
#example [1,1,0,1,0,1,1]
#write a program to coun total present ,count total absent , print attendence percentage
attendance = [1, 1, 0, 1, 0, 1, 1]
present = attendance.count(1)
absent = attendance.count(0)
percentage = (present / len(attendance)) * 100
print("total Present:",present)
print("Attendence percentage:",percentage, "%")