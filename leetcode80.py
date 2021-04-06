## 题目链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
## 题目描述：
## 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
## 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


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
    
## 输出：nums= [1, 2, 1, 2, 2, 3]
##      nums= [1, 2, 3, 2, 2, 3]
## 疑问：上面的完整程序在pycharm中得到如上输出，但是在leetcode中得到的结果是[1,2,3],不知道nums中后面的数[2,2,3]怎么删去的呢？
