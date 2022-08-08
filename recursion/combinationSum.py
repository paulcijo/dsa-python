def combSum(arr, target, idx=0, seq=[]):
    if target == 0:
        print(seq)
        return

    if idx >= len(arr):
        return

    if target - arr[idx] >= 0:
        # can pick
        seq.append(arr[idx])
        combSum(arr, target - arr[idx], idx, seq)  # pick the same idx again
        seq.pop()

    # don't pick
    combSum(arr, target, idx + 1, seq)


def main():
    arr = [3, 2, 1]
    target = 7

    combSum(arr, target)


main()
