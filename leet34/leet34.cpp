// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        int n = nums.size();
        int target_index = -1, left = 0, right = n - 1, mid;
        while (left <= right)
        {
            mid = (left + right) / 2;
            if (nums[mid] == target)
            {
                target_index = mid;
                break;
            }
            else if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        if (target_index == -1)
        {
            return {-1, -1};
        }
        int start_index = target_index;
        while (start_index > 0 && nums[start_index] == nums[start_index - 1])
        {
            start_index--;
        }
        int end_index = target_index;
        while (end_index < n - 1 && nums[end_index] == nums[end_index + 1])
        {
            end_index++;
        }
        return {start_index, end_index};
    }
};