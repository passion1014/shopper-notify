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
driver.get(url='https://www.coupang.com/')

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
menu_list = soup.select_one('#gnbAnalytics > ul.menu.shopping-menu-list')

if menu_list:
    # 모든 <li> 요소 찾기
    li_elements = menu_list.find_all('li', recursive=False) # recursive=False 면 바로 밑 하위 엘레먼트만 조회

    for li in li_elements:
        # depth1 텍스트 추출 (li 바로 아래의 첫 번째 <a> 태그)
        depth1_text = li.find('a', recursive=False)
        if depth1_text:
            print("Depth 1:", depth1_text.get_text(strip=True))

            # depth2 텍스트 추출
            depth2_elements = li.find_all('li', class_='second-depth-list')
            for depth2 in depth2_elements:
                depth2_text = depth2.find('a')
                if depth2_text:
                    print("  Depth 2:", depth2_text.get_text(strip=True))

                    # depth3 텍스트 추출
                    depth3_elements = depth2.find_all('li')
                    for depth3 in depth3_elements:
                        depth3_text = depth3.find('a')
                        if depth3_text:
                            print("    Depth 3:", depth3_text.get_text(strip=True))

            print()  # 각 depth1 요소 사이에 빈 줄 추가
else:
    print("요소를 찾을 수 없습니다.")
    
    
# 출력을 원래대로 되돌리고 파일 닫기
sys.stdout.close()
sys.stdout = original_stdout
print("출력이 'xs.txt' 파일에 저장되었습니다.")



import mysql.connector

####################################
# MySQL 데이터베이스에 연결
####################################
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# 커서 객체 생성
mycursor = mydb.cursor()

# 데이터를 삽입할 SQL 쿼리
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

# 쿼리 실행
mycursor.execute(sql, val)

# 변경사항 커밋 (중요!)
mydb.commit()

print(mycursor.rowcount, "record inserted.")




