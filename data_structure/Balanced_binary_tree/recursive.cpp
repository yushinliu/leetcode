/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    struct Error : public std::exception {};   //using standard exception type
    int depth(TreeNode* node){
        if(!node){
            return 0;
        }
        int left = depth(node->left);
        int right = depth(node->right);
        if(abs(left-right)>1){
            throw Error();
        }
        return max(left,right)+1;
    }
    bool isBalanced(TreeNode* root) {
        if(!root){
            return true;
        }
        try
        {
            return abs(depth(root->left)-depth(root->right))<=1;
        }catch(Error e)
        {
            return false;
        }
        
    }
};