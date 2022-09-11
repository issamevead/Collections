import os
from typing import Optional


def get_env(key: str) -> Optional[str]:
    """Get the value of an environment variable
    Args:
        key (str): Key of the environment variable
    Returns:
        Union[str, None]: Return the value of the environment
        variable if it exits, otherwise returns None
    """
    if key and isinstance(key, str):
        return os.getenv(key, None)
    return None
