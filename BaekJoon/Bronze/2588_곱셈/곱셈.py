#BackJoon 2588 곱셈
car1 = int(input())
car2 = int(input())

for c in reversed(str(car2)):
    print(car1*int(c))

print(car1*car2)
