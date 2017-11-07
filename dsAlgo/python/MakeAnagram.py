def makeAnagram(str1, str2):
    difference = {}

    for letter in str1:
        if letter not in difference:
            difference[letter] = 0
        difference[letter]+=1

    for letter in str2:
        if letter not in difference:
            difference[letter] = 0
        difference[letter]-=1

    return sum(abs(n) for n in difference.values())


def checkAnagram(str1, str2):
    a = list(str1)
    b = list(str2)

    #sort list
    a.sort()
    b.sort()

    #join list back to String
    a = ''.join(a)
    b = ''.join(b)
    return a == b


x = checkAnagram("avinash", "anshi")

print("Are strings anagrams : %s" %x)

y = makeAnagram("avinash", "anshi")
print("minimum characters should be deleted is : %s"%y)
