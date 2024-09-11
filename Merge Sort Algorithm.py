def mergesort_algo(array):    
    if len(array) > 1:        
        mid = len(array) // 2       
        left = array[:mid]
        right = array[mid:]        
        mergesort_algo(left)
        mergesort_algo(right)
        i = 0  
        j = 0  
        r = 0  

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[r] = left[i]  
                i += 1
            else:
                array[r] = right[j]  
                j += 1
            r += 1  

        while i < len(left):
            array[r] = left[i]
            i += 1
            r += 1

        while j < len(right):
            array[r] = right[j]
            j += 1
            r += 1

def print_array(array):
    for element in array:
        print(element, end=" ")
    print()

if __name__ == "__main__":
    array = [45, 17, 34, 1, 5, 90, 81]
    print("The Original array is:")
    print_array(array)

    mergesort_algo(array)

    print("The Sorted array is:")
    print_array(array)
