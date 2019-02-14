# Question 82 - Count of triplets

# Given an array of unique integers and a sum value, can you use python to find the number of triplets with a sum smaller than the given value?

# Example:
# Array of integers = {5, 1, 3, 4, 7}
# Value = 12
# Solution: 4 (e.g. the output of your code)
# Explanation: There are 4 triplets that have a sum less than 12: (1, 3, 4), (1, 3, 5), (1, 3, 7), and (1, 4, 5)

# Solution will be provided in python to premium users.

# Upgrade to premium to receive in-depth solutions to each problem.


def count_triplets(arr, n):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if (arr[i] + arr[j] + arr[k]) < n:
                    count += 1
                    print(str(arr[i]) + ' ' + str(arr[j]) + ' ' + str(arr[k]))
    return count


if __name__ == "__main__":
    # i dont love this solution its O(n^3)
    a = [5, 1, 3, 4, 7]
    print(count_triplets(a, 12))
    print(count_triplets(a, 9))
