// https://leetcode.com/problems/binary-search/description/
#include <vector>

// class Solution
// {
// public:
//     int search(std::vector<int> &nums, int target)
//     {
//         int left = 0, right = nums.size() - 1;
//         while (left <= right)
//         {
//             int mid = (left + right) / 2;
//             if (nums[mid] == target)
//             {
//                 return mid;
//             }
//             else if (nums[mid] < target)
//             {
//                 left = mid + 1;
//             }
//             else
//             {
//                 right = mid - 1;
//             }
//         }
//         return -1;
//     }
// };

class Solution
{
public:
    int bs(std::vector<int> &nums, int left, int right, int target)
    {
        if (left > right)
        {
            return -1;
        }
        int mid = (left + right) / 2;
        if (nums[mid] == target)
        {
            return mid;
        }
        else if (nums[mid] < target)
        {
            return bs(nums, mid + 1, right, target);
        }
        else
        {
            return bs(nums, left, mid - 1, target);
        }
        return -1;
    }
    int search(std::vector<int> &nums, int target)
    {
        return bs(nums, 0, nums.size() - 1, target);
    }
};