class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0;
        int length = nums.size();
        for(int i =1;i<length;i++){
            if(nums[i] == nums[i-1]){count++;}
            else{
                nums[i-count]=nums[i];
            }
    }
        return length-count;
    }
};


//run time:29ms
