// https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01

#include <vector>

class Solution
{
public:
    bool threeConsecutiveOdds(std::vector<int> &arr)
    {
        int count = 0;
        bool flag = false;
        for (int i = 0; i < arr.size(); i++)
        {
            if (arr[i] % 2 != 0)
            {
                count++;
            }
            else
            {
                count = 0;
            }
            if (count == 3)
            {
                flag = true;
                break;
            }
        }
        return flag;
    }
};