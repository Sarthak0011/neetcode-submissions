class Pair {
    int temperature;
    int index;
    Pair(int temperature, int index) {
        this.temperature = temperature;
        this.index = index;
    }
}
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<Pair> stack = new Stack<>();
        int[] res = new int[n];
        stack.push(new Pair(temperatures[0], 0));

        for(int i = 1; i < n; i++) {
            while(!stack.isEmpty() && temperatures[i] > stack.peek().temperature) {
                res[stack.peek().index] = i - stack.peek().index;
                stack.pop();
            }
            stack.push(new Pair(temperatures[i], i));
        }

        return res;
    }
}