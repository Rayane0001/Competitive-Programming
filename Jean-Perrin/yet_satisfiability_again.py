import sys, itertools

data=sys.stdin.read().strip().splitlines()[1:]
clauses=[list(map(int, line.split()[:-1])) for line in data]
v=max(abs(lit) for clause in clauses for lit in clause)

for assign in itertools.product([True,False],repeat=v):
    if all(any(assign[abs(lit)-1]== (lit > 0) for lit in clause) for clause in clauses):
        print("satisfiable")
        sys.exit()

print("unsatisfiable")
