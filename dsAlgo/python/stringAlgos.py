def unique(str):
    if not str:
        return False

    return len(set(str))==len(str)

print(unique("avi"))
print(unique("avinash"))


def permutation(str1, str2):
    if str1 is None or str2 is None:
        return False
    a = sorted(str1)
    b = sorted(str2)

    return a == b

print(permutation("avi","via"))
print(permutation("abcd", "dcak"))

def is_rotation(s1,s2):
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False

    return is_subString(s1,s2+s2)

def is_subString(s1,s2):
    return s1 in s2

print(is_rotation("avi","vi"))
print(is_rotation("avi",""))
print(is_rotation("avi","via"))
print(is_rotation("avi","vib"))
