import sys
from collections import defaultdict, deque


class Reaction():
    def __init__(self, substrates_set, products_set):
        self.__substrates = substrates_set
        self.__products = products_set
        self.__remaining_substrates = len(substrates_set)

    @property
    def substrates(self):
        return self.__substrates

    @property
    def products(self):
        return self.__products

    @property
    def remaining_substrates(self):
        return self.__remaining_substrates

    def decrement_remaining_substrates(self):
        self.__remaining_substrates -= 1


def load_data_from_file(name):
    with open(name) as data:
        chemicals = {chemical for chemical in data.readline().strip().split(' ')}
        graph = populate_graph(data.readlines())
    return chemicals, graph


def load_data_from_stdin():
    chemicals = {chemical for chemical in sys.stdin.readline().strip().split(' ')}
    graph = populate_graph(sys.stdin.readlines())
    return chemicals, graph


def populate_graph(lines):
    graph = defaultdict(set)
    for line in lines:
        substrates, products = map(lambda x: x.split('+'), line.strip().split('->'))
        reaction = Reaction(set(substrates), set(products))
        for substrate in substrates:
            graph[substrate].add(reaction)
    return graph


def get_final_compounds(source_chemicals, reactions_graph):
    answer = source_chemicals
    queue = deque(source_chemicals)
    while queue:
        compound = queue.pop()
        for reaction in reactions_graph[compound]:
            reaction.decrement_remaining_substrates()
            if reaction.remaining_substrates == 0:
                for product in reaction.products:
                    if product not in answer:
                        answer.add(product)
                        queue.appendleft(product)
    return answer


if __name__ == '__main__':
    chem, gr = load_data_from_stdin()
    result = get_final_compounds(chem, gr)
    print(*result, end=' ')
