import unittest
from scripts.database import create_table, insert_transaction, fetch_transactions

class TestDatabase(unittest.TestCase):
    def test_insert_and_fetch(self):
        create_table()
        insert_transaction("Test User", 99.99)
        data = fetch_transactions()
        self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    unittest.main()
