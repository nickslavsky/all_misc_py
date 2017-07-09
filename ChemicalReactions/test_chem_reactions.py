import graph_approach_bfs as gr
import pytest


@pytest.fixture
def reaction():
    """Returns a typical reaction for further tests"""
    return gr.Reaction({1, 2}, {3, 4})


def test_substrates_property(reaction):
    assert reaction.substrates == {1, 2}


def test_products_property(reaction):
    assert reaction.products == {3, 4}


def test_remaining_substrates_property(reaction):
    assert reaction.remaining_substrates == 2


def test_decrement_remaining_substrates(reaction):
    reaction.decrement_remaining_substrates()
    assert reaction.remaining_substrates == 1


@pytest.fixture
def graph():
    """Returns a graph built from the lines of text files"""
    lines = ['4+6->1', '2->3+5', '4->6', '6+4->5', '4+2->7']
    reaction_graph = gr.populate_graph(lines)
    return reaction_graph


def test_populate_graph_keys(graph):
    actual_keys = set(graph.keys())
    expected_keys = {'2', '4', '6'}
    assert actual_keys == expected_keys


def test_populate_graph_values(graph):
    assumption1 = len(graph['4']) == 4
    assumption2 = len(graph['6']) == 2
    assumption3 = len(graph['2']) == 2
    assert assumption1 and assumption2 and assumption3


def test_populate_graph_values_content(graph):
    assumption = True
    for substrate in graph.keys():
        for reaction in graph[substrate]:
            if substrate not in reaction.substrates:
                assumption = False
                break
    assert assumption


def test_populate_graph_reaction_references():
    reaction_graph = gr.populate_graph(['4+6->1'])
    assert reaction_graph['4'] == reaction_graph['6']


if __name__ == '__main__':
    pytest.main()
