# print all subsequences of a list that add up to a number
# modified to print only 1 subSequence


def subSum(arr, targetSum, idx=0, subSeqArr=[], currentSum=0):

    if currentSum == targetSum:
        print(subSeqArr)
        return True

    if idx >= len(arr):
        return False

    subSeqArr.append(arr[idx])
    picked = subSum(
        arr,
        targetSum,
        idx=idx + 1,
        subSeqArr=subSeqArr,
        currentSum=currentSum + arr[idx],
    )

    if picked:
        return picked

    subSeqArr.pop()
    return subSum(
        arr, targetSum, idx=idx + 1, subSeqArr=subSeqArr, currentSum=currentSum
    )


def numSubSum(arr, targetSum, idx=0, subSeqArr=[], currentSum=0):

    if currentSum == targetSum:
        return 1

    if idx >= len(arr):
        return 0

    total = 0
    subSeqArr.append(arr[idx])
    total += numSubSum(
        arr,
        targetSum,
        idx=idx + 1,
        subSeqArr=subSeqArr,
        currentSum=currentSum + arr[idx],
    )

    subSeqArr.pop()
    return total + numSubSum(
        arr, targetSum, idx=idx + 1, subSeqArr=subSeqArr, currentSum=currentSum
    )


def main():
    arr = [1, 2, 1]
    targetSum = 2

    print(numSubSum(arr, targetSum))


main()
