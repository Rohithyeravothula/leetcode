from collections import deque
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def is_operator(a):
        	operators = set(["+", "-", "/", "*"])
        	if a in operators:
        		return True
        	return False

        # def is_operand(a):
        # 	return not is_operator(a)

        def operation(o1, o2, o):
        	if o == "+":
        		return str(int(o1) + int(o2))
        	elif o == "-":
        		return str(int(o1) - int(o2))
        	elif o == "*":
        		return str(int(o1) * int(o2))
        	elif o == "/":
        		return str(int(int(o1)/int(o2)))
        
        stack = []
        if len(tokens) == 0:
        	return 0
        tokens_queue = deque(tokens)
        while len(tokens_queue) != 0:
        	cur = tokens_queue.popleft()
        	if is_operator(cur):
        		o2 = stack.pop()
        		o1 = stack.pop()
        		stack.append(operation(o1, o2, cur))
        	else:
        		stack.append(cur)
        return int(stack[0])

tksn = []
s=Solution()
print(s.evalRPN(tksn))

