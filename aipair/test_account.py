from decimal import Decimal

from account import Account


def test_account_methods_are_used():
    # __init__ and validation helpers
    account = Account("A1001", "Alice", 100)
    assert account.acno == "A1001"
    assert account.customer == "Alice"
    assert account.balance == Decimal("100")

    # static methods
    Account._validate_account_number("A1001")
    Account._validate_customer("Alice")
    assert Account._to_decimal("25.50") == Decimal("25.50")

    # class method validation
    Account._validate_amount(50, "opening balance", allow_zero=True)
    Account._validate_amount(10, "deposit amount")

    # instance methods
    assert account.deposit(25.5) == Decimal("125.5")
    assert account.withdraw(30) == Decimal("95.5")
    assert account.getbalance() == Decimal("95.5")


def test_minimum_balance_is_shared_by_accounts():
    first = Account("A2001", "Alice", 100)
    second = Account("A2002", "Bob", 100)
    Account.setminbalance(25)

    assert first.getminbalance() == Decimal("25")
    assert second.getminbalance() == Decimal("25")
    assert first.withdraw(75) == Decimal("25")

    try:
        second.withdraw(76)
        assert False, "withdrawal below minimum balance should raise ValueError"
    except ValueError:
        pass

    Account.setminbalance(0)


def test_account_validators_reject_invalid_values():
    try:
        Account("", "Alice")
        assert False, "empty account number should raise ValueError"
    except ValueError:
        pass

    try:
        Account("A1002", "")
        assert False, "empty customer should raise ValueError"
    except ValueError:
        pass

    try:
        Account("A1003", "Alice", -5)
        assert False, "negative balance should raise ValueError"
    except ValueError:
        pass

    try:
        Account("A1004", "Alice").withdraw(1)
        assert False, "withdrawal above balance should raise ValueError"
    except ValueError:
        pass
