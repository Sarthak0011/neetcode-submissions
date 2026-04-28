class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int i = 0; 
        int j = n - 1;

        int max = 0;
        while(i < j) {
            int height = Math.min(heights[i], heights[j]);
            int width = j - i;
            max = Math.max(max, height*width);
            if(heights[i] < heights[j]) i++;
            else j--;
        }
        return max;
    }
}
