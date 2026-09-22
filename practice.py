# practice 1
nums = [2, 7, 11, 13]
target = 9
# brute-force solution
def sum_num(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
        return
    
print(sum_num(nums, target))
# time complexity = o(n2)

# Hash-map solution

def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [complement, nums[i]]
        else:
            seen[nums[i]] = i
    return []

print(two_sum(nums, target))

# Time Complexity = o(n)

# problem 2 

x = [1, 3, 2, 2, 5, 5, 5, 7, 8, 9]

# Contains Duplicate
def duplicate_detection(x):
    new_x = []
    for i in range(len(x)):
        for j in range(len(new_x)):
            if x[i] == new_x[j]:
                return True
        new_x.append(x[i])
    return False
print(duplicate_detection(x))

# Time Complexity = o(n2) 

first_str = input("Enter a word: ").lower().strip()
second_str = input("Enter a word: ").lower().strip()
def first_count(str1):
    new_str = {}
    for i in str1:
        if i in new_str:
            new_str[i] += 1
        else:
            new_str[i] = 1
    return new_str

print(first_count(first_str))

def second_count(str2):
    new_str = {}
    for i in str2:
        if i in new_str:
            new_str[i] += 1
        else:
            new_str[i] = 1
    return new_str

print(second_count(second_str))

def anagrams(str1, str2):
    if first_count(str1) == second_count(str2):
        print("This is anagrams")
    else:
        print("This is not anagrams")
anagrams(first_str, second_str)

# Time complexity = O(n)


# pattern practice
# Frequency counting
num = [1, 2, 3, 4, 5, 5, 6, 6, 3]

def freq_count(num):
    new_num = {}
    for i in range(len(num)):
        item = num[i]
        if item in new_num:
            new_num[item] += 1
        else:
            new_num[item] = 1
    return new_num
print(freq_count(num))

# Set Membership
number = [10, 20, 30]
def mem_check(num):
    if num in number:
        print("True")
    else:
        print("False")
mem_check(30)

# Contains Duplicate — Set
num = [1, 2, 2, 3, 4, 5, 5, 6, 6, 3]
def duplicate(num):
    seen = set()
    for item in num:
        if item in seen:
            return True
        seen.add(item)
    return False
print(duplicate(num))