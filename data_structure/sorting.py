#so many swap rather than selection_sort
def buble_sort():
    data = [9,7,5,4,7,3,2,1]
    first_loop = True
    arr_length = len(data) - 1
    while (first_loop):
        first_loop = False
        for i in range(arr_length):
            if data[i] > data[i+1]:
                temp =  data[i+1]
                data[i+1] = data[i]
                data[i] = temp
                first_loop = True
        arr_length = arr_length - 1
    print(data)

#
def selection_sort():
    data = [9,7,5,4,7,3,2,1]
    for i in range(len(data)):
        j = i+1
        lowestNumberIndex = i
        while (j < len(data)):
            if data[j] < data[lowestNumberIndex]:
                lowestNumberIndex = j
            j+=1
        if lowestNumberIndex != i:
            temp = data[i]
            data[i] = data[lowestNumberIndex]
            data[lowestNumberIndex] = temp
    print(data)
            
if __name__=="__main__":
    print("start buble sort")
    buble_sort()
    selection_sort()
    