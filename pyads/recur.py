# List of all recursion examples

#1. Print a list
def recur_print(arr):
    if len(arr) < 2:
        print(arr)
        return arr
    else:
        return recur_print([arr[0]]) + recur_print(arr[1:])

# Test it
test_arr = [1,2,3,4,5]
recur_print(test_arr)

# 2. Calculate factorial
print("FACTORIAL")
def fact_recur(n):
    if n == 0:
        return 1
    else:
        return n * fact_recur(n-1)

print(fact_recur(5))

# 3. Calculate fibonacci
print("FIBONACCI")

fib_cache = dict()

def fib_recur(n):
    if n < 2:
        return n
    else:
        if n in fib_cache:
            return fib_cache[n]
        else:
            fib_cache[n] = fib_recur(n-1) + fib_recur(n-2)
            return fib_cache[n]

print(fib_recur(12))

# 4. Reverse a string
print("STRING REVERSE")
def recur_rev(strArr):
    if len(strArr) < 2:
        print(strArr)
        return strArr
    else:
        return strArr[1:] + strArr[0]

print(recur_rev("BINDU"))

# 5. Generate sets
def recur_sets(strArr):
    if not strArr:
        return [strArr]
    rest = recur_sets(strArr[1:])
    return rest + [[strArr[0]] + item for item in rest]

print(recur_sets([1,2,3,4]))

# 6. Iterative sets
def subsets(arr):
    subArr = [[]]
    for item in arr:
        subArr = subArr + [y + [item] for y in subArr]
    return subArr
print(subsets([1,2,3]))