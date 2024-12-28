a = [0, 1, 2, 3, 4]
b = 5

for i in range(4, 10):
    try:
        a.index(b)
        print('hello')
        continue
    except(ValueError):
        pass
        
    print(i)