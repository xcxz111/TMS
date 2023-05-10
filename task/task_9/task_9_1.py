# Implement a Counter class which optionally accepts the start value and the
# counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."
# Implement to methods: "increment" and "get"
# * <em>If you're familiar with Esception rising use it to display the "Maximal
#  value is reached." message.</em>
#  Example:
#  ```python
#   >>> c = Counter(start=42)
#  >>> c.increment()
#  >>> c.get()
# 43
# 1 2
# 43
# 43
# ```
#  >>> c = Counter()
# >>> c.increment()
#  >>> c.get()
#  >>> c.increment()
#  >>> c.get()
#  >>> c = Counter(start=42, stop=43)
#  >>> c.increment()
#  >>> c.get()
#  >>> c.increment()
#  Maximal value is reached.
#  >>> c.get()

class Counter:
    def __init__(self, value=0, stop=None):
        self.value = value
        self.stop = stop

    def increment(self):
        if self.stop is None or self.value < self.stop:
            self.value += 1
        else:
            raise Exception('Достигнуто максимальное значение')

    def get(self):
        return self.value


counter = Counter(stop=10)

try:
    while True:
        print(counter.get())
        counter.increment()
except Exception as e:
    print(e)



