import pytest
from unittest.mock import patch

from int_addr.int_adder import adder, main


@pytest.mark.parametrize('test_input, expected', [
                        (['1', '1'], 2),
                        (['2', '2'], 4),
                        (['1', '2', '3', '4', '5'], 15), ])
def test_adder(test_input, expected):
    assert adder(test_input) == expected


def test_main(capfd):
    with patch('sys.argv', ['script_name.py', '2', '2']):
        main()
        output = capfd.readouterr().out.strip()
        assert output == '4'
