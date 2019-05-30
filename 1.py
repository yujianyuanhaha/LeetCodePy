#class Solution(object):
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    """ computation efficiency matters"""
    ans = []
   
    ''' version 1
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i] + nums[j] == target:
                if i not in ans:
                    ans.append(i)
                if j not in ans:
                    ans.append(j)
                if len(ans)==2:
                    return ans
                    break
    '''
    
    
    for i in range(len(nums)):
        try:
            j = nums.index(target-nums[i])
        except ValueError:
            pass
        else:
            if j!= i:
                ans.append(i)
                ans.append(j)
                break
    
    return ans
    
if __name__ == '__main__':
    nums = [1,2,3,4]
    target = 3
    ans = twoSum(nums, target)
    print(ans)
    
    
    '''
    Reflections:
        1. once if for c++ 11, what is the .index() and try ... except ?
        2. TODO, the official EFFICIENT solutions.
        '''