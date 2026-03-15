class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # number (not str) in the list
        numList = []
        # set operators into a tuple
        operators = ('+', '-', '*', '/')
        
        for token in tokens:
            if token not in operators:
                # push it into numList
                numList.append(int(token))

            else:
                # do the operation
                oper1 = numList.pop()
                oper2 = numList.pop()
                if token == '+':
                    numList.append(oper2+oper1)
                if token == '-':
                    numList.append(oper2-oper1)
                if token == '*':
                    numList.append(oper2*oper1)
                if token == '/':
                    # divide operation might return a float, so convert it to int to keep only the integer part. 
                    numList.append(int(oper2/oper1))
        
        return numList.pop()
