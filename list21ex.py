marks = [23, 65, 89, 90, 56]
count = 0
highest = marks[0]
lowest = marks[0]
for i in marks:
    print("marks:",i)
    count = count+i
    average = count/len(marks)
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i

print("lowest marks=",lowest)
print("highest marks=", highest)
print("average marks=",average)
print("count marks=",count)
