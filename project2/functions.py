def cocktailSort(sorted_list):
    temp_list = sorted_list
    left = 0
    right = len(temp_list) - 1
    while left <= right:
        for i in range(left, right, 1):
            if temp_list[i] > temp_list[i + 1]:
                temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
        right -= 1

        for i in range(right, left, -1):
            if temp_list[i - 1] > temp_list[i]:
                temp_list[i], temp_list[i - 1] = temp_list[i - 1], temp_list[i]
        left += 1
    return temp_list

def checkInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def checkFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False