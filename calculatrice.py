class Calculator:

    def __init__(self, expression):
        self.tokens = self.prepForCalculate(expression)

    def prepForCalculate(self, expression):
        tokens = []
        num = ""
        
        for c in expression:
            if c.isdigit() or c == '.':
                num += c
            else:
                if num:
                    tokens.append(float(num) if '.' in num else int(num))
                    num = ""
                if c in "+-*/()":
                    tokens.append(c)
        if num:
            tokens.append(float(num) if '.' in num else int(num))

        tokens = self.add_implicit_multiplication(tokens)
        return tokens
    
    def add_implicit_multiplication(self, tokens):
        new_tokens = []

        for index in range(len(tokens)):
            current = tokens[index]
            new_tokens.append(current)

            if index + 1 < len(tokens):
                next_token = tokens[index + 1]

                if (
                    (isinstance(current, (int, float)) and next_token == "(") or
                    (current == ")" and isinstance(next_token, (int, float))) or
                    (current == ")" and next_token == "(")
                ):
                    new_tokens.append("*")

        return new_tokens


    def calculate(self, tokens=None):
        if tokens is None:
            tokens = self.tokens.copy()
        else:
            tokens = tokens.copy()
        
        tokens = self.parenthesis(tokens)
        
        self.evaluate("*/", tokens)
        self.evaluate("+-", tokens)
        return tokens[0]

    def parenthesis(self, tokens):
        i = 0
        while i < len(tokens):
            elem = tokens[i]
            
            if isinstance(elem, str) and elem == "(":
                depth = 1
                j = i + 1
                while j < len(tokens) and depth > 0:
                    if tokens[j] == "(":
                        depth += 1
                    elif tokens[j] == ")":
                        depth -= 1
                    j += 1
                
                sub_tokens = tokens[i+1:j-1]
                
                result = self.calculate(sub_tokens)
                
                tokens = tokens[:i] + [result] + tokens[j:]
                
                i = 0
            else:
                i += 1
        
        return tokens

    def evaluate(self, ops, tokens):
        i = 0
        while i < len(tokens):
            elem = tokens[i]
            if isinstance(elem, str) and elem in ops:
                a = tokens[i-1]
                b = tokens[i+1]

                if elem == "*":
                    res = a * b
                elif elem == "/":
                    res = a / b
                elif elem == "+":
                    res = a + b
                elif elem == "-":
                    res = a - b
                
                tokens[i-1:i+2] = [res]
                i = 0
            else:
                i += 1
                    