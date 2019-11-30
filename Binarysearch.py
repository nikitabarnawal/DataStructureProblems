def binarySearch(arr,l,h,x):

    if h >= 1:
        print("high",h)
        print("low",l)
        mid = int(l + h/2)
        print("mid",mid)
        if (arr[mid] == x):
            return mid
        elif x < arr[mid]:
             return binarySearch(arr,l,mid-1,x)
        else:
             return binarySearch(arr,mid+1,h,x)



if __name__=='__main__':
    arr = [2,3,4,5,6,7,8]
    l = 0
    h = len(arr)
    x = 4
    print(binarySearch(arr,l,h,x))
    
