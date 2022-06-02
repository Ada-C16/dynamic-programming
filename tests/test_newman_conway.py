import pytest
from lib.newman_conway import newman_conway


def test_newman_conway_for_base_cases():
    # Arrange
    input = 0

    # Act-Assert
    with pytest.raises(ValueError):
        newman_conway(input)

    # Arrange
    input = 1

    # Act
    answer = newman_conway(input)

    # Assert
    assert answer == "1"

    # Arrange
    input = 2

    # Act
    answer = newman_conway(input)

    # Assert
    assert answer == "1 1"


def test_newman_conway_for_13():
    # Arrange
    input = 13

    # Act
    answer = newman_conway(input)

    # Assert
    assert answer == "1 1 2 2 3 4 4 4 5 6 7 7 8"


def test_newman_conway_for_20():
    # Arrange
    input = 20

    # Act
    answer = newman_conway(input)

    # Assert
    assert answer == "1 1 2 2 3 4 4 4 5 6 7 7 8 8 8 8 9 10 11 12"
