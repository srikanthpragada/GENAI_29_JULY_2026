from decimal import Decimal, InvalidOperation
from numbers import Number


class Account:
	"""Represent a bank account with validated balance operations."""

	minbalance = Decimal("0")

	def __init__(self, acno, customer, balance=0):
		self._validate_account_number(acno)
		self._validate_customer(customer)
		self._validate_amount(balance, "balance", allow_zero=True)

		self.acno = acno
		self.customer = customer
		self.balance = self._to_decimal(balance)

	@staticmethod
	def _validate_account_number(acno):
		if isinstance(acno, bool) or acno is None:
			raise TypeError("acno must be a non-empty string or positive integer")
		if isinstance(acno, str):
			if not acno.strip():
				raise ValueError("acno cannot be empty")
		elif isinstance(acno, int):
			if acno <= 0:
				raise ValueError("acno must be positive")
		else:
			raise TypeError("acno must be a non-empty string or positive integer")

	@staticmethod
	def _validate_customer(customer):
		if not isinstance(customer, str):
			raise TypeError("customer must be a string")
		if not customer.strip():
			raise ValueError("customer cannot be empty")

	@staticmethod
	def _to_decimal(amount):
		try:
			if isinstance(amount, bool) or not isinstance(amount, (Number, str, Decimal)):
				raise TypeError
			value = Decimal(str(amount))
		except (InvalidOperation, TypeError, ValueError):
			raise TypeError("amount must be a finite number") from None
		if not value.is_finite():
			raise ValueError("amount must be finite")
		return value

	@classmethod
	def _validate_amount(cls, amount, name, allow_zero=False):
		value = cls._to_decimal(amount)
		if value < 0 or (not allow_zero and value == 0):
			qualifier = "non-negative" if allow_zero else "greater than zero"
			raise ValueError(f"{name} must be {qualifier}")

	def deposit(self, amount):
		"""Add a positive amount and return the updated balance."""
		self._validate_amount(amount, "deposit amount")
		self.balance += self._to_decimal(amount)
		return self.balance

	def withdraw(self, amount):
		"""Remove a positive amount while maintaining the minimum balance."""
		self._validate_amount(amount, "withdrawal amount")
		value = self._to_decimal(amount)
		if value > self.balance:
			raise ValueError("withdrawal amount cannot exceed the balance")
		if self.balance - value < type(self).minbalance:
			raise ValueError("withdrawal would fall below the minimum balance")
		self.balance -= value
		return self.balance

	def getbalance(self):
		"""Return the current balance."""
		return self.balance

	@classmethod
	def getminbalance(cls):
		"""Return the minimum balance shared by all accounts."""
		return cls.minbalance

	@classmethod
	def setminbalance(cls, amount):
		"""Set the minimum balance shared by all accounts."""
		cls._validate_amount(amount, "minimum balance", allow_zero=True)
		cls.minbalance = cls._to_decimal(amount)
