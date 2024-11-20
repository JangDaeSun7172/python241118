import sqlite3
import random

class ElectronicsDatabase:
    """
    SQLite를 사용하여 전자제품 데이터를 관리하는 클래스.

    속성:
        db_name (str): SQLite 데이터베이스 파일 이름.
        conn (sqlite3.Connection): 데이터베이스 연결 객체.
        cursor (sqlite3.Cursor): 데이터베이스 작업에 사용되는 커서 객체.
    """

    def __init__(self, db_name="electronics.db"):
        """
        클래스 초기화 및 데이터베이스 연결 생성.

        Args:
            db_name (str, optional): 데이터베이스 파일 이름. 기본값은 "electronics.db".
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        전자제품 데이터를 저장할 테이블을 생성.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS electronics (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                price INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def insert_product(self, product_id, product_name, price):
        """
        새 전자제품 데이터를 삽입.

        Args:
            product_id (int): 제품 ID.
            product_name (str): 제품명.
            price (int): 제품 가격.
        """
        self.cursor.execute("""
            INSERT INTO electronics (product_id, product_name, price)
            VALUES (?, ?, ?)
        """, (product_id, product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name=None, price=None):
        """
        특정 제품의 정보를 업데이트.

        Args:
            product_id (int): 업데이트할 제품 ID.
            product_name (str, optional): 업데이트할 새 제품명.
            price (int, optional): 업데이트할 새 가격.
        """
        query = "UPDATE electronics SET "
        params = []
        if product_name:
            query += "product_name = ?, "
            params.append(product_name)
        if price is not None:
            query += "price = ?, "
            params.append(price)
        query = query.rstrip(", ")  # 마지막 쉼표 제거
        query += " WHERE product_id = ?"
        params.append(product_id)

        self.cursor.execute(query, params)
        self.conn.commit()

    def delete_product(self, product_id):
        """
        특정 제품 데이터를 삭제.

        Args:
            product_id (int): 삭제할 제품 ID.
        """
        self.cursor.execute("DELETE FROM electronics WHERE product_id = ?", (product_id,))
        self.conn.commit()

    def select_all_products(self):
        """
        모든 전자제품 데이터를 조회.

        Returns:
            list: 전자제품 데이터 리스트. 각 항목은 (product_id, product_name, price) 형식의 튜플.
        """
        self.cursor.execute("SELECT * FROM electronics")
        return self.cursor.fetchall()

    def populate_sample_data(self, count=100):
        """
        임의의 샘플 데이터를 삽입.

        Args:
            count (int, optional): 생성할 샘플 데이터의 개수. 기본값은 100.
        """
        for i in range(1, count + 1):
            product_name = f"제품{i}"
            price = random.randint(1000, 50000)  # 1000원 ~ 50000원 사이의 임의 가격
            self.insert_product(i, product_name, price)

    def close(self):
        """
        데이터베이스 연결을 종료.
        """
        self.conn.close()


# 실행 예제
if __name__ == "__main__":
    # 데이터베이스 초기화
    db = ElectronicsDatabase()

    # 샘플 데이터 삽입
    db.populate_sample_data()

    # 모든 데이터 조회
    all_products = db.select_all_products()
    for product in all_products[:10]:  # 처음 10개 데이터 출력
        print(product)

    # 제품 수정
    db.update_product(1, product_name="수정된제품", price=99999)

    # 수정된 데이터 확인
    print("\n수정된 데이터:")
    print(db.select_all_products()[0])

    # 제품 삭제
    db.delete_product(2)

    # 삭제 후 데이터 확인
    print("\n삭제 후 데이터:")
    print(db.select_all_products()[:10])

    # 데이터베이스 연결 종료
    db.close()
