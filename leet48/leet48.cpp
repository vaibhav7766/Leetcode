// https://leetcode.com/problems/rotate-image/

#include <vector>
using namespace std;

class Solution
{
public:
    void transpose(vector<vector<int>> &matrix, int n)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                matrix[i][j] = matrix[i][j] ^ matrix[j][i];
                matrix[j][i] = matrix[i][j] ^ matrix[j][i];
                matrix[i][j] = matrix[i][j] ^ matrix[j][i];
            }
        }
    }

    void rotate(vector<vector<int>> &matrix)
    {
        int n = matrix[0].size();
        transpose(matrix, n);
        for (int i = 0; i < n; i++)
        {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};