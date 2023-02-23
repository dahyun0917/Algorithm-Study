#BackJoon 4375 1
import sys

while True:
    try:
        n=int(sys.stdin.readline())
        count=1
        result=1
        while result%n!=0:
            result=(10*result)+1
            count+=1
        print(count)
    except:
        break
