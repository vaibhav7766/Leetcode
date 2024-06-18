// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#include <vector>

class Solution
{
public:
    int findMin(std::vector<int> &nums)
    {
        int left = 0, right = nums.size() - 1;
        if (nums[left] <= nums[right])
        {
            return nums[left];
        }
        while (left < right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[right])
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return nums[left];
    }
};