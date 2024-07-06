// https://leetcode.com/problems/4sum/

#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    void kSum(int k, int start, long long target, vector<int> &nums, vector<int> &quad, vector<vector<int>> &res)
    {
        if (k == 2)
        {
            int left = start, right = nums.size() - 1;
            while (left < right)
            {
                long long sum = (long long)nums[left] + nums[right];
                if (sum == target)
                {
                    res.push_back({quad[0], quad[1], nums[left], nums[right]});
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1])
                        left++;
                    while (left < right && nums[right] == nums[right + 1])
                        right--;
                }
                else if (sum < target)
                {
                    left++;
                }
                else
                {
                    right--;
                }
            }
        }
        else
        {
            for (int i = start; i < nums.size() - k + 1; i++)
            {
                if (i > start && nums[i] == nums[i - 1])
                    continue;
                quad.push_back(nums[i]);
                kSum(k - 1, i + 1, target - nums[i], nums, quad, res);
                quad.pop_back();
            }
        }
    }

    vector<vector<int>> fourSum(vector<int> &nums, int target)
    {
        vector<vector<int>> res;
        if (nums.size() < 4)
            return res;
        vector<int> quad;
        sort(nums.begin(), nums.end());
        kSum(4, 0, target, nums, quad, res);
        return res;
    }
};