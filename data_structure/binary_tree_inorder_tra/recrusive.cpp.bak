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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> node;
        inorder(root,node);
        return node;
    }
    void inorder(TreeNode* root,vector<int>& node){
        if(root){
            inorder(root->left,node);
            node.push_back(root -> val);
            inorder(root->right,node);
        }
    }
};

/*
int a = b is setting a's VALUE to b's VALUE
int* a = &b is setting a's VALUE to the ADDRESS of b
int& a = b is setting a's ADDRESS to b's ADDRESS (a is a reference to b)

*/