from functools import wraps
from Exceptions import CustomAccessForbiddenException
def raise_403_if_not_admin(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if (user := kwargs.get('current_user')) and user.role.name != 'Admin':
            CustomAccessForbiddenException()
        return await func(*args, **kwargs)

    return wrapper