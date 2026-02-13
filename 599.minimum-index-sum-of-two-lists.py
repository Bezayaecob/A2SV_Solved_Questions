class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        common_string={}
        for i in range(len(list1)):
           if list1[i] in list2:
              common_string[list1[i]] = i + list2.index(list1[i])
        index= list(common_string.values())
        minium= min(index)
        for k,v in common_string.items():
            if v==minium:
              ans.append(k)
        return ans 
            
        
        
