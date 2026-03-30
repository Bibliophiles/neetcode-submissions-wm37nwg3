class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>prevMap;
        for(int i = 0; i < nums.size(); i++){ //Run through the array
            int diff = target - nums[i];  //find the difference between the target and the number in the array
            if(prevMap.find(diff) != prevMap.end()){ //if the difference is already in the map, or it's found in the map
                return {prevMap[diff], i}; // return it's value from the key[diff] and the index of the other number you chose from the integer array
            } //the i is the index of the other number is this case
            prevMap.insert({nums[i], i}); //if it's not in the map, insert the current number and it's index into the map and rerun the loop
        } // the i here is the index of the number itself, so the number and it's index
        return {};
    }
};
