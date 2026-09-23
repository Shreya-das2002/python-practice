# # Day-08
# # practice 1
# nums = [2, 7, 11, 13]
# target = 9
# # brute-force solution
# def sum_num(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [nums[i], nums[j]]
#         return
    
# print(sum_num(nums, target))
# # time complexity = o(n2)

# # Hash-map solution

# def two_sum(nums, target):
#     seen = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in seen:
#             return [complement, nums[i]]
#         else:
#             seen[nums[i]] = i
#     return []

# print(two_sum(nums, target))

# # Time Complexity = o(n)

# # problem 2 

# x = [1, 3, 2, 2, 5, 5, 5, 7, 8, 9]

# # Contains Duplicate
# def duplicate_detection(x):
#     new_x = []
#     for i in range(len(x)):
#         for j in range(len(new_x)):
#             if x[i] == new_x[j]:
#                 return True
#         new_x.append(x[i])
#     return False
# print(duplicate_detection(x))

# # Time Complexity = o(n2) 

# first_str = input("Enter a word: ").lower().strip()
# second_str = input("Enter a word: ").lower().strip()
# def first_count(str1):
#     new_str = {}
#     for i in str1:
#         if i in new_str:
#             new_str[i] += 1
#         else:
#             new_str[i] = 1
#     return new_str

# print(first_count(first_str))

# def second_count(str2):
#     new_str = {}
#     for i in str2:
#         if i in new_str:
#             new_str[i] += 1
#         else:
#             new_str[i] = 1
#     return new_str

# print(second_count(second_str))

# def anagrams(str1, str2):
#     if first_count(str1) == second_count(str2):
#         print("This is anagrams")
#     else:
#         print("This is not anagrams")
# anagrams(first_str, second_str)

# # Time complexity = O(n)


# # pattern practice
# # Frequency counting
# num = [1, 2, 3, 4, 5, 5, 6, 6, 3]

# def freq_count(num):
#     new_num = {}
#     for i in range(len(num)):
#         item = num[i]
#         if item in new_num:
#             new_num[item] += 1
#         else:
#             new_num[item] = 1
#     return new_num
# print(freq_count(num))

# # Set Membership
# number = [10, 20, 30]
# def mem_check(num):
#     if num in number:
#         print("True")
#     else:
#         print("False")
# mem_check(30)

# # Contains Duplicate — Set
# num = [1, 2, 2, 3, 4, 5, 5, 6, 6, 3]
# def duplicate(num):
#     seen = set()
#     for item in num:
#         if item in seen:
#             return True
#         seen.add(item)
#     return False
# print(duplicate(num))

# # Day-09

# # problem 1
# # Valid Palindrome
# val = input("Enter a value: ").lower()
# def palindrome(val):
#     left = 0
#     right = len(val) - 1
#     while left < right:
#         if val[left] == val[right]:
#             return True
#         left += 1
#         right -= 1
#     return False
# print(palindrome(val))

# # Problem 2
# # Move Zeroes
# num = [0, 1, 0, 3, 12]
# def move_zero(num):
#     slow = 0
#     for fast in range(len(num)):
#         if num[fast] != 0:
#             num[slow], num[fast] = num[fast], num[slow]
#             slow += 1
# move_zero(num)
# print(num)

# # Problem 3
# # Is Subsequence

# a = "abc"
# b = "ahbgdc"

# def is_subsequence(s, t):
#     i = 0
#     j = 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#     return i == len(s)

# print(is_subsequence(a, b))

# # Day-10

# problem - 1 
# Maximum Average Subarray 

nums = [1, 12, -5, -6, 50, 3]
k = 4
def average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        
        max_sum = max(window_sum, max_sum)
        return max_sum, max_sum/k
    
print(average(nums, k))

# Problem 2
# Max Vowels in a Substring

word = "abciiidef"
k = 3
def max_count(w, k):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in range(k):
        if w[i] in vowels:
            count += 1
    max_count = count
    
    for right in range(k, len(w)):
        if w[right] in vowels:
            count += 1
        if w[right-k] in vowels:
            count -= 1
            
        max_count = max(max_count, count)
    return max_count

print(max_count(word, k))


# problem 3
# Longest Substring Without Repeating Characters

letter = "abcabcbb"
def length_of_long_substr(s):
    left = 0 
    freq = {}
    max_length = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            left += 1
        window_legth = right - left + 1
        max_length = max(max_length, window_legth)
    return max_length
print(length_of_long_substr(letter))

# prefix sum array
numeric = [2, 4, 6, 8]
prefix = [0]
for i in numeric:
    prefix.append(prefix[-1] + i)
print(prefix)

# range sun function
def range_sun(prefix, left, right):
    return prefix[right + 1] - prefix[left]

print(range_sun(prefix, 1, 3))
    
# Pivot index code
numss = [1, 7, 3, 6, 5, 6]
def pivot_index(numss):
    total = sum(numss)
    left_sum = 0
    for i in range(len(numss)):
        right_sum = total - left_sum -numss[i]
        if right_sum == left_sum:
            return  [i, numss[i]]
        left_sum += numss[i]
    return -1
print(pivot_index(numss))