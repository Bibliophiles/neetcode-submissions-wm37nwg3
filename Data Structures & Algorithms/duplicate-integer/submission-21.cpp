class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //Create an ordered_set to store the distinct elements in the array nums
        //we will compare the sizes of the set and the nums array to check for duplicates
        //If the size of the set is less than that of the nums array, then it did contained duplicates
        //Return true or otherwise

        return unordered_set<int>(nums.begin(), nums.end()).size() < nums.size();
        //return distinctValues.size() < nums.size();

        // we have nums 1, 2 , 3, 3
        // the set will contain 1, 2, 3
        //size of set is 4 - it contains one duplicate
        // size of set is 3
        // we will return true since the size of the set is lesser than the nums array

    }
};
