def bubble_sort(arr):
    a = len(arr)
    for i in range(a-1):
        for j in range(a-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("Sorted array is:", arr)
shivu=[5,4,3,2,1]
bubble_sort(shivu)
