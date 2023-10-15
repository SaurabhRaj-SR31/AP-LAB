
cache = {}


def calculate_square(n):
    if n in cache:
        print(f"Fetching result from cache for {n}")
        return cache[n]
    else:
        result = n * n
        cache[n] = result
        print(f"Calculating and caching result for {n}")
        return result


n = int(input("enter the number: "))
print(calculate_square(n))
print(calculate_square(n))
