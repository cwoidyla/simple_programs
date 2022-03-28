import timeit
import functools
import time

class TimeMe:
    @staticmethod
    def timer(func):
        """
        Print the runtime of the decorated function
        """
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = timeit.default_timer()
            value = func(*args, **kwargs)
            elapsed = timeit.default_timer() - start_time
            print("Executed in {} seconds".format(str(elapsed)))
            return value
        return wrapper_timer

@TimeMe.timer
def nap_time(seconds):
    time.sleep(seconds)

nap_time(1)