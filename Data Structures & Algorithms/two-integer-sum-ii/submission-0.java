class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int low = 0;
        int high = numbers.length-1;

        int ans[] = {-1, -1};

        while(low < high) {
            int sum = numbers[low] + numbers[high];
            if(sum == target) {
                ans[0] = low+1;
                ans[1] = high+1;
                break;
            }
            if(sum > target) high--;
            else low++;
        }

        return ans;
    }
}
