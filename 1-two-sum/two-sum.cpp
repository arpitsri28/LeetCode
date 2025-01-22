class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int diff = target - nums[i];
            if (hashMap.find(diff) != hashMap.end()){
                return {hashMap[diff], i};
            }
            hashMap.insert({nums[i], i});
        }
        return {};
    }
};