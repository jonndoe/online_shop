import time
import random


def isEven(value):
    return value % 2 == 0


def is_even_other(value):
    if int(bin(value)[-1]) == 0:
        return True
    else:
        return False


print(isEven(22))

print(is_even_other(4578965461545465416541654165454661416546546541646462))


class RingBufferSimple:
    def __init__(self, size):
        self.data = [None for i in range(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data


# FIFO ringbuffer
class RingBuffer:

    """ class that implements a not-yet-full buffer """

    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    class __Full:

        """ class that implements a full buffer """

        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = x

            print("cur", self.cur + 1)
            print("max", self.max)

            print("% is ", (self.cur + 1) % self.max)
            print("%%%", 1 % 5)
            print("%%%", 4 % 5)

            self.cur = (self.cur + 1) % self.max
            print(self.cur)

        def get(self):
            """ return list of elements in correct order """
            return self.data[self.cur :] + self.data[: self.cur]

    def append(self, x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data


# sample usage
if __name__ == "__main__":

    start = time.time()

    buf = RingBufferSimple(4)
    for i in range(10):
        buf.append(i)
        print(buf.get())

    x = RingBuffer(5)
    x.append(1)
    x.append(2)
    x.append(3)
    x.append(4)
    print(x.__class__, x.get())
    x.append(5)
    print(x.__class__, x.get())
    x.append(6)
    print(x.data, x.get())

    for i in range(20000):
        x.append(i)

    x.append(7)
    x.append(8)
    x.append(9)
    x.append(10)
    x.append(11)
    x.append(12)
    x.append(13)
    print(x.data, x.get())

    stop = time.time()

    duration = stop - start

    print(duration)

    # sort algorithm
    random_list = []
    for i in range(10000):
        random_list.append(random.randint(0, 100))

    print(random_list)

    def partition(array, begin, end):
        pivot_idx = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(array, begin, end):
        if begin >= end:
            return "finish"
        pivot_idx = partition(array, begin, end)
        quick_sort_recursion(array, begin, pivot_idx - 1)
        quick_sort_recursion(array, pivot_idx + 1, end)

    def quick_sort(array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        return quick_sort_recursion(array, begin, end)

    quick_sort(random_list)
    print(random_list)


####################################################################3
# Задание №1


def is_even_other(value):
    if int(bin(value)[-1]) == 0:
        return True
    else:
        return False


print(isEven(22))
# -----------------------------------------------------------------------


# Задание №2

# FIFO ringbuffer1
class RingBufferSimple:
    def __init__(self, size):
        self.data = [None for i in range(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data


# FIFO ringbuffer2
class RingBuffer:

    """ class that implements a not-yet-full buffer """

    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    class __Full:

        """ class that implements a full buffer """

        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = x

            print("cur", self.cur + 1)
            print("max", self.max)

            print("% is ", (self.cur + 1) % self.max)
            print("%%%", 1 % 5)
            print("%%%", 4 % 5)

            self.cur = (self.cur + 1) % self.max
            print(self.cur)

        def get(self):
            """ return list of elements in correct order """
            return self.data[self.cur :] + self.data[: self.cur]

    def append(self, x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data

    # ---------------------------------------------------------------------------------------------------------

    # Задание3

    # sort algorithm

    random_list = []
    for i in range(10000):
        random_list.append(random.randint(0, 100))

    print(random_list)

    def partition(array, begin, end):
        pivot_idx = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(array, begin, end):
        if begin >= end:
            return "finish"
        pivot_idx = partition(array, begin, end)
        quick_sort_recursion(array, begin, pivot_idx - 1)
        quick_sort_recursion(array, pivot_idx + 1, end)

    def quick_sort(array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        return quick_sort_recursion(array, begin, end)

    quick_sort(random_list)
    print(random_list)
