
def quicksort(array):
    # 기본단계 : 원소의 개수가 0이나 1이면 이미 정렬되어있는 상태
    if len(array) < 2:
        return array
    else:
        # 재귀 단계
        pivot = array[0]
        # 기준원소(pivot) 보다 작거나 같은 원소로 이루어진 하위배열
        less = [i for i in array[1:] if i <= pivot]
        # 기준원소(pivot) 보다 큰 원소로 이루어진 하위배열
        greater = [i for i in array[1:] if i > pivot]

        # 재귀 호출 후 합치기
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    print(quicksort([1,3,4,2,56,4,76,3,5,7,4,2,1]))