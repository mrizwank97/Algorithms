def BinarySearch(A,lo,hi,x):
    while(lo <= hi):
        mid = int((lo+hi)/2)
        if(x == A[mid]):
            return True
        if(A[mid] < x):
            lo = mid + 1
        else:
            hi = mid - 1
    return False


A = [i * i for i in range(1000) if i % 2 == 0]
n = len(A) - 1
print(BinarySearch(A,0,n,16))
