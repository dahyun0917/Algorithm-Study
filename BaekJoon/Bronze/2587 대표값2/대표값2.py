#BaekJoon 2587 대표값2
nlist = [int(input()) for _ in range(5)]
print(int(sum(nlist)/5))
print(sorted(nlist)[2])
