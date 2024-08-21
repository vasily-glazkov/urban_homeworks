import unittest
from unittest.mock import patch
from io import StringIO

# Import the functions to be tested
from module_3.module_3_2 import check_validity, send_email

class TestEmailSender(unittest.TestCase):
    def test_check_validity(self):
        # Test valid email addresses
        self.assertTrue(check_validity('user@example.com', 'sender@example.com'))
        self.assertTrue(check_validity('user@example.ru', 'sender@example.net'))
        
        # Test invalid email addresses
        self.assertFalse(check_validity('user@example', 'sender@example.com'))
        self.assertFalse(check_validity('user@example.com', 'sender@example'))
        self.assertFalse(check_validity('user@example.xyz', 'sender@example.com'))
        self.assertFalse(check_validity('user@example.com', 'sender@example.xyz'))
        
    def test_send_email(self):
        # Test valid email addresses
        with patch('sys.stdout', new=StringIO()) as fake_out:
            send_email('Test message', 'user@example.com')
            self.assertEqual(fake_out.getvalue().strip(), 'Письмо успешно отправлено с адреса university.help@gmail.com на адрес user@example.com.')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            send_email('Test message', 'user@example.com', sender='custom@example.com')
            self.assertEqual(fake_out.getvalue().strip(), 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса custom@example.com на адрес user@example.com.')
            
        # Test invalid email addresses
        with patch('sys.stdout', new=StringIO()) as fake_out:
            send_email('Test message', 'user@example', sender='custom@example.com')
            self.assertEqual(fake_out.getvalue().strip(), 'Невозможно отправить письмо с адреса custom@example.com на адрес user@example')
            
        # Test sending to self
        with patch('sys.stdout', new=StringIO()) as fake_out:
            send_email('Test message', 'user@example.com', sender='user@example.com')
            self.assertEqual(fake_out.getvalue().strip(), 'Нельзя отправить письмо самому себе!')

if __name__ == '__main__':
    unittest.main()
