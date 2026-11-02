import pytest

@pytest.mark.parametrize("days", [1, 2, 3, 4, 5])
def test_overdue(days):
    if days < 2:
        assert days<2 , "no overdue"
    elif days>=2 and days<5:    
        assert days>=2 , "valid case of overdue"
    elif days==5:    
        assert days==5 , "boundary case"
    else:
        assert days>5 , "invalid overdue"
