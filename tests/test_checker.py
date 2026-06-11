import pytest
from src.checker import check_single_proxy

def test_check_single_proxy():
    assert check_single_proxy() == 'Invaliv proxy'
    assert check_single_proxy('123') == 'Invalid proxy'
    assert check_single_proxy('https://1.1.1.1') == 'Invalid proxy'
