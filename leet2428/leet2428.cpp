// https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

#include <vector>
using namespace std;

class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int max_sum = INT_MIN;
        for(int i = 1; i < m - 1; i++){
            for(int j = 1; j < n - 1; j++){
                int current_sum = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] +
                                  grid[i][j] +
                                  grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1];
                max_sum = max(max_sum, current_sum);
            }
        }
        return max_sum;
    }
};