import openpyxl
import random

# 샘플 제품 데이터 준비
electronic_products = [
    ("스마트폰", 800000, 1200000),
    ("노트북", 1200000, 2500000),
    ("태블릿", 400000, 800000),
    ("이어폰", 50000, 300000),
    ("스마트워치", 200000, 500000),
    ("블루투스 스피커", 80000, 250000),
    ("게이밍 모니터", 300000, 800000),
    ("키보드", 50000, 200000),
    ("마우스", 30000, 150000),
    ("외장하드", 100000, 300000)
]

# 엑셀 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active

# 헤더 추가
headers = ['제품ID', '제품명', '수량', '가격']
ws.append(headers)

# 100개의 데이터 생성 및 추가
for i in range(1, 101):
    product = random.choice(electronic_products)
    product_id = f'P{str(i).zfill(3)}'  # P001, P002 형식의 ID
    product_name = product[0]
    quantity = random.randint(1, 50)  # 1~50 사이의 수량
    price = random.randint(product[1], product[2])  # 제품별 가격 범위 내에서 랜덤
    
    ws.append([product_id, product_name, quantity, price])

# 파일 저장
wb.save('products.xlsx')
print('products.xlsx 파일이 생성되었습니다.')