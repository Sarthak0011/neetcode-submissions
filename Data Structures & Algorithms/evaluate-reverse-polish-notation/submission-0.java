class Solution {
    private boolean isOperator(String ch) {
        return ch.equals("+") || ch.equals("-") || ch.equals("*") || ch.equals("/");
    }
    private int operate(int a, int b, String operator) {
        if(operator.equals("+")) return a+b;
        if(operator.equals("-")) return a-b;
        if(operator.equals("*")) return a*b;
        if(operator.equals("/")) return a/b;
        return 0;
    }
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for(int i = 0; i < tokens.length; i++) {
            String ch = tokens[i];
            if(isOperator(ch)) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(operate(b, a, ch));
            }
            else {
                stack.push(Integer.parseInt(ch));
            }
        }

        return stack.peek();
    }
}
