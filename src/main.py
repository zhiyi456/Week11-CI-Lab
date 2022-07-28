from Account import Bank_Account
#creating an object of class
s = Bank_Account(1000, "Preethi")
s1 = Bank_Account(1000, "Chris")
if (s.__eq__(s1)): print ("Equal") 
else: print("Not Equal")
#calling functions with that class
s.deposit(1000)
s.withdraw(500)
#s.display()