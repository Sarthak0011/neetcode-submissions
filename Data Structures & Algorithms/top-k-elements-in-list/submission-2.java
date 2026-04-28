class Data {
    int num;
    int freq;
    Data(int num, int freq) {
        this.num = num;
        this.freq = freq;
    }
}
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int num: nums) {
            if(freq.containsKey(num)) {
                freq.put(num, freq.get(num)+1);
            }
            else {
                freq.put(num, 1);
            }
        }

        PriorityQueue<Data> minHeap = new PriorityQueue<>((a,b) -> a.freq - b.freq);
        for(Map.Entry<Integer, Integer> entry: freq.entrySet()) {
            if(minHeap.size() < k) {
                minHeap.offer(new Data(entry.getKey(), entry.getValue()));
            }
            else if(entry.getValue() > minHeap.peek().freq) {
                minHeap.poll();
                minHeap.offer(new Data(entry.getKey(), entry.getValue()));
            }
        }

        int[] ans = new int[minHeap.size()];
        int index = 0;
        while(!minHeap.isEmpty()) {
            ans[index] = minHeap.poll().num;
            index++;
        }
        return ans;
    }
}
