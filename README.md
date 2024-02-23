recurring task
==============

Virtually the same concept of JavaScript's `setInterval` but for Python.

```python3
# examples/greet.py

from recurring_task import RecurringTask

# create a recurring task that prints "Hello world!" every 2 seconds
# note that this won't start the task
t = RecurringTask(2, lambda: print("Hello world!"))

# start is non-blocking, the task run in its own thread
t.start() 

# stop the task when you're done
t.cancel()
```
