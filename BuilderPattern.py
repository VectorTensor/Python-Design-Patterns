class Burger:
    def __init__(self, builder):
        self.patty = builder.patty
        self.tomato = builder.tomato
        self.onion = builder.onion

    def __str__(self):
        return f'{self.patty}, {self.tomato}, {self.onion}'

    class BurgerBuilder:
        def __init__(self):
            self.patty = False
            self.tomato = False
            self.onion = False

        def add_patty(self):
            self.patty = True
            return self

        def add_tomato(self):
            self.tomato = True
            return self

        def add_onion(self):
            self.onion = True
            return self

        def build(self):
            return Burger(self)


x = (Burger.BurgerBuilder()
     .add_tomato()
     .add_patty()
     .add_onion()
     .build())

print(x)
