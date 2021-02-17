def longSubArr(a,n):
    res = 0 
    for i in range(n): 

        current_count = 0
        while (i < n and a[i] >= 0): 
      
            current_count+=1
            i+=1

        res = max(res, current_count) 
      
    return res


T=int(input())
while T > 0:
    n=int(input())
    a=list(map(int,input().strip().split()))
    print(longSubArr(a,n))
    T -=1