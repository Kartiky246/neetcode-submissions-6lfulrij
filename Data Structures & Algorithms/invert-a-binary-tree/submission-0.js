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
     * @return {TreeNode}
     */
    invertTree(root) {
        const swap = (node)=>{
            if(!node) return;
            const left = node.left;
            const right = node.right;
            node.left = right;
            node.right = left;
            swap(node.left);
            swap(node.right);

        }
        swap(root);
        return root;
    }
}
