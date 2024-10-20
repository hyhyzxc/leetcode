class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        # operator -> append
        # open bracket -> pop operator -> loop until close bracket -> append result
        def evaluate(stack):
            top = stack[-1]
            bools = []
            while top != "(":
                popped = stack.pop()
                boolean = True if popped == "t" or popped == True else False
                bools.append(boolean)
                top = stack[-1]
            stack.pop()
            op = stack.pop() 
           
            if op == "|":
                b = bools[0]
                for i in range(1, len(bools)):
                    b = b | bools[i]
                return b, stack
            elif op == "&":
                b = bools[0]
                for i in range(1, len(bools)):
                    b = b & bools[i]
                return b, stack
            else:
                return not bools[0], stack


        i = 0 
        while i < len(expression):
            curr = expression[i]
            if curr == "&" or curr == "|" or curr == "!" or curr == "(" or curr == "t" or curr == "f":
                stack.append(curr)
            elif curr == ")":
               
                res, stack = evaluate(stack)
                stack.append(res)
               
            i += 1
       
        return stack[0]