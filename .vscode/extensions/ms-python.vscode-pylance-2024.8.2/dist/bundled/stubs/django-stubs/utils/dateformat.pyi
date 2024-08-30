from datetime import date, datetime
from typing import Any

from django.utils.timezone import FixedOffset

re_formatchars: Any
re_escaped: Any

class Formatter:
    def format(self, formatstr: str) -> str: ...

class TimeFormat(Formatter):
    data: datetime | str = ...
    timezone: FixedOffset | None = ...
    def __init__(self, obj: datetime | str) -> None: ...
    def a(self) -> str: ...
    def A(self) -> str: ...
    def B(self) -> None: ...
    def e(self) -> str: ...
    def f(self) -> int | str: ...
    def g(self) -> int: ...
    def G(self) -> int: ...
    def h(self) -> str: ...
    def H(self) -> str: ...
    def i(self) -> str: ...
    def O(self) -> str: ...  # noqa:E741,E743
    def P(self) -> str: ...
    def s(self) -> str: ...
    def T(self) -> str: ...
    def u(self) -> str: ...
    def Z(self) -> int | str: ...

class DateFormat(TimeFormat):
    data: datetime | str
    timezone: FixedOffset | None
    year_days: Any = ...
    def b(self) -> Any: ...
    def c(self) -> str: ...
    def d(self) -> str: ...
    def D(self) -> Any: ...
    def E(self) -> Any: ...
    def F(self) -> Any: ...
    def I(self) -> str: ...  # noqa:E741,E743
    def j(self) -> int: ...
    def l(self) -> Any: ...  # noqa:E741,E743
    def L(self) -> bool: ...
    def m(self) -> str: ...
    def M(self) -> str: ...
    def n(self) -> int: ...
    def N(self) -> Any: ...
    def o(self) -> int: ...
    def r(self) -> str: ...
    def S(self) -> str: ...
    def t(self) -> str: ...
    def U(self) -> int: ...
    def w(self) -> int: ...
    def W(self) -> int: ...
    def y(self) -> str: ...
    def Y(self) -> int: ...
    def z(self) -> int: ...

def format(value: datetime | str | date, format_string: str) -> str: ...
def time_format(value: datetime | str, format_string: str) -> str: ...
