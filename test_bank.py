from bank import bankoper

def test_deposit():
    totalBalance, updatedBalance = bankoper(200000,30000,0)

    assert totalBalance == 230000
    assert updatedBalance == 230000

def test_withdraw():
    totalBalance, updatedBalance = bankoper(100000,4000,10000)

    assert totalBalance == 140000
    assert upadatedBalance == 130000

def test_anymount():
    totalBalance, updatedBalance = bankoper(150000,0,15000)

    assert totalBalance == 150000
    assert upadatedBalance == 135000