// https://leetcode.com/problems/3sum-closest/description/

#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        sort(nums.begin(), nums.end());
        int left, right, close_sum = nums[0] + nums[1] + nums[2], total_sum;
        int n = nums.size();
        for (int i = 0; i < n - 2; i++)
        {
            left = i + 1;
            right = n - 1;
            while (left < right)
            {
                total_sum = nums[i] + nums[left] + nums[right];
                if (total_sum == target)
                {
                    return total_sum;
                }
                else if (total_sum > target)
                {
                    right--;
                }
                else
                {
                    left++;
                }
                if (abs(total_sum - target) < abs(close_sum - target))
                {
                    close_sum = total_sum;
                }
            }
        }
        return close_sum;
    }
};