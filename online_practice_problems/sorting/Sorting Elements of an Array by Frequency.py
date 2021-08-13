#Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.
def sortByFrequency(arr):
    f={}
    for val in arr:
        if val in f:
            f[val]+=1
        else:
            f[val]=1
    fToNum={}
    for key,value in f.items():
        if value in fToNum:
            fToNum[value].append(key)
        else:
            fToNum[value]=[key]
    
    frequencies=list(fToNum.keys())
    frequencies.sort()
    result=[]
    for i in range(len(frequencies)-1,-1,-1):
        fToNum[frequencies[i]].sort()
        for val in fToNum[frequencies[i]]:
            t=[val]*frequencies[i]
            result.extend(t)
    return result




def driver():
    cases=int(input())
    for i in range(cases):
        _ignore=input()
        array=input()
        array=array.split(' ')
        try:
            array=[int(val) for val in array]
        except:
            print('error')
        result=sortByFrequency(array)
        for val in result:
            print(val,end=' ')
        print()

driver()