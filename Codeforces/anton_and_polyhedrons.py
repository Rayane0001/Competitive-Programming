# tags: geometry

# nb of polyhedrons
n = int(input())
polyhedrons = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

faces = sum(polyhedrons[input().strip()] for _ in range(n))

print(faces)