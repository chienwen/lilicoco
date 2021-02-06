import collections
import queue
import time

testNumSteps = 1000000

queue1 = collections.deque([])
d1start = time.time()
for i in range(testNumSteps):
    queue1.append(i)
for i in range(testNumSteps):
    queue1.popleft()
print('deque spent', time.time() - d1start, 'seconds')

queue2 = queue.Queue()
d2start = time.time()
for i in range(testNumSteps):
    queue2.put(i)
for i in range(testNumSteps):
    queue2.get()
print('queue spent', time.time() - d2start, 'seconds')
