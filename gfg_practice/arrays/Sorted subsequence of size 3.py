
# only useful if you dont want actual numbers , only true or false
def find3number(self,A, n):
        l=m=(10**6)+1
        result=[]
        for val in A:
            if l>=val:
                l=val
            elif m>=val:
                m=val
            else:
                return True
        return False

# find better solution....