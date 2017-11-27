class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def get_value(left, right, operation):
        	if operation == "+":
        		return left + right
        	elif operation == "-":
        		return left - right
        	elif operation == "*":
        		return left * right
        	elif operation == "/":
        		return left / right

        def is_operation(left):
        	if left in ["+", "-", "*", "/"]:
        		return True
        	return False
        	
        def find(lst, operation):
        	left = lst[-1]
        	if is_operation(left):
        		return ""
        	else:
        		right=find(lst[0:-1])
        		return get_value(left, right, operation)