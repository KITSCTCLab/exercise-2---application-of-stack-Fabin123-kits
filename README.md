# Problem
Implement a program to validate and evaluate a postfix expression..

# Input
The input will be a valid or invalid postfix string. The expression consists of only integers and binary operators ("+","-","*","/","^"). There will not be any division by zero operation.</br>
Every integer and operator will be separated by a SPACE. 

The idea is to traverse the given expression from left to right. If the current character of the expression is an operand, push it into the stack; otherwise, if the current character is an operator, pop the top two elements from the stack, evaluate them using the current operator and push the result back into the stack. When all the expression characters are processed, we will be left with only one element in the stack containing the value of a postfix expression.

# Constraints
NA


# Sample Input-0
2 3 1 * + 9 -

# Sample Output-0
-4

# Sample Input-1
1 2 3 + * 8 -

# Sample Output-1
-3

# Sample Input-2
31 4 50 + * 

# Sample Output-2
1674

# Sample Input-3
31 4 50 5 * *

# Sample Output-3
Invalid postfix expression
