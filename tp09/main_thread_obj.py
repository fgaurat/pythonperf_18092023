from collections.abc import Callable, Iterable, Mapping
import threading
import time
from typing import Any


the_lock = threading.Lock()

class TheThread(threading.Thread):

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        with the_lock:
            for i in range(5):
                print(threading.current_thread().name,i)
                time.sleep(i)


def main():
    th1 = TheThread()
    th2 = TheThread()

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("après les threads")

if __name__=='__main__':
    main()
