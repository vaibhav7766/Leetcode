// https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

#include <string>
using namespace std;

class Solution {
public:
    int gcd(int a, int b){
        while(b){
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    string gcdOfStrings(string str1, string str2) {
        if(str1 + str2 != str2 + str1){
            return "";
        }
        int gcd_length = gcd(str1.length(), str2.length());
        return str1.substr(0, gcd_length);
    }
};
