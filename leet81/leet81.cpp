// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

#include <vector>
using namespace std;

class Solution
{
public:
    bool search(vector<int> &nums, int target)
    {
        int left = 0, right = nums.size() - 1;
        while (left <= right)
        {
            int mid = (right + left) / 2;
            if (nums[mid] == target)
            {
                return true;
            }
            while (left < mid && nums[left] == nums[mid])
            {
                left++;
            }
            while (right > mid && nums[right] == nums[mid])
            {
                right--;
            }
            if (nums[left] <= nums[mid])
            {
                if (nums[left] <= target && target < nums[mid])
                {
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
            }
            else
            {
                if (nums[mid] < target && target <= nums[right])
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }
        }
        return false;
    }
};