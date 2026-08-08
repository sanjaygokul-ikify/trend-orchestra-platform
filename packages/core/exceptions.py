class CoreException(Exception):
    pass

class InvalidMessageError(CoreException):
    pass

class AgentNotFoundError(CoreException):
    pass