students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]
max = 0
name=''
for i in students:
    a,b,c,d=i
    if c>max:
        max=c
        name=b
print(name)

newList = [(b,c)for (a,b,c,d) in students]
print(newList)

students[1][3] = 25