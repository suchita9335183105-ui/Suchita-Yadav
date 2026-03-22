marks = [78, 35, 90, 40, 55]
count = 0
for m in marks:
    if m>=40:
        print(m,"pass")
        count+=1
    else:
        print(m,"Fail")
print("total student pass",count)