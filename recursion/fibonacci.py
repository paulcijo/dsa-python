def fibonacci(n, recursive_vals = {}):
    if n == 0 or n == 1:
        return n

    if not recursive_vals.get(n-1):
        recursive_vals[n-1] = fibonacci(n-1)

    if not recursive_vals.get(n-2):
        recursive_vals[n-2] = fibonacci(n-2)
    
    return recursive_vals[n - 1] + recursive_vals[n - 2]

def main():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))

    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(1000))

main()