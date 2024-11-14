
"""
9. Hard: Create a metaclass 'Singleton' that ensures only one instance of a class is created.
Then create a class 'DatabaseConnection' using this metaclass.
The DatabaseConnection should have methods:
- connect()
- disconnect()
- execute_query(query)
"""
import unittest
import math
class Singleton(type):
    pass

class DatabaseConnection(metaclass=Singleton):
    pass

class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        self.assertIs(db1, db2)
        
        self.assertTrue(db1.connect())
        self.assertEqual(db1.execute_query("SELECT * FROM users"), "Query executed")
        self.assertTrue(db1.disconnect())

if __name__ == "__main__":
    unittest.main()