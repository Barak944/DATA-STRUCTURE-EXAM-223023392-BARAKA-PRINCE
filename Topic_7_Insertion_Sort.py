# Topic 7: Use Insertion Sort to Sort Data Based on Priority with Predefined Input
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

if __name__ == "__main__":
    input_values = [50, 20, 40, 10, 30]
    print("Unsorted data:", input_values)
    sorted_data = insertion_sort(input_values)
    print("Sorted data:", sorted_data)
