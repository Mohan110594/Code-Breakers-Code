#Quick sort
def partition(input,low,high):
    pivot=input[high]
    pindex=low

    for i in range(low,high):
        if input[i]<=pivot:
            input[i],input[pindex]=input[pindex],input[i]
            pindex+=1
    input[high],input[pindex]=input[pindex],input[high]
    # print(input)
    return pindex

def quicksort(input,low,high):
    if low<high:
        p=partition(input,low,high)
        quicksort(input,low,p-1)
        quicksort(input,p+1,high)


if __name__=="__main__":
    input = [90, 70, 50, 20, 80, 5]
    quicksort(input,0,len(input)-1)
    print(input)

#Merge sort

# o(nlogn)
def mergesort(input1):
    if len(input1)>1:
        mid=len(input1)//2
        l=input1[:mid]
        r=input1[mid:]
        mergesort(l)
        mergesort(r)
        print(l,r)
        merge(input1,l,r)
        print("input1 is ",input1)

def merge(input1,l,r):
    low_l=0
    low_r=0
    low_k=0

    while low_l<len(l) and low_r<len(r):
        if l[low_l]<r[low_r]:
            input1[low_k]=l[low_l]
            low_l=low_l+1
        else:
            input1[low_k]=r[low_r]
            low_r=low_r+1
        low_k=low_k+1

    while low_l<len(l):
        input1[low_k]=l[low_l]
        low_l=low_l+1
        low_k=low_k+1

    while low_r<len(r):
        input1[low_k]=r[low_r]
        low_r=low_r+1
        low_k=low_k+1

if __name__=="__main__":
    input1=[90,70,50,20,80,5]
    mergesort(input1)
    print(input1)
    
    
#insertion sort

# o(n2)
def insertion(input1):
    for i in range(1,len(input1)):
        while i>0:
            if input1[i-1]>input1[i]:
                input1[i-1],input1[i]=input1[i],input1[i-1]
            i=i-1


if __name__=="__main__":
    input1=[12, 11, 13, 5, 6]
    insertion(input1)
    print(input1)
    
#selection sort

input=[64,25,12,22,11]

for i in range(len(input)):
    mini=i
    for j in range(i+1,len(input)):
        if input[j]<input[mini]:
            mini=j
    input[i],input[mini]=input[mini],input[i]
    print(input)
    
#Bubble sort

# o(n2),in-place
def bubblesort(input1):
    for j in range(len(input1)):
        for i in range(len(input1)-1):
            if input1[i]>input1[i+1]:
                input1[i],input1[i+1]=input1[i+1],input1[i]

if __name__=="__main__":
    input1=[6,5,80,90,20,40,10]
    bubblesort(input1)
    print(input1)
