#s = "anagram";t = "nagaram"
s = "car";t = "care"

## method - 1

def isAnagram(s: str, t: str) -> bool:
    return(sorted(s) == sorted(t))
print(isAnagram( s, t))

## method - 2
def isAnagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return(False)
        else:
            return (True)
    else:
        return(False)
    
print(isAnagram(s,t))

## 