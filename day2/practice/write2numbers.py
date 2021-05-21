x, y = map(int, input("Write 2 numbers : ").split())
if x < y:
    print(list(range(x , y + 1)))
elif x > y:
    print(list(range(y, x + 1)))
else :
    x, y = map(int, input("Please write '2 different' numbers : ").split())
    if x < y:
        print(list(range(x , y + 1)))
    elif x > y:
        print(list(range(y, x + 1)))
