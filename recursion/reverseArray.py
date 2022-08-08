def reverse(arr, idx):
    left = idx
    right = len(arr) - idx - 1
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1)


def main():
    arr = [1, 2, 3]
    reverse(arr, 0)
    print(arr)


main()
