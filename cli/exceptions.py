"""Custom exceptions in the BiAlert CLI."""


class ManagerError(Exception):
    """Top-level exception for Manager errors."""


class InvalidConfigError(ManagerError):
    """BiAlert config is not valid."""


class TestFailureError(ManagerError):
    """Exception raised when a BiAlert test fails."""
