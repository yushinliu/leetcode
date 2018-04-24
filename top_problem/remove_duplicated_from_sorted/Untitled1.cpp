class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int i =1;
        vector<int>::iterator it;
        while(i < nums.size()){
            if(nums[i] == nums[i-1]){
                for(it=nums.begin();it!=nums.end();it++){
                    nums.erase(nums.begin()+i);
                }
                continue;
                
            }
            else{
                i ++;
            }
        }
        return nums.size();
    }
};