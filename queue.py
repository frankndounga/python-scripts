class QueueError(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)
        

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, value):
        self.__queue.append(value)

    def get(self):
        if len(self.__queue) == 0:
            try:
                raise QueueError('You cannot get a value from an empty queue')
            except QueueError:
                print('Something went wrong')
                raise
        value = self.__queue[0]
        del self.__queue[0]
        return value
    
    def get_queue(self):
        return self.__queue
    
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def is_queue_empty(self):
        return True if len(Queue.get_queue(self)) == 0 else False

if __name__ == '__main__':

    queue1 = Queue()
    queue1.put('armel')
    #queue1.put('ulrich')

    try:
        print(queue1.get())
        print(queue1.get())
    except Exception:
        print('An exception was raised')

    print(queue1.get_queue())

    queue2 = SuperQueue()
    queue2.put('Frank')
    try:
        print(queue2.get())
        print(queue2.get())
    except QueueError:
        print('Another exception was raised')

    print(queue2.is_queue_empty())