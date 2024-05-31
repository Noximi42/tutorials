class CustomError(Exception):
    """Custom exception for the module.

    Args:
        message (str): Error message to display.

    Attributes:
        message (str): Error message to display.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsError(Exception):
    """Exception raised when attempting to withdraw more funds than available.

    Args:
        balance (float): Current balance.
        amount (float): Attempted withdrawal amount.

    Attributes:
        balance (float): Current balance.
        amount (float): Attempted withdrawal amount.
    """

    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Attempted to withdraw {amount}, but only {balance} is available.")


class BankAccount:
    """A simple bank account class.

    Args:
        initial_balance (float): Initial balance for the account.

    Attributes:
        balance (float): Current balance of the account.
    """

    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def deposit(self, amount: float):
        """Deposits the specified amount into the account.

        Args:
            amount (float): Amount to deposit.

        Returns:
            None
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        """Withdraws the specified amount from the account.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            None

        Raises:
            InsufficientFundsError: If the account balance is insufficient.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

    def get_balance(self) -> float:
        """Returns the current balance of the account.

        Returns:
            float: Current account balance.
        """
        return self.balance
