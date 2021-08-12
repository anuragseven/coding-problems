# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# TC=O(n) , SC=O(n)
def isUnique(string):
    s = set()
    for v in string:
        if v in s:
            return False
        s.add(v)
    return True


# TC=O(n), SC=O(1)
# Assuming string is ASCII
def isUniqueOptimized(string):
    chars = [False] * 128
    for c in string:
        if chars[ord(c)]:
            return False
        chars[ord(c)] = True
    return True


# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# TC=O(nlogn) , sorting algos can take additional space upto O(n)
def checkPermutation(str1, str2):
    sorted1 = ''.join(sorted(str1))
    sorted2 = ''.join(sorted(str2))
    return sorted1 == sorted2


# Assumption : strings are in ascii
# TC=O(n) . SC=O(1)
def checkPermutationOptimized(str1, str2):
    charCount = [0] * 128

    for c in str1:
        charCount[ord(c)] += 1

    for c in str2:
        charCount[ord(c)] -= 1
        if charCount[ord(c)] < 0:
            return False
    return True


# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

# TC=O(n) ,  SC=O(n)
def urlify(string):
    string = string.strip()
    chars = list(string)
    for i in range(len(string)):
        if chars[i] == ' ':
            chars[i] = '%20'

    return ''.join(chars)


# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A
# palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of
# letters. The palindrome does not need to be limited to just dictionary words. EXAMPLE Input: Tact Coa Output: True
# (permutations: "taco cat", "atco eta", etc.)


# a palindrome cant have more than one character with odd count
# TC=O(n) , SC=O(1) if string contains ascii chars
def palindromePermutation(string):
    charCount = {}
    for c in string:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
    onlyOneOddCount = 0
    for char in charCount:
        if charCount[char] % 2 != 0:
            onlyOneOddCount += 1

        if onlyOneOddCount > 1:
            return False
    return True


# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# TC=O(n) , SC=O(1)
def oneAway(string, edited):
    if len(string) == len(edited):
        replaced = False
        for c1, c2 in zip(string, edited):
            if c1 != c2:
                if replaced:
                    return False
                replaced = True
        return True

    if len(string) == len(edited) + 1:
        i = 0
        j = 0
        deleted = False
        while j < len(edited):
            if string[i] != edited[j]:
                i = i + 1
                if deleted:
                    return False
                deleted = True
            else:
                i += 1
                j += 1
        return True

    if len(string) == len(edited) - 1:
        i = 0
        j = 0
        inserted = False
        while i < len(string):
            if string[i] != edited[j]:
                j = j + 1
                if inserted:
                    return False
                inserted = True
            else:
                i += 1
                j += 1
        return True
    return False


# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compressString(string):
    prev = ''
    count = 0
    result = ''
    for char in string:
        if prev != char:
            result = result + prev + str(count) if count > 0 else ''
            prev = char
            count = 1
        else:
            count += 1
    result = result + prev + str(count) if count > 0 else ''
    return result if len(result) < len(string) else string


# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotateMatrix(a):
    pass


# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

def zeroMatrix(matrix):
    rowsZero = []
    columnZero = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rowsZero.append(i)
                columnZero.append(j)

    for i in rowsZero:
        matrix[i] = [0] * len(matrix[i])
    for j in columnZero:
        for i in range(len(matrix)):
            matrix[i][j] = 0


# 1.9 String Rotation:Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").


# we need to check if there's a way to split s1 into x and y such that xy = s1 and yx = s2. Regardless of
# where the division between x and y is, we can see that yx will always be a substring of xyxy.That is, s2 will
# always be a substring of s1s1.
def stringRotation(str1, str2):
    if len(str1) == len(str2):
        s1s1 = str1 + str1
        return str2 in s1s1
    return False



