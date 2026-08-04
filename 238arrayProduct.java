class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
      
        // First pass: Calculate products of all elements to the left of each index
        // For each position i, store the product of all elements before index i
        int leftProduct = 1;
        for (int i = 0; i < n; i++) {
            result[i] = leftProduct;      // Store product of all elements to the left
            leftProduct *= nums[i];        // Update left product for next iteration
        }
      
        // Second pass: Calculate products of all elements to the right of each index
        // Multiply each position by the product of all elements after index i
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= rightProduct;     // Multiply by product of all elements to the right
            rightProduct *= nums[i];       // Update right product for next iteration
        }
      
        return result;
    }
}