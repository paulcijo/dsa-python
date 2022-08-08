def isPallindrome(str, idx):
    left = idx
    right = len(str) - left - 1

    if left >= right:
        return True

    return str[left] == str[right] and isPallindrome(str, idx + 1)

def main():
    str = "malayalam"
    print(isPallindrome(str, 0))

    str = "adam"
    print(isPallindrome(str, 0))

    str = "maddam"
    print(isPallindrome(str, 0))

main()