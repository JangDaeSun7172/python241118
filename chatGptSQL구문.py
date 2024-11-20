import sqlite3
import random

class ElectronicsDatabase:
    def __init__(self, db_name="electronics.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """Create the products table if it doesn't exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    price REAL NOT NULL
                )
            ''')

    def insert_product(self, product_name, price):
        """Insert a new product into the table."""
        with self.connection:
            self.connection.execute('''
                INSERT INTO products (product_name, price) 
                VALUES (?, ?)
            ''', (product_name, price))

    def update_product(self, product_id, product_name=None, price=None):
        """Update a product's details."""
        with self.connection:
            if product_name and price:
                self.connection.execute('''
                    UPDATE products 
                    SET product_name = ?, price = ? 
                    WHERE product_id = ?
                ''', (product_name, price, product_id))
            elif product_name:
                self.connection.execute('''
                    UPDATE products 
                    SET product_name = ? 
                    WHERE product_id = ?
                ''', (product_name, product_id))
            elif price:
                self.connection.execute('''
                    UPDATE products 
                    SET price = ? 
                    WHERE product_id = ?
                ''', (price, product_id))

    def delete_product(self, product_id):
        """Delete a product from the table."""
        with self.connection:
            self.connection.execute('''
                DELETE FROM products 
                WHERE product_id = ?
            ''', (product_id,))

    def select_products(self):
        """Retrieve all products from the table."""
        with self.connection:
            cursor = self.connection.execute('SELECT * FROM products')
            return cursor.fetchall()

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()

# 샘플 데이터 생성 및 삽입
if __name__ == "__main__":
    db = ElectronicsDatabase()

    # 샘플 데이터 생성
    product_names = [f"Product {i}" for i in range(1, 101)]
    prices = [round(random.uniform(10.0, 1000.0), 2) for _ in range(100)]

    # 데이터 삽입
    for name, price in zip(product_names, prices):
        db.insert_product(name, price)

    # 데이터 출력
    products = db.select_products()
    for product in products:
        print(product)

    # 데이터베이스 연결 닫기
    db.close_connection()
