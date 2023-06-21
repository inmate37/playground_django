# Python
import time
import functools
from typing import (
    Any,
    TypeVar,
    Callable,
    cast
)


F = TypeVar('F', bound=Callable[..., Any])


def performance_counter(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        print(
            f'>>> {func.__name__} | {(time.perf_counter()-start):.2f} seconds'
        )
        return result
    return cast(F, wrapper)
