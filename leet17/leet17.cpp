// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<string> splitString(const string &str)
    {
        vector<string> result;
        for (char c : str)
        {
            result.push_back(string(1, c));
        }
        return result;
    }

    vector<string> letterCombinations(string digits)
    {
        unordered_map<char, string> phoneMap = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};

        if (digits.empty())
        {
            return {};
        }

        if (digits.size() == 1)
        {
            return splitString(phoneMap[digits[0]]);
        }

        vector<string> previousCombinations = letterCombinations(digits.substr(0, digits.size() - 1));
        string currentLetters = phoneMap[digits.back()];

        vector<string> result;
        for (const string &combo : previousCombinations)
        {
            for (char letter : currentLetters)
            {
                result.push_back(combo + letter);
            }
        }
        return result;
    }
};