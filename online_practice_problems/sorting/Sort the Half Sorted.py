def sortHalves (self, arr, n):
        L=[]
        R=[]
        
        m=-1
        if len(arr)%2==0:
            m=len(arr)//2
        else:
            m=len(arr)//2
            if arr[m+1]<arr[m]:
                m+=1
        
        for i in range(0,m):
            L.append(arr[i])
        for i in range(m,len(arr)):
            R.append(arr[i])
        L.append(float('inf'))
        R.append(float('inf'))
        
        i=0
        j=0
        for k in range(0,len(arr)):
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1