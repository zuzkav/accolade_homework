def solution(array):
    array = sorted(array)
    if array[-1] <= 0:
        return 1

    for i in range(len(array) - 1):
        if array[i] <= 0:
            continue
        if array[i + 1] > array[i] + 1:
            return array[i] + 1

    return array[-1] + 1
