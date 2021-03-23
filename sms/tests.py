from django.test import TestCase
import sqlite3

# Create your tests here.

from sms.models import Order


class SMSTests(TestCase):
    def test_for_json_support(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT JSON(\'{"a": "b"}\')')
            self.assertIs(False, False)
        except:
            self.assertIs(True, False, "no support for json in sqlite3")
    def test_welcome(self):
        oOrder = Order(phone = '123-456-7890', data={"state":"WELCOMING"})
        aReturn = oOrder.handleInput("hello")
        self.assertEqual(aReturn[0], "Welcome to Rich's pizza", "welcome message line 1")
        self.assertEqual(aReturn[1], "Would you like a SMALL, MEDIUM, or LARGE?", "welcome message line 2")
        self.assertEqual(oOrder.getState(), "SIZE", "order state should be SIZE")
    def test_size(self):
        oOrder = Order(phone = '123-456-7890', data={"state":"SIZE"})
        aReturn = oOrder.handleInput("small")
        self.assertEqual(aReturn[0], "What toppings would you like?", "size message line 1")
        self.assertEqual(aReturn[1], "(please enter a list with commas)", "size message line 2")
        self.assertEqual(oOrder.getState(), "TOPPINGS", "order state should be TOPPINGS")
        self.assertEqual(oOrder.getSize(), "small", "size should be small")
    def test_toppings(self):
        oOrder = Order(phone = '123-456-7890', data={"state":"TOPPINGS"})
        aReturn = oOrder.handleInput("canadian, hot peppers, and onions")
        self.assertEqual(aReturn[0], "Would you like drinks with that?", "toppings message line 1")
        self.assertEqual(aReturn[1], "(please enter a list with commas or NO)", "toppings message line 2")
        self.assertEqual(oOrder.getState(), "DRINKS", "order state should be DRINKS")
        self.assertEqual(oOrder.getToppings(), "canadian, hot peppers, and onions", "toppings should be as entered")
    def test_no_drinks(self):
        oOrder = Order(phone = '123-456-7890', data={"state":"SIZE"})
        aReturn = oOrder.handleInput("medium")
        aReturn = oOrder.handleInput("hot peppers and anchovies")
        aReturn = oOrder.handleInput("no")
        self.assertEqual(aReturn[0], "Thank you for your order", "drinks message line 1")
        self.assertEqual(aReturn[1], "medium pizza. With hot peppers and anchovies", "complete order")
        self.assertEqual(aReturn[2], "Please pickup in 20 minutes", "drinks message line 2")
        self.assertEqual(oOrder.getState(), "DONE", "order state should be DONE")
        self.assertEqual(oOrder.getDrinks(), None, "no drinks were entered")