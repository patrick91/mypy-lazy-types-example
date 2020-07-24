from typing import TYPE_CHECKING
from typing_extensions import Annotated

if TYPE_CHECKING:
    from .type_a import TypeA


class TypeB:
    def type_a(self) -> Annotated["TypeA", "app.type_a"]:
        from .type_a import TypeA
        return TypeA()
