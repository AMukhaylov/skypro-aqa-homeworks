class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

class Mailing:
    def __init__(self, to: Address, _from: Address, cost, track):
        self.to = to 
        self.from_ = _from
        self.cost = cost
        self.track = track