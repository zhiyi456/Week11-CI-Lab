import unittest
import unittest.mock
from unittest.mock import MagicMock, patch
from src.Account import Bank_Account
from src.Interest_Rate_Computer import Interest_Rate_Computer

class testBankAccount(unittest.TestCase):
   def setUp(self):
     self.s = Bank_Account(1000, "Preethi")
     self.s1 = Bank_Account(1500, "Chris")
     self.s2 = Bank_Account(1000, "Daniel")
   def tearDown(self):
      self.s = None
      self.s1 = None
      self.s2 = None
   def test_deposit(self):
    bal = self.s.balance()
    self.assertEqual(bal, 1000)
    self.assertEqual(self.s.name(), "Preethi")
    self.assertEqual(self.s.deposit(500), 1500)
   def test_withdraw(self):
    self.assertEqual(self.s1.withdraw(1000), 500)
    self.assertEqual(self.s1.balance(), 500)
    self.assertRaises(Exception, self.s1.withdraw, 600)

   @patch('src.Interest_Rate_Computer.Interest_Rate_Computer.getRate', return_value = 0.02)
   def test_interest(self, getRate):
      interest_computer_mock = Interest_Rate_Computer()
      #interest_computer_mock.getRate = MagicMock(interest_computer_mock, return_value = 0.02)
      
      self.assertEqual(self.s.interest(interest_computer_mock), 0.02*self.s.balance())

   def test_EqualAccounts(self):
      self.assertTrue(self.s.balance() > 0)
      self.assertIsNot(self.s, self.s2)
      self.assertIs(self.s,self.s)

    
       
    
   