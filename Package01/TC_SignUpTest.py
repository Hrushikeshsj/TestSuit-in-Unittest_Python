import unittest


class SignUpTest(unittest.TestCase):

    def test_signup_by_email(self):
        print("this is Signup by email")
        self.assertTrue(True)

    def test_signup_by_num(self):
        print("this is Signup by Mobile Number")
        self.assertTrue(True)

    def test_signup_by_fb(self):
        print("this is Signup by facebook account")
        self.assertTrue(False, "Test is marked as false intensionally")


if __name__ == "__main__":
    unittest.main()
