class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int maxProfit = 0;
        int minSoFar = prices[0];
        for(int i = 1; i < n; i++) {
            int currProfit = prices[i] - minSoFar;
            maxProfit = Math.max(maxProfit, currProfit);
            if(prices[i] < minSoFar) minSoFar = prices[i];
        }
        return maxProfit;
    }
}
