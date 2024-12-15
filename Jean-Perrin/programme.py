def parse_input():
    # Lire la première ligne
    header = input().split()
    v = int(header[2])  # Nombre de variables
    c = int(header[3])  # Nombre de clauses

    # Lire les clauses
    clauses = []
    for _ in range(c):
        clause = list(map(int, input().split()))
        clause.pop()  # Retirer le dernier élément (0) qui termine chaque clause
        clauses.append(clause)

    return v, clauses

def is_satisfiable(v, clauses):
    # Générer toutes les assignations possibles (True/False) pour les variables
    for bits in range(1 << v):  # 2^v possibilités
        assignment = [(bits >> i) & 1 == 1 for i in range(v)]

        satisfied_all = True
        for clause in clauses:
            satisfied_clause = False
            for literal in clause:
                var_index = abs(literal) - 1
                is_true = assignment[var_index] if literal > 0 else not assignment[var_index]
                if is_true:
                    satisfied_clause = True
                    break
            if not satisfied_clause:
                satisfied_all = False
                break
        if satisfied_all:
            return True
    return False

# Main
v, clauses = parse_input()
if is_satisfiable(v, clauses):
    print("satisfiable")
else:
    print("unsatisfiable")
