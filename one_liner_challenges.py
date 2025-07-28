word_lengths = list(map(len, "This is a one-liner task".split()))
uppercased = list(map(str.upper, ['hello', 'world']))
flat = [item for sublist in [[1, 2], [3, 4], [5]] for item in sublist]


lists = [[1, 2], [3, 4], [5]]
l=[]
for i in lists:
    for j in i:
        (l.append(j))
print(l)

