def binarysearch(a,k,i,l):
    mid = int(i+l/2)
    if a[mid] == k:
        return mid
    elif a[mid] < k:
        return binarysearch(a,k,i+mid,l)
    elif a[mid] > k:
        return binarysearch(a,k,i,l-mid)
a = [1,2,3,4,5,6,7]
print(binarysearch(a,4,0,len(a)))

