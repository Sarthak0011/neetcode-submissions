class Solution {
    private String getHashKey(String str) {
        int[] hash = new int[26];
        for(int i = 0; i < str.length(); i++) {

            hash[str.charAt(i) - 'a']++;
        }

        StringBuilder hashKey = new StringBuilder();
        for(int freq : hash) {
            hashKey.append(freq).append("#");
        }

        return hashKey.toString();
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groups = new ArrayList<>();
        Map<String, List<String>> mpp = new HashMap<>();

        for(String str: strs) {
            String hashKey = getHashKey(str);
            
            if(!mpp.containsKey(hashKey)) {
                mpp.put(hashKey, new ArrayList<>());
            }
            mpp.get(hashKey).add(str);
        }

        for(List<String> group: mpp.values()) {
            groups.add(group);
        }

        return groups;
    }
}
