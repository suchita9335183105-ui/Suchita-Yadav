#Program By: Suchita Yadav
#Roll no.73
#List Assingement No:11
 #Take a list like [-5, 3, -2, 8]. create a new list where all negative numbers are converted to positive

nums = [-5, 3, -2, 8]
new_list =[]
for i in nums:
    if i < 0:
        
        new_list.append(-i)
    else:
        new_list.append(i)
print(new_list)