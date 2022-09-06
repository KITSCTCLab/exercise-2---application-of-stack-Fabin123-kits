class Evaluate:

  def __init__(self, size):
 
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
   
      return len(self.stack) == 0


  def pop(self):
  
    if not self.isEmpty():
      self.top -= 1
      return self.stack.pop(-1)
    


  def push(self, operand):
 
    if len(self.stack) < self.size_of_stack:
      self.top += 1
      self.stack.append(operand)
      


  def validate_postfix_expression(self, expression):
   
    operands = [element for element in expression if element.isdigit()]
    operators = [element for element in expression  if element in ["+", "-", "*", "/", "^"]]
    if (len(operands) + len(operators)) == len(expression) and len(operands) == len(operators) + 1:
        return expression[0] not in operators and expression[1] not in operators


  def evaluate_postfix_expression(self, expression):
   
    self.stack = []
    for element in expression:
      if element.isdigit():
        self.push(int(element))
      elif element in ["+", "-", "*", "/", "^"]:
        if element == "+":
          result = self.stack[-2] + self.stack[-1]
        elif element == "-":
          result = self.stack[-2] - self.stack[-1]
        elif element == "*":
          result = self.stack[-2] * self.stack[-1]
        elif element == "/":
          result = self.stack[-2] // self.stack[-1]
        elif element == "^":
          result = self.stack[-2] ** self.stack[-1]
        self.pop()
        self.pop()
        self.push(result)
    return self.pop()



postfix_expression = input()  
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
