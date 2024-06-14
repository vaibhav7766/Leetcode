#include <string>
#include <unordered_map>
#include <stack>

class Solution {
public:
    bool isValid(std::string s) {
        std::unordered_map<char, char> hashmap = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        std::stack<char> stack;

        for (char i : s) {
            if (hashmap.find(i) == hashmap.end()) {
                stack.push(i);
            } else {
                if (stack.empty() || stack.top() != hashmap[i]) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.empty();
    }
};
