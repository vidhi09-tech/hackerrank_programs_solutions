final=list()
for i in range(int(input())):
    lst=[]
    name = input()
    score = float(input())
    lst.append(name)
    lst.append(score)
    final.append(lst)
    
    
k=list()
for i in range(len(final)):
    k.append(final[i][1])
    
x=min(k)
k1=[]
for i in range(len(k)):
    if x!=k[i]:
        k1.append(k[i])

y=min(k1)
student=[]
for i in range(len(final)):
    if y==final[i][1]:
        student.append(final[i][0])
student.sort()
for i in range(len(student)):
    print (student[i])
