def linearsearch(a,k):
    for i in range(len(a)):
        if a[i] == k:
            return i

def recursive(a,k,i):
    while i < len(a):
        if a[i] == k:
            return i
        else:
           return recursive(a,k,i+1)
        
a = [1,2,3]
print(linearsearch(a,3))
print(recursive(a,4,0))

