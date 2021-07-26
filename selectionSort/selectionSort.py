
def findSmallest(arr):
    smallest = arr[0];
    smallest_index = 0;
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectsionSort(arr):
    newArr = [];
    for i in range(len(arr)):
        smallest = findSmallest(arr);
        newArr.append(arr.pop(smallest));
    return newArr;

if __name__ == '__main__':
    print(selectsionSort([5,3,6,2,10]));