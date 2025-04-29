class TaskDomainException(Exception):
    """Generic Domain Exception."""


class TaskTitleTooShortException(TaskDomainException):
    """When title is too short."""


class TaskNotFoundException(TaskDomainException):
    """When task is not found."""
