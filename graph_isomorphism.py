import itertools
import numpy as np
import timeit

# Обычный брутфорс; перебираю все возможные перестановки вершин, пока не будет найдено необходимое преобразование.
# Поэтому сложность алгоритма – факториальная (O(n!)), где n = |V| для неориентированного невзвешенного графа G(V,E).


def get_vertices_degrees(adj_matrix: np.ndarray) -> list[np.ndarray | int]:
    return sorted([np.sum(vertex) for vertex in adj_matrix], reverse=True)


def get_vertices_permutations(adj_matrix: np.ndarray) -> list[np.ndarray]:
    matrix_order: int = len(adj_matrix)
    vertices_combinations = [list(permutation) for permutation
                             in itertools.permutations(range(matrix_order), matrix_order)]

    vertices_permutations = [np.transpose(adj_matrix[combination])[combination]
                             for combination in vertices_combinations]
    return vertices_permutations


def are_isomorphic(adj_first: np.ndarray, adj_second: np.ndarray) -> bool:
    if adj_first.shape == adj_second.shape \
            and get_vertices_degrees(adj_first) == get_vertices_degrees(adj_second):

        for adj_permutation in get_vertices_permutations(adj_first):
            if np.array_equal(adj_permutation, adj_second):
                return True
    return False


def main():
    g_1 = np.asarray([[0, 1, 0, 0, 1],
                      [1, 0, 1, 0, 0],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1],
                      [1, 0, 0, 1, 0]], dtype=np.int8)

    g_2 = np.asarray([[0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 1],
                      [1, 0, 0, 0, 1],
                      [1, 1, 0, 0, 0],
                      [0, 1, 1, 0, 0]], dtype=np.int8)

    print(are_isomorphic(g_1, g_2))
    # around 8e-4 for 5 vertices with garbage collector enabled
    # print(timeit.timeit(lambda: are_isomorphic(g_1, g_2), 'gc.enable()', number=1))


if __name__ == '__main__':
    main()
