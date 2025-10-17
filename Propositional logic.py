import itertools
import pandas as pd

# --- Helper function to evaluate a logic expression ---
def evaluate(expr, model):
    """Evaluates a propositional logic expression based on the model (truth values)."""
    local_dict = {symbol: model[symbol] for symbol in model}
    return eval(expr, {}, local_dict)

# --- Truth Table Entailment Function ---
def truth_table_entailment(kb, query, symbols):
    """Generates the truth table and checks if KB entails the query."""
    rows = []
    entails = True

    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))

        # Evaluate all KB statements and query
        kb_values = [evaluate(stmt, model) for stmt in kb]
        kb_true = all(kb_values)
        query_val = evaluate(query, model)

        # Add to table
        row = {sym: model[sym] for sym in symbols}
        for i, stmt in enumerate(kb):
            row[f"KB{i+1}"] = kb_values[i]
        row["KB True?"] = kb_true
        row["Query"] = query_val
        rows.append(row)

        # Check entailment condition
        if kb_true and not query_val:
            entails = False

    # Create DataFrame for truth table
    df = pd.DataFrame(rows)
    return entails, df

# --- Example Knowledge Base ---
# KB: (R → W) and (R)
# Query: W
kb = [
    "(not R or W)",   # R → W
    "R"               # R is True
]
query = "W"
symbols = ['R', 'W']

# --- Run Entailment Check ---
entails, truth_table = truth_table_entailment(kb, query, symbols)

# --- Display Results ---
print("\nKnowledge Base:")
for i, s in enumerate(kb, 1):
    print(f"  {i}. {s}")
print("\nQuery:", query)

print("\n--- Truth Table ---")
print(truth_table.to_string(index=False))

print("\nDoes KB entail the query?", "✅ YES" if entails else "❌ NO")
