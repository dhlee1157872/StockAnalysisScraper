#this is to sort the stocks for html as the scraping puts the PE values as string

def merge(arr, left, mid, right):
    size1 = mid - left +1
    size2 = right - mid

    L = [None] * size1
    R = [None] * size2

    for i in range(0,size1):
        L[i] = arr[left+i]

    for j in range(0,size2):
        R[j] = arr[mid+j+1]
    
    i = 0
    j = 0
    k = left

    while i < size1 and j < size2:
        if float(L[i]['PE']) <= float(R[j]['PE']):
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    while i <size1:
        arr[k] = L[i]
        i+=1
        k +=1

    while j < size2:
        arr[k] = R[j]
        j+=1
        k +=1
    
def mergeSort(arr,left, right):
    if left < right:

        mid = (left+(right-1))//2

        mergeSort(arr, left ,mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)