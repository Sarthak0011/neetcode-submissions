class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num : nums) set.add(num);
        int longest = 0;
        for(int num : set) {
            if(!set.contains(num-1)) {
                int currLongest = 1;
                int tempNum = num+1;
                while(set.contains(tempNum)) {
                    currLongest++;
                    tempNum++;
                }
                longest = Math.max(longest, currLongest);
            }
        }

        return longest;
    }
}
