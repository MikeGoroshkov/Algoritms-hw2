def heap_sort(arr):
    n = len(arr)

    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # левый = 2 * i + 1
    r = 2 * i + 2  # правый = 2 * i + 2

    # Смотрим, есть ли левый дочерний элемент больший, чем корень
    if l < n and arr[largest] < arr[l]:
        largest = l

    # Смотрим, есть ли правый дочерний элемент больший, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Продолжаем строить поддерево с корнем в largest
        heapify(arr, n, largest)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив: ")
print(arr)