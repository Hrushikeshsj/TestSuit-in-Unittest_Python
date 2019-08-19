import unittest
from Package01.TC_LoginTest import LoginTest
from Package01.TC_SignUpTest import SignUpTest
from Package02.TC_PaymentReturn import PaymentReturn
from Package02.TC_PaymentTest import PaymentTest



# fetching all Test cases from a class
tc01 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc02 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc03 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)
tc04 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

# Creating a test suit
Sanity_Test_Suit = unittest.TestSuite([tc01, tc02])
Functional_Test_Suit = unittest.TestSuite([tc03, tc04])
Master_Test_Suit = unittest.TestSuite([tc04, tc03, tc02, tc01])

unittest.TextTestRunner(verbosity=2).run(Master_Test_Suit)





