count= Counter(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if count[i]>1:
                res.append(i)
        return res