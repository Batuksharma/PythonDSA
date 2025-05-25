class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the value and its index
        num_to_index = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Add the current number and its index to the dictionary
            num_to_index[num] = i

