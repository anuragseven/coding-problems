# Implement strstr 
for i in range(len(s)):
        if s[i]==x[0]:
            if i+len(x)<=len(s):
                if s[i:i+len(x)]==x:
                    return i
            else:
                return -1
    return -1