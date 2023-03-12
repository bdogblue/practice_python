
def isSubsequence(s, t):

    subNum = 0

    for i in range(len(t)):
        if(subNum > len(s)-1):
            break
        elif(s[subNum] == t[i]):
            subNum += 1
    
    if(subNum == len(s)):
        return True

    return False

s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))