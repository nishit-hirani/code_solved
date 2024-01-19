def pairSum(arr, t):
    for x in range(t):
        for y in range(len(arr)-1):
            if((arr[x]+arr[y+1])==n):
                if(arr[x]<=arr[y+1]):
                    print(arr[x],arr[y+1])
    # Write your code here.
    pass

if __name__ == "__main__":
    arr = []
    t = int(input("t: "))
    n = int(input("n: "))
    
    for x in range(t):
        a = int(input("abcd: "))
        arr.append(a)
    
    arr.sort()
    pairSum(arr, t)
