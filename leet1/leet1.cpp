// https://leetcode.com/problems/two-sum/
#include <unordered_map>
#include <vector>

class Solution
{
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target)
    {
        std::unordered_map<int, int> hashmap;
        for (int index = 0; index < nums.size(); index++)
        {
            hashmap[nums[index]] = index;
        }
        for (int index = 0; index < nums.size(); index++)
        {
            int aim = target - nums[index];
            if (hashmap.find(aim) != hashmap.end() && hashmap[aim] != index)
            {
                return {index, hashmap[aim]};
            }
        }
        return {};
    }
};