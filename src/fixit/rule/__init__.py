from __future__ import annotations
from abc import ABC, abstractmethod

from typing import (
    ClassVar,
    Dict,
    Callable,
    Collection,
    Iterable,
    List,
    Optional,
    Set,
    TypeVar,
    Type,
    Generic,
)
from collections import defaultdict

from fixit.types import LintViolation, FileContent


Timings = Dict[str, int]
TimingsHook = Callable[[Timings], None]


class LintRule:
    TAGS: Set[str] = set()
    _violations: List[LintViolation] = []
    _runner: ClassVar[Type[LintRunner]]


SomeRule = TypeVar("SomeRule", bound=LintRule)


class LintRunner(ABC, Generic[SomeRule]):
    def __init__(self) -> None:
        self.timings: Timings = defaultdict(lambda: 0)

    @abstractmethod
    def collect_violations(
        self,
        source: FileContent,
        rules: Collection[SomeRule],
        timings_hook: Optional[TimingsHook] = None,
    ) -> Iterable[LintViolation]:
        pass


__all__ = ["LintRule", "LintRunner", "Timings", "TimingsHook"]
