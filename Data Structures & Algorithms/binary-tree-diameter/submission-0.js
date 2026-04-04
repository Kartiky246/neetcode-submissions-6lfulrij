/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
       let ans = 0;
       const dfs = (node) =>{
        if(!node) return 0;
        const leftWidth = dfs(node.left);
        const rightWidth = dfs(node.right);
        ans = Math.max(ans, leftWidth + rightWidth);
        return 1 + Math.max(leftWidth, rightWidth);
       }
       dfs(root);
       return ans;

    }
}
