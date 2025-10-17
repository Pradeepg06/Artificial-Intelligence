import itertools
import pandas as pd

# --- Function to evaluate a logical expression ---
def evaluate(expr, model):
    local_dict = {symbol: model[symbol] for symbol in model}
    try:
        return eval(expr, {}, local_dict)
    except Exception as e:
        print(f"Error evaluating '{expr}' with {model}: {e}")
        return False

# --- Function for Truth Table Entailment ---
def truth_table_entailment(kb, query, symbols):
    rows = []
    entails = True

    # Generate combinations: from all False → all True
    for values in itertools.product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        kb_values = [evaluate(stmt, model) for stmt in kb]
        kb_true = all(kb_values)
        query_val = evaluate(query, model)

        row = {sym: model[sym] for sym in symbols}
        for i, stmt in enumerate(kb):
            row[f"KB{i+1}"] = kb_values[i]
        row["KB True?"] = kb_true
        row["Query"] = query_val
        rows.append(row)

        if kb_true and not query_val:
            entails = False

    df = pd.DataFrame(rows)
    return entails, df

# --- User Input ---
print("=== Propositional Logic Entailment Checker ===")
symbols = input("Enter symbols (separated by spaces): ").split()

n = int(input("Enter number of KB statements: "))
kb = []
print("Enter KB statements (use 'not', 'and', 'or', parentheses):")
for i in range(n):
    kb.append(input(f"KB{i+1}: "))

query = input("Enter the query statement: ")

# --- Run Entailment Check ---
entails, truth_table = truth_table_entailment(kb, query, symbols)

# Sort truth table from False False False → True True True
truth_table = truth_table.sort_values(by=symbols, ascending=True, ignore_index=True)

# --- Output ---
print("\nKnowledge Base:")
for i, s in enumerate(kb, 1):
    print(f"  {i}. {s}")

print("\nQuery:", query)
print("\n--- Truth Table ---")
print(truth_table.to_string(index=False))

print("\nResult:")
print("✅ The query IS ENTAILED by the Knowledge Base."
      if entails else "❌ The query is NOT entailed by the Knowledge Base.")
