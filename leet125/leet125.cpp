// https://leetcode.com/problems/valid-palindrome/description/
#include <string>
using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        string clean_s = "";
        for (int i = 0; i < s.length(); i++)
        {
            if (isalnum(s[i]))
            {
                clean_s += tolower(s[i]);
            }
        }

        int left = 0;
        int right = clean_s.length() - 1;

        while (left < right)
        {
            if (clean_s[left] != clean_s[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
