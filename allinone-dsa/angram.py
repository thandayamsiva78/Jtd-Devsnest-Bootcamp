"""Anagram Exmples"""
# Word Anagrams:

# Listen → Silent
# Dormitory → Dirty room
# School master → The classroom
# Astronomer → Moon starer
# Phrase Anagrams:

# Eleven plus two → Twelve plus one
# The eyes → They see
# A gentleman → Elegant man
# Funeral → Real fun
"""Sorted ()"""
def is_anagram(s1, s2):
    # Convert to lowercase
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Remove any spaces
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    
    # Sort the strings and compare
    return sorted(s1) == sorted(s2)
s1 = "Astronomer"
s2 = "Moon starer"
print(is_anagram(s1, s2)) 

"""Without use any Built in Functions """
def is_angram(s1 , s2):
    if len(s1) != len(s2):
        return False
    count1 = {}
    for char in s1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
            
    count2 = {}
    for char in s2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    for key in count1:
        if key not in count2 or count1[key] != count2[key]:
            return False

    return True

s1 = "listen"
s2 = "silent"
print(is_angram(s1, s2))




"""Without use any Built in Functions or methods"""
def is_anagram(s1, s2):
    # Convert to lowercase manually
    s1 = ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s1])
    s2 = ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s2])
    
    # Remove spaces manually
    s1 = ''.join([c for c in s1 if c != ' '])
    s2 = ''.join([c for c in s2 if c != ' '])
    
    # If lengths differ, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Manually count character frequencies for s1
    count1 = {}
    for char in s1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    # Manually count character frequencies for s2
    count2 = {}
    for char in s2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    
    # Compare character frequencies
    for key in count1:
        if key not in count2 or count1[key] != count2[key]:
            return False

    return True

s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # Output should be True