#상윤쓰 부탁...

#동행자 구인 페이지 하이퍼링크 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def crawl_accompany_data(driver, detail_url):
    # 상세 페이지로 이동
    driver.get(detail_url)
    # 페이지 로딩을 기다림 (3초 기다리고 조절 가능)
    driver.implicitly_wait(3)
    # 현재 페이지의 소스 코드
    current_page_source = driver.page_source
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(current_page_source, 'html.parser')
    # 데이터를 저장할 딕셔너리 초기화
    accompany_data = {}
    # 제목 추출
    title_tag = soup.find('div', class_='sc-cda0618d-4 hytgOb')
    if title_tag:
        accompany_data['Title'] = title_tag.get_text(strip=True)
    else:
        accompany_data['Title'] = 'N/A'
    # 이미지 추출
    img_tag = soup.find('div', class_='culture_view_img').find('img')
    if img_tag:
        accompany_data['Image_URL'] = urljoin('https://www.mcst.go.kr', img_tag['src'])
    # 기타 정보 추출
    dl_elements = soup.find_all('dl')
    for dl in dl_elements:
        dt = dl.find('dt').get_text(strip=True)
        dd = dl.find('dd').get_text(strip=True)
        # 일부 정보는 특정한 전처리가 필요할 수 있음
        if dt == '개최기간':
            # 개최기간 예시로 정규화
            dd = dd.replace('.', '-')
        # 추가 정보 추출 (예시: 개최지역, 축제성격, 관련 누리집 등)
        if dt in ['개최지역', '축제성격', '관련 누리집', '축제장소', '요금', '주최/주관기관', '문의']:
            accompany_data[dt] = dd
    # 상세 내용 추출
    view_con_tag = soup.find('div', class_='view_con')
    if view_con_tag:
        accompany_data['Description'] = view_con_tag.get_text(strip=True)
    return accompany_data

# Chrome WebDriver 설정
driver = webdriver.Chrome()

# 예시 URL
url = "https://tripsoda.com/community?area=%ED%95%9C%EA%B5%AD&areaId=2&type=accompany"

# 상세 페이지 링크 가져오기
driver.get(url)
detail_links = [link.get_attribute('href') for link in driver.find_elements(By.CSS_SELECTOR, 'a.go')]

# 각 상세 페이지에서 정보 추출
accompany_data_list = []
for detail_link in detail_links:
    accompany_data = crawl_accompany_data(driver, detail_link)
    accompany_data_list.append(accompany_data)
# WebDriver 종료
driver.quit()
# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(accompany_data_list)
# 결과 출력
print(result_df)


# 예시:
# title = <p class="sc-cda0618d-4 hytgOb">내일 1박2일로 평창 발왕산 케이블카 타고 올라갈 사람 구합니다~</p>
# 날짜: <p class="sc-cda0618d-15 ibohzt">2024.01.22 - 2024.01.23 (2일)</p>
# 위치 : <p class="sc-cda0618d-15 ibohzt">동아시아, 한국, 강원도</p>
# description : <p class="sc-cda0618d-15 ibohzt">현재 혼자이고 29살 남자입니다.
# 내일 강원도 평창쪽에 발왕산 같이가실분 1명 구합니다. 강원도에 눈이 많이와서 힐링하러 가요~
# 출발은 서울 고터역이고 자차로 이동합니다</p>
# 하이퍼링크:
# 사진: <img src="https://tripsoda.s3.ap-northeast-2.amazonaws.com/prod/image/Countries/East Asia/Korea/10.webp" alt="bg" class="sc-ed5bc865-2 Jjfuv">
    
# 여행장: <p class="sc-785ac9a7-4 eNynWT">chinabom…</p>
# 여행장 나이: <p color="#9a9a9a" class="sc-b4a7fe24-1 YmsoB">20대</p>
# 여행장 성별: <p color="#9a9a9a" class="sc-b4a7fe24-2 fkbYrB">남자</p>
# 여행장 국적: <p color="#9a9a9a" class="sc-b4a7fe24-3 gbNzDD"> 한국</p>

# 1부터 끝까지.