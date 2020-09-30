if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l=list(student_marks[query_name])
    num=len(l)
    s=sum(l)
    ss=(s/num)
    avg="{:.2f}".format(ss)
    print(avg)
