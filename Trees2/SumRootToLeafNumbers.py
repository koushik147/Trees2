#Time_Complexity: O(n) 
#Space_Complexity : O(n)
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0 # initializing result with 0
        self.inorderTraversal(root,0) # calling inorder function
        return self.result # returning result
    
    def inorderTraversal(self,root,currSum):
        #base condition
        if root == None:
            return
        
        self.inorderTraversal(root.left,currSum*10+root.val) # calling left side of root and calculating the current sum
        
        if root.left == None and root.right == None:
            self.result += currSum*10+root.val # adding the current value in result
            
        self.inorderTraversal(root.right,currSum*10+root.val) # calling left side of root and calculating the current sum
