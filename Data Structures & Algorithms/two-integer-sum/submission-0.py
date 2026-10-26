class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #compare integer against the others 
        #check if they add target

        length = len(nums)

        for i in range(length):
            for j in range(i+1,length):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]
                


            
            
        