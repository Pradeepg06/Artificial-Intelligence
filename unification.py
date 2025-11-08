# Unification in First Order Logic (FOL-Style Output)
# ---------------------------------------------------
# Supports natural expressions like:
# Eats(x, apple)
# Eats(riya, y)

import re

# --- Parser: Converts expression string -> nested tuple ---
def parse(expr):
    expr = expr.strip()
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|\(|\)|,", expr)
    stack = []
    current = []

    for token in tokens:
        if token == '(':
            stack.append(current)
            func_name = current.pop()
            current = [func_name]
        elif token == ')':
            func = tuple(current)
            current = stack.pop()
            current.append(func)
        elif token == ',':
            continue
        else:
            current.append(token)
    if len(current) == 1:
        return current[0]
    return tuple(current)

# --- Convert nested tuple back to FOL-like string ---
def format_fol(expr):
    if isinstance(expr, str):
        return expr
    return f"{expr[0]}({', '.join(format_fol(sub) for sub in expr[1:])})"

# --- Occurs check ---
def occurs_check(var, expr):
    if var == expr:
        return True
    if isinstance(expr, tuple):
        return any(occurs_check(var, sub) for sub in expr)
    return False

# --- Apply substitution ---
def substitute(expr, subst):
    if isinstance(expr, str):
        return subst.get(expr, expr)
    return tuple(substitute(sub, subst) for sub in expr)

# --- Unification algorithm ---
def unify(Y1, Y2, subst=None):
    if subst is None:
        subst = {}

    Y1 = substitute(Y1, subst)
    Y2 = substitute(Y2, subst)

    if Y1 == Y2:
        return subst

    if isinstance(Y1, str):
        if occurs_check(Y1, Y2):
            return "FAILURE"
        subst[Y1] = Y2
        return subst

    if isinstance(Y2, str):
        if occurs_check(Y2, Y1):
            return "FAILURE"
        subst[Y2] = Y1
        return subst

    if not (isinstance(Y1, tuple) and isinstance(Y2, tuple)):
        return "FAILURE"

    if Y1[0] != Y2[0] or len(Y1) != len(Y2):
        return "FAILURE"

    for a, b in zip(Y1[1:], Y2[1:]):
        subst = unify(a, b, subst)
        if subst == "FAILURE":
            return "FAILURE"

    return subst

# --- MAIN PROGRAM ---
print("=== Unification in First Order Logic (FOL-style Output) ===")
print("Example: Eats(x, apple)   and   Eats(riya, y)\n")

expr1 = input("Enter first expression: ")
expr2 = input("Enter second expression: ")

try:
    parsed1 = parse(expr1)
    parsed2 = parse(expr2)
    result = unify(parsed1, parsed2)

    print("\nParsed Expression 1:", format_fol(parsed1))
    print("Parsed Expression 2:", format_fol(parsed2))

    if result == "FAILURE":
        print("\n❌ Unification failed.")
    else:
        print("\n✅ Most General Unifier (MGU):")
        for var, val in result.items():
            print(f"  {var} = {format_fol(val)}")

        # Show unified form
        unified1 = substitute(parsed1, result)
        unified2 = substitute(parsed2, result)
        print("\nUnified Form:", format_fol(unified1))

except Exception as e:
    print("Error:", e)
