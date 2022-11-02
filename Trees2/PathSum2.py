#Time_Complexity: O(n) 
#Space_Complexity : O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.target = targetSum # creating target element
        self.result = [] # creating resultant array
        self.recur(root,0,[]) # calling recur function
        return self.result # returning result
    
    def recur(self,root,currSum,path):
        #base condition
        if root == None:
            return
        
        currSum = currSum + root.val # calculating current sum
        path.append(root.val) # appending root value in path
        
        self.recur(root.left,currSum,path) # calling left side of root 
        
        if root.left == None and root.right == None:
            if currSum == self.target: # if current sum is equal to target
                temp = path[:] # copying to temp
                self.result.append(temp) # appending temp to resultant array
        
        self.recur(root.right,currSum,path) # calling right side of root
        
        path.pop() # poppping the path
