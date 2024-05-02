class loginandregister:
    print("hey! whatsup?...")

    def reg(self):
        self.data = []
        username = input("enter your email: ")
        password = input("enter your phone_num: ")
        phone_num = input("enter username: ")
        email = input("enter password: ")
        print("registration successful")
        self.data.append(username)
        self.data.append(password)
        self.data.append(phone_num)
        self.data.append(email)

    def login(self):
        login_username = input("enter username: ")
        login_password = input("enter login password: ")
        if login_username in self.data and login_password in self.data:
            print("login success")
            print("welcome",login_username,"!you are a wonderer...")
        else:
            print("invalid")

obj = loginandregister()

while True:
    print("1.register, 2.login ")
    choice=int(input("enter your choice:"))
    if choice == 1:
        obj.reg()
    elif choice == 2:
        obj.login()
        break
    


class traveller(loginandregister):
    def init(self, mode_of_transport, destination, days,price):
        self.mode_of_transport = mode_of_transport
        self.destination = destination
        self.days = days
        self.price = price

    def calculate(self):
        if self.mode_of_transport == "Bus" and self.destination == "kerala" and self.days==3:
            self.price = 7000
        elif self.mode_of_transport == "Bus" and self.destination == "kerala" and self.days==4:
            self.price = 9000
        elif self.mode_of_transport == "Bus" and self.destination == "kerala" and self.days==5:
            self.price = 10000
        elif self.mode_of_transport == "Bus" and self.destination == "tamilnadu"and self.days==3 :
            self.price = 15000
        elif self.mode_of_transport == "Bus" and self.destination == "tamilnadu"and self.days==4 :
            self.price = 17000
        elif self.mode_of_transport == "Bus" and self.destination == "tamilnadu"and self.days==5 :
            self.price = 18000
        elif self.mode_of_transport == "Bus" and self.destination == "pondicherry"and self.days==3 :
            self.price = 20500
        elif self.mode_of_transport == "Bus" and self.destination == "pondicherry"and self.days==4 :
            self.price = 21500
        elif self.mode_of_transport == "Bus" and self.destination == "pondicherry"and self.days==5 :
            self.price = 22500
        elif self.mode_of_transport == "train" and self.destination == "goa"and self.days==6 :
            self.price = 20000
        elif self.mode_of_transport == "train" and self.destination == "goa"and self.days==7 :
            self.price = 22000
        elif self.mode_of_transport == "train" and self.destination == "goa"and self.days==8 :
            self.price = 23000
        elif self.mode_of_transport == "train" and self.destination == "kodagu"and self.days==6 :
            self.price = 14000
        elif self.mode_of_transport == "train" and self.destination == "kodagu"and self.days==7 :
            self.price = 16000
        elif self.mode_of_transport == "train" and self.destination == "kodagu"and self.days==8 :
            self.price = 18000
        elif self.mode_of_transport == "train" and self.destination == "mysore"and self.days==6 :
            self.price = 15000
        elif self.mode_of_transport == "train" and self.destination == "mysore"and self.days==7 :
            self.price = 17000
        elif self.mode_of_transport == "train" and self.destination == "mysore"and self.days==8 :
            self.price = 18500
        elif self.mode_of_transport == "flight" and self.destination == "pune" and self.days==8:
            self.price = 104000
        elif self.mode_of_transport == "flight" and self.destination == "pune" and self.days==9:
            self.price = 106000
        elif self.mode_of_transport == "flight" and self.destination == "pune" and self.days==10:
            self.price = 108000
        elif self.mode_of_transport == "flight" and self.destination == "mumbai"and self.days==8 :
            self.price = 150000
        elif self.mode_of_transport == "flight" and self.destination == "mumbai"and self.days==9 :
            self.price = 152000
        elif self.mode_of_transport == "flight" and self.destination == "mumbai"and self.days==10 :
            self.price = 154000
        elif self.mode_of_transport == "flight" and self.destination == "kashmir" and self.days==8:
            self.price = 200000
        elif self.mode_of_transport == "flight" and self.destination == "kashmir" and self.days==9:
            self.price = 202000
        elif self.mode_of_transport == "flight" and self.destination == "kashmir" and self.days==10:
            self.price = 206000
        print("num of days",self.days)
        print("Total cost:", self.price)
obj=traveller()
        

while True:
    print("1. Bus, 2. train, 3. flight")
    mode_of_transport = int(input("Choose the mode of transport from which you wish to travel: "))
    if mode_of_transport == 1:
        destination = input("Choose your favorite destination ( kerala, tamilnadu, pondicherry): ")
        days= int(input("choose no of  days(3,4,5):"))
        obj.mode_of_transport = "Bus"
        obj.destination = destination
        obj.days=days
        obj.calculate()
        print("WELCOME TO",destination)
        break
    elif mode_of_transport == 2:
        destination = input("Choose your favorite destination ( goa, kodagu, mysore): ")
        days= int(input("choose no of  days(6,7,8):"))
        obj.mode_of_transport = "train"
        obj.destination = destination
        obj.days=days
        obj.calculate()
        print("WELCOME TO",destination)
        break
    elif mode_of_transport == 3:
        destination = input("Choose your favorite destination ( pune, mumbai, kashmir): ")
        days= int(input("choose no of  days(8,9,10):"))
        obj.mode_of_transport = "flight"
        obj.destination = destination
        obj.days=days
        obj.calculate()
        print("WELCOME TO",destination)
        break
    else:
        print("Enter valid option")