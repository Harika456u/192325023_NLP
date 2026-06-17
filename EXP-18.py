# Simple First-Order Predicate Calculus (FOPC) Parser

def parse_fopc(expression):
    if "(" in expression and ")" in expression:
        predicate = expression[:expression.index("(")]
        arguments = expression[expression.index("(")+1:expression.index(")")]
        args = arguments.split(",")

        print("Predicate :", predicate)
        print("Arguments :", args)
    else:
        print("Invalid FOPC Expression")

# Example expressions
expressions = [
    "Likes(John,Mary)",
    "Student(Alice)",
    "Loves(Ram,Sita)"
]

for exp in expressions:
    print("\nExpression:", exp)
    parse_fopc(exp)
