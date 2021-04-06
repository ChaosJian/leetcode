class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for i in range(len(nums) ):
            if nums[i] !=nums[s]:
                s += 1
                nums[s] = nums[i]
                print('nums=',nums)
        return s+1 # 已经排序好的长度   后面的数直接忽视

def main():
    input = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    Solution.removeDuplicates(solution,input)


if __name__ == '__main__':
    main()