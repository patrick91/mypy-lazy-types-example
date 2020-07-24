import importlib

from typing import Any, Callable

from app.type_b import TypeB


def eval_return_type(method: Callable[..., Any]) -> Any:
    type_ = method.__annotations__["return"]
    module, = type_.__metadata__
    ref = type_.__origin__.__forward_arg__
    _module = importlib.import_module(module)
    return getattr(_module, ref)


print(TypeB().type_a())
print(eval_return_type(TypeB.type_a)())