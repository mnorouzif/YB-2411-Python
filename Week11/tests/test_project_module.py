import pytest

import project_module

def test_something(my_data):
    assert my_data == 41

@pytest.mark.parametrize("values,expected_results",[
    (
    [1,2,3,4,5,6],
    [3,4 ],
    ),
    (
    [-1,-2,-3,-4,-5,-6],
    [-3.0, -4],
    ),
])
def test_rolling_average(values,expected_results):

    result = project_module.rolling_average(values, 5)
    assert result == expected_results