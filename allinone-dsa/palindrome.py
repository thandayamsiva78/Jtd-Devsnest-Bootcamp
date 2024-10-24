"""Palindrome or not"""
def is_palindrome(arr):
    if not arr:
        return True
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True
# Example usage:
arr1 = [1, 2, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5]

print(is_palindrome(arr1))  # True
print(is_palindrome(arr2))  # False


def palindrome(string):
    s = string.lower()
    return s == s[::-1]
string = "123454321"
print(palindrome(string))



