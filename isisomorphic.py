
def isIsomorphic(s, t):

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        
        if(s_to_t.get(s[i]) == None and t_to_s.get(t[i]) == None):
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        elif(s_to_t.get(s[i]) != t[i] or t_to_s.get(t[i]) != s[i]):
            return False
        
    print(s_to_t)
    print(t_to_s)

    

    return True

s = "egg"
t = "add"

print(isIsomorphic(s, t))