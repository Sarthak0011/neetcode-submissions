class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int max = 0;
        for(int i = 0; i < n-1; i++){
            for(int j = i+1; j < n; j++){
                int height = Math.min(heights[i], heights[j]);
                int width = j - i;
                max = Math.max(max, height*width);
            }
        }
        return max;
    }
}
