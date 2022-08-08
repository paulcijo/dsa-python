# T.C. O(2^n) S.C. O(n)
def printSubSequence(idx, arr, subArray =[]):
    if idx == len(arr):
        print(subArray)
        return

    # take the idx element into subArray
    subArray.append(arr[idx])
    printSubSequence(idx + 1, arr, subArray)
    subArray.pop()
    printSubSequence(idx + 1, arr, subArray)


def main():
    arr = [3,1,2]
    printSubSequence(0, arr)

main()