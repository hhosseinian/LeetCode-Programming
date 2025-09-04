#include <vector>

class Solution {
public:
    bool increasingTriplet(std::vector<int>& nums) {
        int n = nums.size();
        if (n < 3) {
            return false; // There are less than 3 elements, so no increasing triplet can exist.
        }

        int first = INT_MAX;  // Initialize with a large value.
        int second = INT_MAX; // Initialize with a large value.

        for (int num : nums) {
            if (num <= first) {
                first = num; // Update the smallest value encountered so far.
            } else if (num <= second) {
                second = num; // Update the second smallest value encountered so far.
            } else {
                return true; // A third element larger than both 'first' and 'second' was found.
            }
        }

        return false; // No increasing triplet was found.
    }
};
