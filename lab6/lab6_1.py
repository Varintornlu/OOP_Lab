class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        
    def get_name(self):
        return self.__name
        
        
class Account:
    def __init__(self, account_number, balance, owner):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner
        self.__transaction_list = []
        self.__transaction_show_list = []
        
    def __str__(self):
        return "\n".join(self.__transaction_show_list)
    
    @property
    def account_number(self):
        return self.__account_number
        
    @property
    def owner(self):
        return self.__owner
        
    @property
    def balance(self):
        return self.__balance
    
    @property
    def transaction_list(self):
        return self.__transaction_list
    
    def deposit(self, atm, money):
        if money > 0 and atm.limit >= money:
            result1 = f"{self.owner.get_name()} account before test : {self.balance}"
            self.__balance += money
            atm.limit = money
            atm.money_remaining_deposit = money

            transaction_show_list_detail = f"{self.owner.get_name()} transaction : D-ATM:{atm.atm_number}-{money}-{self.__balance}"
            self.__transaction_show_list.append(transaction_show_list_detail)
            result2 = f"{self.owner.get_name()} account after test : {self.balance}"
            
            self.__transaction_list.append(Transaction('Deposit', money, None, atm.atm_number, None))
            
            return f"{result1}\n{result2}"
        return "Error"
    
    def withdraw(self, atm, money):
        if money > 0 and self.balance >= money and atm.limit >= money and atm.money_remaining >= money:
            result1 = f"{self.owner.get_name()} account before test : {self.balance}"
            self.__balance -= money
            atm.limit = money
            atm.money_remaining_withdraw = money
            
            transaction_show_list_detail = f"{self.owner.get_name()} transaction : W-ATM:{atm.atm_number}-{money}-{self.__balance}"
            self.__transaction_show_list.append(transaction_show_list_detail)
            result2 = f"{self.owner.get_name()} account after test : {self.balance}" 
            self.__transaction_list.append(Transaction('Withdraw', money, None, atm.atm_number, None))
        
            return f"{result1}\n{result2}"
        return "Error"
    
    def transfer(self, atm, money, partner):
        if money > 0 and self.balance >= money:
            result1 = F"{self.owner.get_name()} account before test : {self.__balance}"
            self.__balance -= money
            atm.limit = money
            self.__transaction_show_list.append(F"{self.owner.get_name()} transaction : T-ATM:{atm.atm_number}-{money}-{self.__balance}")
            result2 = F"{self.owner.get_name()} account after test : {self.__balance}"
            
            result3 = F"{partner.owner.get_name()} account before test : {partner.__balance}"
            partner.__balance += money
            partner.__transaction_show_list.append(F"{partner.owner.get_name()} transaction : T-ATM:{atm.atm_number}-+{money}-{partner.__balance}")
            result4 = F"{partner.owner.get_name()} account after test : {partner.__balance}"
            
            self.__transaction_list.append(Transaction('Transfer', money, None, atm.atm_number, self.__account_number))
        
            return F"{result1}\n{result2}\n{result3}\n{result4}"
        return "Error"
    
        
        
class ATMcard:
    fee = 150
    def __init__(self, atm_number, pin_number, account):
        self.__atm_number = atm_number
        self.__pin_number = pin_number
        self.__account = account
        
    @property
    def atm_number(self):
        return self.__atm_number
        
    @property
    def pin_number(self):
        return self.__pin_number
        
    @property
    def account(self):
        return self.__account

    
    
        
