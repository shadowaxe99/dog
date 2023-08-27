```python
from collections import deque
from time import sleep

class RateLimiter:
    def __init__(self, rate_limit=60):
        self.queue = deque()
        self.rate_limit = rate_limit

    def add_request(self):
        self.queue.appendleft(1)
        if len(self.queue) > self.rate_limit:
            self.queue.pop()
            sleep(1)
```