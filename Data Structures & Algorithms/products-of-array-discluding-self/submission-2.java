class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int[] output = new int[n];
        int[] prefix = new int[n];
        int[] suffix = new int[n];

        prefix[0] = nums[0];
        suffix[n-1] = nums[n-1];

        for(int i = 1; i < n; i++) {
            prefix[i] = nums[i] * prefix[i-1];
            suffix[n-i-1] = nums[n-i-1] * suffix[n-i];
        }

        for(int i = 0; i < n; i++) {
            int pre = (i == 0) ? 1 : prefix[i-1];
            int suf = (i == n-1) ? 1 : suffix[i+1];
            output[i] = pre * suf;
        }
        return output;
    }
}  
