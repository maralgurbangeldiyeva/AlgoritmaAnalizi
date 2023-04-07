#Morris-Pratt algoritması kodu
def bron_kerbosch(graph):
    n = len(graph)
    visited = [False] * n
    r = []
    p = list(range(n))
    x = []
    cliques = []

    def bron_kerbosch_recursive(r, p, x):
        nonlocal cliques

        if not p and not x:
            # Maksimum bağımsız küme bulundu, sonuç listesine ekle
            cliques.append(r)
            return

        u = choose_pivot_vertex(graph, visited, p, x)

        for v in list(p):
            if v not in graph[u]:
                r.append(v)
                new_p = [n for n in graph[v] if n in p]
                new_x = [n for n in graph[v] if n in x]
                visited[v] = True
                bron_kerbosch_recursive(r, new_p, new_x)
                visited[v] = False
                r.remove(v)
                p.remove(v)
                x.append(v)

    def choose_pivot_vertex(graph, visited, p, x):
        # Basit Pivot Seçimi: En az dereceye sahip olmayan ziyaret edilmemiş bir düğümü seç
        for v in p:
            if not visited[v] and any(n in p for n in graph[v]):
                return v

        # Eğer seçilecek düğüm bulunamazsa, x kümesindeki bir düğümü seç
        for v in x:
            if not visited[v] and any(n in p for n in graph[v]):
                return v

        # Eğer p ve x kümeleri de boş ise, grafin ilk düğümünü seç
        for v in range(len(graph)):
            if v in p:
                return v

    bron_kerbosch_recursive(r, p, x)

    return cliques

# Bir graf tanımlama örneği
graph = [
    [1, 2, 3],
    [0, 2],
    [0, 1],
    [0]
]

cliques = bron_kerbosch(graph)
print("Maksimum Bağımsız Kümeler:")
for clique in cliques:
    print(clique)