class Atm:
    def __init__(self, atm_number, money_remaining):
        self.__atm_number = atm_number
        self.__money_remaining = money_remaining #money remain in atm mechine
        self.__limit = 40000 #limit money
        
    @property
    def atm_number(self):
        return self.__atm_number
    
    @property
    def limit(self):
        return self.__limit
    
    @property
    def money_remaining(self):
        return self.__money_remaining
    
    @limit.setter
    def limit(self, money):
        if self.__limit >= money:
            self.__limit -= money
            
    @money_remaining.setter
    def money_remaining_deposit(self, money):
        self.__money_remaining += money_remaining
            
    @money_remaining.setter
    def money_remaaining_withdraw(self, money):
        if self.__money_remaining >= money:
            self.__money_remaining -= money_remaining
        
    def deposit(self, atm, money):
        if money > 0 and atm.limit >= money:
            result1 = f"{self.owner.get_name()} account before test : {self.balance}"
            self.__balance += money
            atm.limit = money
            atm.money_remaining_deposit = money

            transaction_show_list_detail = f"{self.owner.get_name()} transaction : D-ATM:{atm.atm_number}-{money}-{self.__balance}"
            self.__transaction_show_list.append(transaction_show_list_detail)
            result2 = f"{self.owner.get_name()} account after test : {self.balance}"
            
            self.__transaction_list.append(Transaction('Deposit', money, None, atm.atm_number, None))
            
            return f"{result1}\n{result2}"
        return "Error"
    
    def withdraw(self, atm, money):
        if money > 0 and self.balance >= money and atm.limit >= money and atm.money_remaining >= money:
            result1 = f"{self.owner.get_name()} account before test : {self.balance}"
            self.__balance -= money
            atm.limit = money
            atm.money_remaining_withdraw = money
            
            transaction_show_list_detail = f"{self.owner.get_name()} transaction : W-ATM:{atm.atm_number}-{money}-{self.__balance}"
            self.__transaction_show_list.append(transaction_show_list_detail)
            result2 = f"{self.owner.get_name()} account after test : {self.balance}" 
            self.__transaction_list.append(Transaction('Withdraw', money, None, atm.atm_number, None))
        
            return f"{result1}\n{result2}"
        return "Error"
    
    def insert_card(self, ATMcard, pin_number):
        if ATMcard.pin_number == pin_number:
            return ATMcard.atm_number, ATMcard.account.account_number, "Sucess"
        return "Error"
    
class Transaction:
    def __init__(self, type, amount_money, date_time, atm_number, partner):
        self.__type = type
        self.__amount_money = amount_money
        self.__date_time = date_time
        self.__atm_number = atm_number
        self.__partner = partner
        
class Bank:
    def __init__(self):
        self.__user_list = []
        self.__atm_list = []
        
    def add_user_list(self, user, account, ATMcard):
        self.__user_list.append((user, account, ATMcard))
        
    def add_atm_list(self, atm):
        self.__atm_list.append(atm)
        
    @property
    def get_user_list(self):
        return self.__user_list
    
    @property
    def get_atm_list(self):
        return self.__atm_list

users ={'1-1101-12345-52-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-53-0':['Hermione Jean Granger','0987654321','12346',1000]}

atms ={'1001':1000000,'1002':200000}

bank = Bank()

for user_id, infomation in users.items():
    user = User(user_id, infomation[0])
    account = Account(infomation[1], infomation[3], user)
    atm_card = ATMcard(infomation[2], '1234' ,account)
    bank.add_user_list(user, account, atm_card)
    
for atm_number, money_remaining in atms.items():
    bank.add_atm_list(Atm(atm_number, money_remaining))
    
# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1")
print(bank.get_atm_list[0].insert_card(bank.get_user_list[0][2], '1234'), end='\n\n')

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2")
print(bank.get_user_list[1][1].deposit(bank.get_atm_list[1], 1000), end="\n\n")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3")
print(bank.get_user_list[1][1].deposit(bank.get_atm_list[1], -1), end="\n\n")

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test case #4")
print(bank.get_user_list[1][1].withdraw(bank.get_atm_list[1], 500), end="\n\n")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #5")
print(bank.get_user_list[1][1].withdraw(bank.get_atm_list[1], 2000), end="\n\n")

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test case #6")
print(bank.get_user_list[0][1].transfer(bank.get_atm_list[1], 10000, bank.get_user_list[1][1]), end="\n\n")

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test case #7")
print(bank.get_user_list[1][1])