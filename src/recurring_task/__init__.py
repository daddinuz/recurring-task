from typing import Any, Callable, Mapping, Optional, Sequence
from threading import Timer


class RecurringTask:
    __slots__ = "interval", "function", "args", "kwargs", "_timer"

    def __init__(
        self,
        interval: float | int,
        function: Callable[..., None],
        args: Optional[Sequence[Any]] = None,
        kwargs: Optional[Mapping[str, Any]] = None,
    ):
        self.interval = interval
        self.function = function
        self.args: Sequence[Any] = tuple() if args is None else args
        self.kwargs: Mapping[str, Any] = dict() if kwargs is None else kwargs
        self._timer = None

    def start(self) -> None:
        def callback(task: RecurringTask):
            task.function(*task.args, **task.kwargs)
            task._timer = timer = Timer(task.interval, callback, (task,))
            timer.start()

        self.cancel()
        self._timer = timer = Timer(self.interval, callback, (self,))
        timer.start()

    def cancel(self) -> None:
        if self._timer:
            self._timer.cancel()
            self._timer = None
