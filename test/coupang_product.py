####################################
# 설치
# % pip install selenium BeautifulSoup4
####################################


####################################
# 모듈 import
####################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import sys

####################################
# 출력을 'xs.txt' 파일로 리다이렉트
####################################
original_stdout = sys.stdout
sys.stdout = open('xs.txt', 'w', encoding='utf-8')


####################################
# 셀레니윰 호출
####################################
# 브라우저 자동 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 브라우저 자동 꺼짐 방지 옵션
driver = webdriver.Chrome(options=chrome_options)

# 페이지 로딩이 완료될 떼까지 기다리는 코드 (3초 설정)
#driver.implicitly_wait(3)

# 사이트 접속하기
driver.get(url='https://www.coupang.com/np/categories/178456?listSize=120&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=178356&rating=0')

# 페이지가 로딩 완료될때까지 기다리기
wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')


# class name으로 찾기
#driver.find_element(By.CLASS_NAME,'gLFyf')
# tag name으로 찾기
#driver.find_element(By.TAG_NAME,'textarea')
# id로 찾기
#driver.find_element(By.ID,'APjFqb')
# XPath로 찾기
#driver.find_element(By.XPATH,'//*[@id="APjFqb"]')

#gnbAnalytics > ul.menu.shopping-menu-list
####################################
# HTML Reponse 파싱
####################################
html_data = driver.page_source

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_data, 'html.parser')

# '#gnbAnalytics > ul.menu.shopping-menu-list' 선택자로 요소 찾기
product_list = soup.select_one('#productList')

if product_list:
    # 모든 <li> 요소 찾기
    li_el_list = product_list.find_all('li', recursive=False) # recursive=False 면 바로 밑 하위 엘레먼트만 조회

    for li_el in li_el_list:
        # <a> 태그 조회
        a_el = li_el.find('a', recursive=False)
        if a_el:
            href = a_el.get('href')
            item_id = a_el.get('data-item-id')
            vendor_item_id = a_el.get('data-vendor-item-id')
            print(f"href={href} item_id={item_id} vendor_item_id={vendor_item_id}")
                                               
        # <div.name> 태그 조회           
        name_el = li_el.find('div', class_='name')
        if name_el:
            name = name_el.get_text(strip=True)
            print(f"name={name}")
            
        # <img> 태그 조회           
        img_el = li_el.find('img')
        if img_el:
            img_src = img_el.get('src')
            print(f"img_src={img_src}")    
            
        # <strong.price-value> 태그 조회       
        price_el = li_el.find('strong', class_='price-value')
        if price_el:
            price_str = price_el.get_text(strip=True)
            price = int(price_str.replace(",", ""))
            print(f"price={price}")                                        
        print("=============================================================================")    
            
else:
    print("요소를 찾을 수 없습니다.")
    
    
# 출력을 원래대로 되돌리고 파일 닫기
sys.stdout.close()
sys.stdout = original_stdout
print("출력이 'xs.txt' 파일에 저장되었습니다.")



# import mysql.connector

# ####################################
# # MySQL 데이터베이스에 연결
# ####################################
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )

# # 커서 객체 생성
# mycursor = mydb.cursor()

# # 데이터를 삽입할 SQL 쿼리
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")

# # 쿼리 실행
# mycursor.execute(sql, val)

# # 변경사항 커밋 (중요!)
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")




