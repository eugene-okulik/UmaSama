class Flower:
    def __init__(self, name, color, stem_length, price, freshness, lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.freshness = freshness
        self.lifetime = lifetime

    def __repr__(self):
        return f"{self.name} ({self.color})"


class Rose(Flower):
    pass


class Tulip(Flower):
    pass


class Lily(Flower):
    pass


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        return sum(f.price for f in self.flowers)

    def withering_time(self):
        if not self.flowers:
            return 0
        return sum(f.lifetime for f in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda f: f.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda f: f.color)

    def sort_by_stem(self):
        self.flowers.sort(key=lambda f: f.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda f: f.price)

    def find_by_lifetime(self, min_lifetime):
        return [f for f in self.flowers if f.lifetime >= min_lifetime]


rose1 = Rose("Красная роза", "красный", 50, 100, 100, 7)
rose2 = Rose("Белая роза", "белый", 45, 90, 95, 6)
tulip1 = Tulip("Желтый тюльпан", "желтый", 40, 50, 98, 5)
lily1 = Lily("Белая лилия", "белый", 60, 150, 90, 10)

bouquet = Bouquet([rose1, rose2, tulip1, lily1])

print("Стоимость:", bouquet.total_price())
print("Увядание:", bouquet.withering_time())

print("Долгожители:", [str(f) for f in bouquet.find_by_lifetime(7)])

bouquet.sort_by_freshness()
print("По свежести:", [str(f) for f in bouquet.flowers])
