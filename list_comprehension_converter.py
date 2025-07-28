squares = []
for i in range(10):
    squares.append(i**2)

squares_list = [i*i for i in range(10)]

evens = []
for i in range(10):
    if i&1==0:
        evens.append(i)
even_fiter = [i for i in range(10) if i&1==0]

pairs = []
for i in range(4):
    for j in range(3):
        pairs.append((i,j))

pairs_filtered = [(x,y) for x in range(4) for y in range(3)]