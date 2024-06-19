// https://leetcode.com/problems/sqrtx/

class Solution
{
public:
    long long int mySqrt(long long int x)
    {
        if (x == 0 || x == 1)
        {
            return x;
        }
        long long int left = 1, right = x;
        while (left <= right)
        {
            long long int mid = (left + right) / 2;
            if (mid * mid == x)
            {
                return mid;
            }
            else if (mid * mid < x)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        return right;
    }
};