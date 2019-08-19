import unittest


class PaymentTest(unittest.TestCase):

    def test_PaymentinDoller(self):
        print("payment is done in Dollers")
        self.assertTrue(True)

    def test_PaymentinRupee(self):
        print("payment is done in Rupees")
        self.assertTrue(False, "Payment in Rupees not allowed")


if __name__ == "__main__":
    unittest.main()

