// https://leetcode.com/problems/trapping-rain-water/description/
#include <vector>
using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        int left = 0, right = height.size() - 1, max_left = height[left], max_right = height[right], area = 0;
        while (left < right)
        {
            if (max_left < max_right)
            {
                left++;
                max_left = max(max_left, height[left]);
                area += max_left - height[left];
            }
            else
            {
                right--;
                max_right = max(max_right, height[right]);
                area += max_right - height[right];
            }
        }
        return area;
    }
};