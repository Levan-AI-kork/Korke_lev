# # BankAccount კლასი - საბანკო ანგარიშის სიმულაცია
#
# class BankAccount:
#
#     def __init__(self, owner, balance):
#         self.owner = owner          # საჯარო ატრიბუტი - მფლობელის სახელი
#         self.__balance = balance    # პრივატული ატრიბუტი - ბალანსი (გარედან პირდაპირ არ იცვლება)
#
#     # თანხის შეტანა ანგარიშზე
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance = self.__balance + amount
#         else:
#             print("შეცდომა: შეტანილი თანხა უნდა იყოს დადებითი რიცხვი!")
#
#     # თანხის გატანა ანგარიშიდან
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("შეცდომა: არასაკმარისი თანხაა ბალანსზე!")
#         else:
#             self.__balance = self.__balance - amount
#
#     # property - ბალანსის წაკითხვა (account.balance)
#     @property
#     def balance(self):
#         return self.__balance
#
#     # setter - ბალანსის დაყენება (account.balance = value)
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             print("შეცდომა: ბალანსი ვერ იქნება უარყოფითი!")
#         else:
#             self.__balance = value
#
#     # კლასის ობიექტის ტექსტური სახე print()-ისთვის
#     def __str__(self):
#         return f"Owner: {self.owner} | Balance: {self.__balance} GEL"
#
#
# # --- გამოყენების მაგალითი ---
#
# account = BankAccount("Nika", 1000)
# print(account)
#
# account.deposit(500)
# print(account.balance)
#
# account.withdraw(200)
# print(account.balance)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in")


class Admin(User):
    def delete_user(self):
        print(f"{self.username} deleted a user")


class Logger:
    def log(self):
        print("Logging action...")


class SuperAdmin(Admin, Logger):
    pass


super_admin = SuperAdmin("Nika", "nika@example.com")
super_admin.login()
super_admin.delete_user()
super_admin.log()

print(SuperAdmin.mro())


Python მეთოდს ეძებს კლასების იმ თანმიმდევრობით, რასაც mro() აჩვენებს: SuperAdmin → Admin → User → Logger → object. ანუ ჯერ თავად კლასში იძებნება, მერე მშობლებში — მარცხნიდან მარჯვნივ, თან ისე, რომ თითოეული კლასი სიაში მხოლოდ ერთხელ და თანმიმდევრულად გამოჩნდეს. როგორც კი პირველ კლასს იპოვის, სადაც ეს მეთოდია განსაზღვრული, იქვე ჩერდება.
