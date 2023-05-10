# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
# Example:
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
# ["bar"]


class HistoryDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.history.append(key)
        if len(self.history) > 10:
            self.history.pop(0)

    def get_history(self):
        return self.history


d = HistoryDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
d['h'] = 8
d['i'] = 9
d['j'] = 10
d['k'] = 11

print(d.get_history())
