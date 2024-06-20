
def connectToNewCategory(a_href_el, insertDataList):
    # 새로운 URL 생성
    new_url = f"http://www.coupang.com{a_href_el}"

    # 새로운 페이지로 이동
    driver.get(new_url)

    # 페이지가 로딩 완료될 때까지 기다리기
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    ############################################################################

    # '#gnbAnalytics > ul.menu.shopping-menu-list' 선택자로 요소 찾기
    menu_list = soup.select_one('#searchCategoryComponent > ul.search-option-items')

    if menu_list:
        # 모든 <li> 요소 찾기
        depth4_li_el_list = menu_list.find_all('li', recursive=False) # recursive=False 면 바로 밑 하위 엘레먼트만 조회
        for depth4_li_el in depth4_li_el_list:
            # depth4 텍스트 추출 (li 바로 아래의 첫 번째 <a> 태그)
            a_el = depth4_li_el.find('a', recursive=False)
            if a_el:
                a_href_el = a_el.get('href')

                depth4_category_id = 'None'
                if len(a_href_el.split('/')) > 4:                
                    depth4_category_id = a_href_el.split('/')[4]            

                text = a_el.get_text(strip=True) #카테고리명

                insertDataList.append({
                    'category_id': depth4_category_id,
                    'depth': 4,
                    'text': text,
                    'parent_id': None #TODO: 일단 none으로
                })
                
                print("         Depth 4:", text, " categoryid=", depth4_category_id)

                # depth5 텍스트 추출
                #depth2_li_el_list = depth4_li_el.find_all('li', class_='second-depth-list')
                depth5_li_el_list = depth4_li_el.select('ul > li')
                for depth5_li_el in depth5_li_el_list:
                    a_el = depth5_li_el.find('a')
                    if a_el:
                        a_href_el = a_el.get('href')

                        depth5_category_id = 'None'
                        if len(a_href_el.split('/')) > 4:                
                            depth5_category_id = a_href_el.split('/')[4]            
                        text = a_el.get_text(strip=True) #카테고리명

                        insertDataList.append({
                            'category_id': depth5_category_id,
                            'depth': 5,
                            'text': text,
                            'parent_id': depth4_category_id
                        })

                        print("             Depth 5:", text, " categoryid=", depth5_category_id)

                        # depth6 텍스트 추출
                        depth6_li_el_list = depth5_li_el.find_all('li')                        
                        for depth6_li_el in depth6_li_el_list:
                            a_el = depth6_li_el.find('a')
                            if a_el:                            
                                a_href_el = a_el.get('href')

                                depth6_category_id = 'None'
                                if len(a_href_el.split('/')) > 4:                
                                    depth6_category_id = a_href_el.split('/')[4]
                                text = a_el.get_text(strip=True) #카테고리명

                                insertDataList.append({
                                    'category_id': depth6_category_id,
                                    'depth': 6,
                                    'text': text,
                                    'parent_id': depth5_category_id
                                })
                                print("             Depth 6:", text, " categoryid=", depth6_category_id)



####################################
# 패키지 설치
####################################
# conda create -n crawling python=3.11
# conda activate crawling
# pip install selenium BeautifulSoup4 mysql-connector-python

####################################
# 모듈 import
####################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import sys
import random
import time



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
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

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



insertDataList = [] # DB 입력될 데이터 리스트

# '#gnbAnalytics > ul.menu.shopping-menu-list' 선택자로 요소 찾기
menu_list = soup.select_one('#gnbAnalytics > ul.menu.shopping-menu-list')

if menu_list:
    # 모든 <li> 요소 찾기
    depth1_li_el_list = menu_list.find_all('li', recursive=False) # recursive=False 면 바로 밑 하위 엘레먼트만 조회
    for depth1_li_el in depth1_li_el_list:
        # depth1 텍스트 추출 (li 바로 아래의 첫 번째 <a> 태그)
        a_el = depth1_li_el.find('a', recursive=False)
        if a_el:
            a_href_el = a_el.get('href')

            depth1_category_id = 'None'
            if len(a_href_el.split('/')) > 3:                
                depth1_category_id = a_href_el.split('/')[3]            

            text = a_el.get_text(strip=True) #카테고리명

            insertDataList.append({
                'category_id': depth1_category_id,
                'depth': 1,
                'text': text,
                'parent_id': None
            })

            print("Depth 1:", text, " categoryid=", depth1_category_id)

            # depth2 텍스트 추출
            depth2_li_el_list = depth1_li_el.find_all('li', class_='second-depth-list')
            for depth2_li_el in depth2_li_el_list:
                a_el = depth2_li_el.find('a')
                if a_el:
                    a_href_el = a_el.get('href')

                    depth2_category_id = 'None'
                    if len(a_href_el.split('/')) > 3:                
                        depth2_category_id = a_href_el.split('/')[3]            
                    text = a_el.get_text(strip=True) #카테고리명

                    insertDataList.append({
                        'category_id': depth2_category_id,
                        'depth': 2,
                        'text': text,
                        'parent_id': depth1_category_id
                    })

                    print("  Depth 2:", text, " categoryid=", depth2_category_id)

                    # depth3 텍스트 추출
                    depth3_li_el_list = depth2_li_el.find_all('li')

                    for index, depth3_li_el in enumerate(depth3_li_el_list):
                    #for depth3_li_el in depth3_li_el_list:
                        a_el = depth3_li_el.find('a')
                        if a_el:                            
                            a_href_el = a_el.get('href')

                            depth3_category_id = 'None'
                            if len(a_href_el.split('/')) > 3:                
                                depth3_category_id = a_href_el.split('/')[3]
                            text = a_el.get_text(strip=True) #카테고리명

                            insertDataList.append({
                                'category_id': depth3_category_id,
                                'depth': 3,
                                'text': text,
                                'parent_id': depth2_category_id
                            })
                            print("    Depth 3:", text, " categoryid=", depth2_category_id)

                            # depth 4이상 팀험
                            if len(depth3_li_el_list)-1 == index: #마지막 loop
                                connectToNewCategory(a_href_el, insertDataList)                                                                
                                delay = random.uniform(4, 10)
                                time.sleep(delay)
                                
            print()  # 각 depth1 요소 사이에 빈 줄 추가
else:
    print("요소를 찾을 수 없습니다.")
    

# 출력을 원래대로 되돌리고 파일 닫기
sys.stdout.close()
sys.stdout = original_stdout
print("출력이 'xs.txt' 파일에 저장되었습니다.")

####################################
# MySQL 데이터베이스에 연결
####################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="coupang",
  password="coupang!",
  database="coupangdb"
)

# 커서 객체 생성
mycursor = mydb.cursor()


####################################
# List 데이터 입력
####################################

# 데이터를 삽입할 SQL 쿼리
sql = "INSERT INTO category (category_id, depth, text, parent_id) VALUES (%s, %s, %s, %s)"

for data in insertDataList:
    values = (data['category_id'], data['depth'], data['text'], data['parent_id'])
    mycursor.execute(sql, values)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

