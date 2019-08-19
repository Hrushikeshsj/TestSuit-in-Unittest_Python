import unittest
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    def test_login_by_email(self):
        print("this is log in by email")
        self.assertTrue(True)

    def test_login_by_num(self):
        print("this is log in by Mobile Number")
        self.assertTrue(True)

    def test_login_by_fb(self):
        print("this is log in by facebook account")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()