    def TotalPairs(nums, k):
	    counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        count=0
        if k==0:
            for key,v in counts.items():
                if v>1:
                    count+=1
            return count
    
        for key, v in counts.items():
            if key+k in counts:
                count+=1
        return count