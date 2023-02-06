from address import Address
from address import Mailing

print_address = Mailing(Address("187330", "Санкт-Петербург", "Софийская улица", "12", "1"), 
Address("614000", "Пермь", "Ленина", "101", "17"), cost=1700, track="7738493LP") 

print("Отправление", print_address.track, "из", print_address.to.city, print_address.to.street, print_address.to.house, print_address.to.apartment,
"в", print_address.from_.city, print_address.from_.street, print_address.from_.house, print_address.from_.apartment, 
"Стоимость", print_address.cost, "рублей.")