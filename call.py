# class Point:
#     '''Описание работы класса'''
#     color = 'red'
#     circle = 2
import random


# class Book:
#
#     def __init__(self, name, author, isbn):
#         self.__name = name
#         self.__author = author
#         self.__isbn = isbn
#
#     def get_author(self):
#         return self.__author
#
#     def set_author(self, author):
#         self.__author = author
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_isbn(self):
#         return self.__isbn
#
#     def set_isbn(self, isbn):
#         self.__author = isbn
#
#
# b = Book('name', 'author1', 12356789)
# print(b.get_author())
# b.set_author('sdgnhfxdzsa')
# print(b.get_author())
# b.set_name('dgfsf')
# print(b.get_name())

# class Figure:
#
#     def __init__(self, coords, width, color):
#         self.coords = coords
#         self.width = width
#         self.color = color
#
#     def draw(self):
#         print(f'Рисуем фигуру цвета {self.color} и шириной {self.width}')
#
# class Line(Figure):
#     def draw(self):
#         print(f'Рисуем линию цветом {self.color} и шириной {self.width}')
#
#
# class Rect(Figure):
#     def __init__(self, coords, width, color, right):
#         super().__init__(coords, width, color)
#         self.right = right
#
#
#     def draw(self):
#         print(f'Рисуем прямоугольник цветом {self.color} и шириной {self.width}. Прямоугольник {self.right}')
#
# class Ellips(Figure):
#
#     def draw(self):
#         print(f'Рисуем эллипс цветом {self.color} и шириной {self.width}')
#
# f = Figure([1, 2, 4, 5, 7, 8], 2, 'black')
# f.draw()
# l = Line([1, 1, 5, 6],3, 'red')
# l.draw()
# e = Ellips([5, 5, 2, 9], 4, 'yellow')
# e.draw()
# r = Rect([1, 8, 6, 2], 6, 'blue', 'неправильный')
# r.draw()

# class Publicatioin:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def display(self):
#         print('Название:', self.title)
#         print(f'Автор: {self.author}')
#         print(f'Год издания: {self.year}')
#
# class Book(Publicatioin):
#     def __init__(self, title, author, year, isbn):
#         super().__init__(title, author, year)
#         self.isbn = isbn
#
#     def display(self):
#         super().display()
#         print(f'ISBN: {self.isbn}')
#
# class Magazine(Publicatioin):
#     def __init__(self, title, author, year, issue_number):
#         super().__init__(title, author, year)
#         self.issue_number = issue_number
#
#     def display(self):
#         super().display()
#         print(f'Номер журнала:{self.issue_number}')
#
#
# def info(obj):
#     obj.display()
#
# p = Publicatioin('Название1', 'Автор1', 2015)
# b = Book('Название2', 'Автор2', 2021, 98765432143)
# m = Magazine('Название3', 'Автор3', 2022, 5)
# list = []
# list.append(p)
# list.append(b)
# list.append(m)
# for i in list:
#     info(i)
#     print()



#ПРАКТИКА

# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f'''
# Название: {self.title}
# Исполнитель: {self.artist}
# Год выпуска: {self.release_year}
# Жанр: {self.genre}
# Список треков: {self.tracklist}
#                 ''')
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# album4.get_info()
# print(album4.play_random_track())

# class Student:
#
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def info(self):
#         print('Имя', self.name)
#         print('Возраст', self.age)
#         print('Класс', self.grade)
#         print('Оценки', self.scores)
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
#
# student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
# student2.info()
# print(student2.average_score())

# class Recipe:
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         print(f"Ингредиенты для {self.name}")
#         for ingredient in self.ingredients:
#             print(f"- {ingredient}")
#
#     def cook(self):
#         print(f"Сегодня мы готовим {self.name}.")
#         print(f"Выполняем инструкцию по приготовлению блюда {self.name}...")
#         print(f"Блюдо {self.name} готово!")
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# spaghetti.print_ingredients()
# spaghetti.cook()
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
# cake.print_ingredients()
# cake.cook()

# class Publisher:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#
#     def get_info(self):
#         return f"{self.name} ({self.location})"
#
#     def publish(self, message):
#         print(f'Готовим "{message}" к публикации в {self.get_info()}')
#
#
# class BookPublisher(Publisher):
#     def __init__(self, name, location, num_authors):
#         super().__init__(name, location)
#         self.num_authors = num_authors
#
#     def publish(self, title, author):
#         print(f"Передаем рукопись '{title}', написанную автором {author} в издательство {self.get_info()}")
#
#
# class NewspaperPublisher(Publisher):
#     def __init__(self, name, location, num_pages):
#         super().__init__(name, location)
#         self.num_pages = num_pages
#
#     def publish(self, title):
#         print(f'Печатаем свежий номер со статьей "{title}" на главной странице в издательстве {self.get_info()}')
#
#
# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish("Справочник писателя")
#
# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")
#
# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish("Новая версия Midjourney будет платной")

# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.balance = balance
#         self.interest_rate = interest_rate
#         self.transactions = []
#
#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"Внесение наличных на счет: {amount}")
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self.transactions.append(f'Снятие наличных: {amount}')
#         else:
#             print("Недостаточно средств на счете")
#
#     def add_interest(self):
#         sum_balance_interest = self.balance * self.interest_rate
#         self.balance += sum_balance_interest
#         self.transactions.append(f'Начислены проценты по вкладу {sum_balance_interest}')
#
#     def history(self):
#         for transaction in self.transactions:
#             print(transaction)
#
# # создаем объект счета с балансом 100000 и процентом по вкладу 0.05
# account = BankAccount(100000, 0.05)
#
# # вносим 15 тысяч на счет
# account.deposit(15000)
#
# # снимаем 7500 рублей
# account.withdraw(7500)
#
# # начисляем проценты по вкладу
# account.add_interest()
#
# # печатаем историю операций
# account.history()


# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.bonus = 0
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_salary(self):
#         return self.salary
#
#     def set_bonus(self, bonus):
#         self.bonus = bonus
#
#     def get_bonus(self):
#         return self.bonus
#
#     def get_total_salary(self):
#         return self.salary + self.bonus
#
#
# # создаем сотрудника с именем, возрастом и зарплатой
# employee = Employee("Марина Арефьева", 30, 90000)
#
# # устанавливаем бонус для сотрудника
# employee.set_bonus(15000)
#
# # выводим имя, возраст, зарплату, бонус и общую зарплату сотрудника
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())


# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(f"{self.name} подает голос")
#
#     def move(self):
#         print(f"{self.name} дергает хвостом")
#
# class Dog(Animal):
#     def __init__(self, name, breed, legs):
#         super().__init__(name, breed, legs)
#         self.breed = breed
#
#     def bark(self):
#         print(f"{self.breed} {self.name} лает")
#
# class Bird(Animal):
#     def __init__(self, name, species, wingspan):
#         super().__init__(name, species, 2)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(f"{self.species} {self.name} летaeт")
#
#
# dog = Dog("Геральт", "доберман", 4)
# bird = Bird("Вася", "попугай", 2)
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()


