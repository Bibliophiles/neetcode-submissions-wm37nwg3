class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Create a set from the elements in the vector
        unordered_set<int> uniqueElements(nums.begin(), nums.end());

        // If the size of the set is less than the size of the vector,
        // it means there are duplicate elements
        return uniqueElements.size() < nums.size();
    }
};