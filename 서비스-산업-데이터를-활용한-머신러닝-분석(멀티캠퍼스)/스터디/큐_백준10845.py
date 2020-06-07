queue = []

def push(x):
    return queue.append(x)

# pop 틀림
def pop(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[0]

def size(queue):
    return len(queue)

def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0

def front(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[0]