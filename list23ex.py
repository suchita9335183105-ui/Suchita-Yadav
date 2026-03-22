runs = [45, 60, 10, 80, 55, 90]
total = 0
highest = 0
count =0
for r in runs:
    total = total+r
    if r>highest:
        highest=r
    if r>50:
       count+=1
print("count score=",count)
print("total run=",total)
print("higest score=",highest)