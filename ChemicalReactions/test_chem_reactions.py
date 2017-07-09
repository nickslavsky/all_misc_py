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


def test_remaining_substrates(reaction):
    assert reaction.remaining_substrates == 2


def test_substrates_decrement(reaction):
    reaction.decrement_remaining_substrates()
    assert reaction.remaining_substrates == 1

if __name__ == '__main__':
    pytest.main()
