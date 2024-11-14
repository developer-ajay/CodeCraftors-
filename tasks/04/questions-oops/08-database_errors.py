
"""
8. Hard: Implement a class hierarchy for a custom exception handling system.
Create a base exception class 'DatabaseError' and derived classes for specific errors:
- ConnectionError
- QueryError
- DataError
Each error should have appropriate attributes and methods to handle different database scenarios.
"""
import unittest
import math
class DatabaseError(Exception):
    pass

class ConnectionError(DatabaseError):
    pass

class QueryError(DatabaseError):
    pass

class DataError(DatabaseError):
    pass

class TestDatabaseErrors(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(ConnectionError) as context:
            raise ConnectionError("Failed to connect", host="localhost", port=5432)
        self.assertEqual(str(context.exception), "Failed to connect to localhost:5432")
        
        with self.assertRaises(QueryError) as context:
            raise QueryError("Invalid SQL", query="SELECT * FORM users")
        self.assertEqual(context.exception.get_position(), 14)

if __name__ == '__main__':
    unittest.main()