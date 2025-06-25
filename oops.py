class Seasons: 
    def __init__(self,name):
        self.name=name
        self.weather=""
        self.months=""
        self.holiday=""
    def find_weather(self):
        if self.name=="summer":
            self.weather="sunny"
        elif self.name=="spring":
            self.weather="rainy"
        elif self.name== "winter":
            self.weather="snowy"
        elif self.name=="fall":
            self.weather="chilly"
    def find_months(self):
        if self.name=="summer":
            self.months=["June","Julyyyy","August"]
        if self.name=="spring":
            self.months=["March","April","May"]
        if self.name=="winter":
            self.months=["December","January","February"]
        if self.name=="fall":
            self.months=["September","October","November"]
    def find_holidays(self):
        if self.name=="summer":
            self.holiday="July 4th"
        if self.name=="spring":
            self.holiday="Easter"
        if self.name=="winter":
            self.holiday="Christmas"
        if self.name=="fall":
            self.holiday="Halloween"
    def print_details(self):
        print("the weather will be",self.weather)
        print("the months are")
        for month in self.months:
            print (month)
        print("the holiday is",self.holiday)
    def change_holiday(self):
        if self.name=="spring":
            self.holiday=input("what holiday do you want in spring?")
        if self.name=="winter":
            self.holiday=input("what holiday do you want in winter?")
        if self.name=="fall":
            self.holiday=input("what holiday do you want in fall?")
        if self.name=="summer":
            self.holiday=input("what holiday do you want in summer?")

        
s1=Seasons("summer")    
s1.find_months()    
s1.find_holidays()
s1.find_weather()
s1.change_holiday()
s1.print_details()

s2=Seasons("spring")    
s2.find_months()    
s2.find_holidays()
s2.find_weather()
s2.print_details()

s3=Seasons("winter")    
s3.find_months()    
s3.find_holidays()
s3.find_weather()
s3.print_details()

s4=Seasons("fall")    
s4.find_months()    
s4.find_holidays()
s4.find_weather()
s4.print_details()





#homework:Implement a class on  Bank Account details of a person
#account number
#balance
#withdrawal
#deposit

class Bank_Account: 
    def __init__(self,number):
        self.number=number
        self.balance=""
        self.withdrawl=""
        self.deposit=""
    def find_balance(self):
        if self.number=="123":
            self.balance="$5000"
        elif self.number=="124":
            self.balance="100000"
    def find_withdrawl(self):
        if self.number=="123":
            self.withdrawl="$100"
        if self.number=="124":
            self.withdrawl="1000"
    def find_deposit(self):
        if self.number=="123":
            self.deposit="$1"
        if self.number=="124":
            self.deposit="$10000000"
    def print_details(self):
        print("your balance is",self.balance)
        print("your recent withdrawl was",self.withdrawl)
        print("your deposit is",self.deposit)
    def change_deposit(self):
        if self.number=="123":
            self.holiday=input("How much would you like to deposit instead?")
        if self.number=="124":
            self.holiday=input("How much would you like to deposit insted?")

b1=Bank_Account("123")    
b1.find_balance()    
b1.find_withdrawl()
b1.find_deposit()
b1.change_deposit()
b1.print_details()






