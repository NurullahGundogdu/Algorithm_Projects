#######################      Part1      #######################

def black_white_boxes(boxes,first_index,last_index):

    if first_index % 2 == 1:
        boxes[first_index],boxes[last_index] = boxes[last_index],boxes[first_index]
    
    if first_index < last_index:
        boxes = black_white_boxes(boxes,first_index + 1, last_index - 1)
    
    return boxes
    
#######################      Part2      #######################


def fakeCoin(coins): 

    temp = 0

    arr1 = []
    arr2 = []

    if len(coins) % 2 == 1:
        size = (int) (len(coins) / 2)

        arr1 = coins[:size]

        arr2 = coins[size + 1:]

        if sum(arr1) == sum(arr2):

            return coins[size]

    else :

        size = (int) (len(coins) / 2)

        arr1 = coins[:size]

        arr2 = coins[size:]


    if sum(arr1) < sum(arr2):

        if len(arr1) == 1:

            return arr1[0]

        temp = fakeCoin(arr1)

    else :

        if len(arr2) == 1:
            return arr2[0]

        temp = fakeCoin(arr2)

    return temp
  


#######################      Part3      #######################


def partition(arr,low,high,num): 
    
    i = ( low-1 )          
    pivot = arr[high]      
  
    for j in range(low , high): 
  
        if   arr[j] < pivot: 
            num += 1
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    num += 1
    return ( i+1 ), num 
  

def quickSort(arr,low,high,num): 

    if low < high: 

        pi, num = partition(arr,low,high,num) 
   
        num = quickSort(arr, low, pi-1,num) 
        num = quickSort(arr, pi+1, high,num) 
  
    return num

def insertionSort(arr,num): 
   
    for i in range(1, len(arr)): 
  
        current = arr[i] 

        position = i-1

        while position >= 0 and current < arr[position] : 
            num += 1    
            arr[position+1] = arr[position] 
            position -= 1

        arr[position+1] = current 

    return num


#######################      Part4      #######################

def quickSelect(arr):

    if len(arr) % 2 == 1:
        return quickSelect_helper(arr, len(arr) // 2)
    else:
        return (quickSelect_helper(arr, len(arr) // 2 - 1) + quickSelect_helper(arr, len(arr) // 2)) // 2



def quickSelect_helper(arr, half_of_size):

    if len(arr) != 0:
      
        pivot = arr[half_of_size]
    
    Left_Side_Of_List = []

    Right_Side_Of_List = []

    for i in arr:
        if i < pivot:
           Left_Side_Of_List.append(i)
   
        elif i > pivot:
           Right_Side_Of_List.append(i)
   
    size_of_left = len(Left_Side_Of_List)

    pivot_num = len(arr) - size_of_left - len(Right_Side_Of_List)

    if half_of_size >= size_of_left and half_of_size < size_of_left + pivot_num:
        return pivot
    elif size_of_left > half_of_size:
        return quickSelect_helper(Left_Side_Of_List, half_of_size)
    else:
        return quickSelect_helper(Right_Side_Of_List, half_of_size - size_of_left - pivot_num)

#######################      Part5      #######################


def Optimal_SubArray(arr, index, subarr, temp, sum_B): 
    
    if index == len(arr): 
        if len(subarr) != 0: 
            if sum(subarr) >= sum_B:  
                if sum(subarr) <= sum(temp) and len(subarr) <= len(temp):
                    temp = subarr
           
    else: 
 
        temp = Optimal_SubArray(arr, index + 1, subarr, temp, sum_B) 
         
        temp = Optimal_SubArray(arr, index + 1, subarr+[arr[index]], temp, sum_B) 
    
    return temp;



#######################      Driver function      #######################


def main():

    #######################      Part1      #######################

    boxes = ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
             "white", "white", "white", "white", "white", "white", "white", "white", "white", "white"] 

    print ("---------------Part1---------------\n")
    
    print ("Input   :   ", boxes, "\n")

    boxes = black_white_boxes(boxes,0,len(boxes)-1) 
   
    print ("Output   :   ", boxes, "\n")


    #######################      Part2      #######################

    print ("---------------Part2---------------\n")

    arr = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1] 

    print ("Input   :   ", arr, "\n")
    
    print ("Fake Coin   :   ", fakeCoin(arr), "\n")


    #######################      Part3      #######################

    print ("---------------Part3---------------\n")

    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr3 = [2, 4, 9, 1, 10, 8, 3, 6, 5, 7]

    arr4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr6 = [2, 4, 9, 1, 10, 8, 3, 6, 5, 7]

    print ("Quick Sort:") 
    print ("Unsorted array  :  ", arr)
    print ("Swap num  :  ",quickSort(arr,0,len(arr)-1,0))
    print ("Sorted array  :  ",arr,"\n")     

    
    print ("Insertion Sort:") 
    print ("Unsorted array  :  ", arr4)  
    print ("Swap num  :  ",insertionSort(arr4,0))
    print ("Sorted array  :  ",arr4,"\n")     


    print ("Quick Sort:") 
    print ("Unsorted array  :  ", arr2)  
    print ("Swap num  :  ",quickSort(arr2,0,len(arr2)-1,0))    
    print ("Sorted array  :  ",arr2,"\n")     


    print ("Insertion Sort:") 
    print ("Unsorted array  :  ", arr5)  
    print ("Swap num  :  ",insertionSort(arr5,0))
    print ("Sorted array  :  ",arr5,"\n")     


    print ("Quick Sort:") 
    print ("Unsorted array  :  ", arr3)
    print ("Swap num  :  ",quickSort(arr,0,len(arr3)-1,0))  
    print ("Sorted array  :  ",arr3,"\n")     

    
    print ("Insertion Sort:") 
    print ("Unsorted array  :  ", arr6)  
    print ("Swap num  :  ",insertionSort(arr6,0))
    print ("Sorted array  :  ",arr6,"\n")     



    #######################      Part4      #######################

    print ("---------------Part4---------------\n")

    arr = [10, 7, 8, 9, 1, 5, 20, 41, 12,11,31,2,21,90] 

    arr2 = [1,2,3,4,5,6,7,8,9,10]

    arr3 = [13,12,11,10,9,8,7,6,5,4,3,2,1,0]

    arr4 =[1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print ("Input   :   ", arr, "\n")

    #print ("Median   :   ", quickSelect(arr, len(arr) // 2), "\n")
    print ("Median   :   ", quickSelect(arr3), "\n")


    #######################      Part5      #######################

    print ("---------------Part5---------------\n")
         
    arr = [2, 4, 7, 5, 22, 11] 
    print ("Input   :   ", arr, "\n")

    sum_B = (int) ((min(arr) + max(arr)) * (len(arr) / 4))

    print ("SUM(B)   :   ", sum_B, "\n")

    print ("Optimal sub-array   :   ", Optimal_SubArray(arr, 0, [], arr, sum_B), "\n")


if __name__ == "__main__":
    main()
