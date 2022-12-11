def partition(num_list, start_index, end_index):

    # midpoint is initial pivot value
    midpoint = start_index + (end_index-start_index)//2
    pivot = num_list[midpoint]

    low = start_index
    high = end_index
    done = False

    while not done:
        # increases low if value is less than pivot ((if it's less than pivot, doesn't need to be moved))
        while num_list[low] < pivot:
            low = low+1

        # decreases high if value is higher than pivot, it doesn't need to be moved
        while pivot < num_list[high]:
            high = high - 1

        if low >= high:  # if low becomes high and high becomes low, this loop is finished
            done = True

        else:  # swappy time
            temp1 = num_list[low]
            temp2 = num_list[high]

            num_list[low] = temp2
            num_list[high] = temp1

            low += 1
            high -= 1

    return high


def quick_sort(num_list, start_index, end_index):
    if (end_index <= start_index):
        return

    high = partition(num_list, start_index, end_index)

    # sorting left of pivot
    quick_sort(num_list, start_index, high)

    # sorting right of pivot
    quick_sort(num_list, high + 1, end_index)


integers = [1, 23, 0, 55, 67, 30, 12, 80, 88, 70]
print("initial list: ", integers)

quick_sort(integers, 0, len(integers)-1)

print("Sorted: ", integers)
