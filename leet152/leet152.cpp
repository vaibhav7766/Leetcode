//https://leetcode.com/problems/maximum-product-subarray/description/
#include <vector>
#include <math.h>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int prefix_prod = 1;
        int suffix_prod = 1;
        int ans = nums[0];
        for(int i = 0; i < n; i++) {
            prefix_prod = prefix_prod == 0 ? 1 : prefix_prod;
            suffix_prod = suffix_prod == 0 ? 1 : suffix_prod;

            prefix_prod *= nums[i];
            suffix_prod *= nums[n - 1 - i];

            ans = max(ans, max(prefix_prod, suffix_prod));
        }

        return ans;
    }
};