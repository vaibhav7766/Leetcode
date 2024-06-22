// https://leetcode.com/problems/container-with-most-water/
#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1, max_area = 0, cur_area;
        while(left < right){
            cur_area = min(height[left], height[right]) * (right - left);
            max_area = max(cur_area, max_area);
            if(height[left] < height[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return max_area;
    }
};