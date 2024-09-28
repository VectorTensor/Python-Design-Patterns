class AddMixin:
    def add(self):
        return self.a + self.b


class SubMixin:
    def sub(self):
        return self.a - self.b


class Opt(AddMixin, SubMixin):
    def __init__(self, a=10, b=20):
        self.a = a
        self.b = b


o = Opt()
print(o.add())
print(o.sub())