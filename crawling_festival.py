#https://www.mcst.go.kr/kor/s_culture/festival/festivalList.jsp

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.musinsa.com/app/styles/lists?use_yn_360=&style_type=&brand=&model=&tag_no=&max_rt=&min_rt=&display_cnt=60&list_kind=big&sort=date&page=2")
imgs = driver.find_element(By.CSS_SELECTOR, "img.style-list-thumbnail__img")
imgs.get_attribute('src')


from selenium import webdriver
import time

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome()

# 구글 지도 접속하기
driver.get("https://www.google.com/maps/")

# 검색창에 "카페" 입력하기
searchbox = driver.find_element_by_css_selector("input#searchboxinput")
searchbox.send_keys("카페")

# 검색버튼 누르기
searchbutton = driver.find_element_by_css_selector("button#searchbox-searchbutton")
searchbutton.click()

# 여러 페이지(999)에서 반복하기
for i in range(999):
    # 시간 지연
    time.sleep(3)

    # 컨테이너(가게) 데이터 수집 // div.section-result-content
    stores = driver.find_elements_by_css_selector("div.section-result-content")

    for s in stores:
        # 가게 이름 데이터 수집 // h3.section-result-title
        title = s.find_element_by_css_selector("h3.section-result-title").text

        # 평점 데이터 수집 // span.cards-rating-score
        # 평점이 없는 경우 에러 처리
        try:
            score = s.find_element_by_css_selector("span.cards-rating-score").text
        except:
            score = "평점없음"

        # 가게 주소 데이터 수집 // span.section-result-location
        addr = s.find_element_by_css_selector("span.section-result-location").text

        print(title, "/", score, "/", addr)

    # 다음페이지 버튼 클릭 하기
    # 다음페이지가 없는 경우(데이터 수집 완료) 에러 처리
    try:
        nextpage = driver.find_element_by_css_selector("button#n7lv7yjyC35__section-pagination-button-next")
        nextpage.click()
    except:
        print("데이터 수집 완료.")
        break

# 크롬창 닫기
driver.close()
출처: https://datalabbit.tistory.com/45 [간토끼 DataMining Lab:티스토리]