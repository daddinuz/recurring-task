import time
from recurring_task import RecurringTask


def main():
    # create a recurring task that prints "Hello world!" every 2 seconds
    # note that this won't start the task
    t = RecurringTask(2, lambda: print("Hello world!"))

    # start is non-blocking, the task run in its own thread
    t.start()

    print("task started")
    
    # let it run for 2 times
    time.sleep(4.5)

    # stop the task when you're done
    t.cancel()

    print("task stopped")



if __name__ == "__main__":
    main()
