class Solution:
    def threeSumClosest(self, num: List[int], target: int) -> int:
        num.sort()
        res=sum(num[:3])
        for i in range(len(num)-2):
            l,r=i+1,len(num)-1
            while l<r:
                Sum=num[i]+num[l]+num[r]
                if Sum==target:
                    return Sum
                
                if abs(Sum-target)<abs(res-target):
                    res=Sum
                
                if Sum<target:
                    l+=1
                elif Sum>target:
                    r-=1
        return res  
