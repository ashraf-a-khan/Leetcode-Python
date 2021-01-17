s1 = "ab"
s2 = "eidbaooo"

s3 = sorted(s1)
s4 = sorted(s2)

s1Sorted = "".join(s3)
s2Sorted = "".join(s4)

if s1Sorted in s2Sorted:
    print(True)
