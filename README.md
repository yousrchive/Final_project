# 🚀 Final Project

## 📚 목차

1. [기획배경](#기획배경)
2. [프로젝트 기간](#프로젝트-기간)
3. [팀원 소개](#팀원-소개)
4. [기능 소개](#기능-소개)
5. [모델 설계서](#모델-설계서)
6. [API 설계서](#api-설계서)
7. [ERD](#erd)
8. [시스템 아키텍처](#시스템-아키텍처)
9. [데이터 명세서](#데이터-명세서)
10. [기술 스택](#기술-스택)
11. [결과물](#결과물)

## 🎯 기획배경

- 세대불문 여행 수요 증가
- 여행지 선정의 어려움을 겪는 사용자들을 위한 추천
- 여행 계획 수립에 어려움을 겪는 인원이 많음
- 타인의 여행 스케줄을 공유받고 자신의 여행 기록을 관리어(환경 구축, 데이터 수집 자동화)
- 여행 기간, 인원, 취향별 여행지 추천과 여행코스등을 한번에 누릴 All-In-One 서비스를 원하는 인원이 많음
- 
## ⏰ 프로젝트 기간

24년 1월 8일 ~ 24년 3월 22일

## 👥 팀원 소개

| 이름 | 역할 |
|---|---|
| 구주완(팀장) | 데이터 엔지니어(클라우드 기반 서버 구축, 데이터 수집 자동화) |
| 이슬희 | 데이터 엔지니어 (클라우드 기반 서버 구축, 데이터 수집 자동화) |
| 최상윤 | 데이터 사이언티스트(데이터 수집, 챗봇 모델 개발) |
| 김태현 | 데이터 사이언티스트(추천시스템 개발) |
| 이유정 | 데이터 사이언티스트(챗봇 모델 개발) |
| 김겨레 | 백엔드 & 프론트엔드(웹 설계 및 기능 구현) |


## 🎁 기능 소개

| 기능 | 상세 설명 |
|---|---|
| 회원 관리 | 회원가입 설문조사 / 로그인 / 로그아웃 |
| 메인페이지 | 여행지 조회 |
| 여행지 상세 정보 | 여행지 주소, 소개 등 기본정보 조회. 해당 여행지 카카오맵 마커 및 지도 표시. 해당 여행지와 비슷한 여행지 추천 |
| 마이페이지 | 사용자 기본정보, 사용자 여행지도, 프로필 사진 등록, 팔로워, 팔로잉, 여행기록 수, 여행 스타일 조회 등 |
| 여행지 추천 | 사용자 맞춤 여행지 추천, 여행지 상세 정보 조회 |
| 스케쥴러 | 여행지 장바구니, 여행지별 여행하기 좋은 시간대 추천, 여행지 스케줄러: 여행지 장바구니. 표 형식 (관광지명, 사진, 장소, 전화번호, 방문 시간 등...). 순서 결정 (가장 처음에는 최상의 순서). 각 여행지 별 여행하기 좋은 시간대 추천. 순서 결정 후, 지도에 순서대로 동선 표시. 해당 여행지 대체 여행지 추천 |
| 커뮤니티 | 동행자 구인, 스케쥴러 기반 여행기록 작성, 다른 여행 기록 조회, 장바구니 담기 등 |
| 챗봇 | ex) 제주도 1박2일 여행지 추천, 제주도 오름 추천, 테마파크같은 여행지 추천 등.. |

## 📄 모델 설계서
  ### 🎉 추천시스템

*추천 서비스 정의

유저가 4개 정도의 선호하는 관광지를 고르면 그와 유사한 관광지 몇몇을 추천해줌.
<br><br>

*모델 설계 1

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/6e35cbec-2fd4-4109-85d5-be209552698b)



관광지에 대한 여러 정보를 수집 -> columns
관광지에 대한 메타 데이터 테이블을 형성

Cold start
유저 정보나 선택 정보가 없어서 Collaborative Filtering을 적용하기 힘들다. Content-Based Filtering을 채택. 모델 설계1 은 Content-Based Filtering 중 OneHotEncoding 방식. 모델 설계2, 3은 Embeding 방식.
![image](https://github.com/PlaydataFinal/Final_project/assets/147587058/825973e0-13e1-4af1-a24c-8bcfa3087f49)
<br><br>

*모델 설계 2

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/39618555-b2cd-45a3-bb11-3f7cc04ee1a1)


단어집 논문 소개

문장 유사도와 비슷한 맥락으로 관광지들마다 태그들이 달려있다는 사실만으로 유사도를 알 수 있다고 생각함.

모델 설계1, 2는 배치 자동화를 통한 모델 업데이트
<br><br>

*모델 설계3

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/dbd0094f-5fa3-4528-a1b9-6fc28594ec00)


모델 설계 2, 3의 데이터는 성격이 다르다. 
2는 자유도 높고 주관적 특성을 담고 있으며 자유도가 높은 low-level 데이터.
3은 제주관광공사에서 도메인 지식에 따라 labeling한 정제된 데이터.




  ### 💬 챗봇

  ![001](https://github.com/PlaydataFinal/Final_project/assets/147587058/4a480aa5-5488-4923-8350-61bd02245fdb)
  ![002](https://github.com/PlaydataFinal/Final_project/assets/147587058/d5826717-4c6c-4f84-8c47-99f85b138579)
  ![003](https://github.com/PlaydataFinal/Final_project/assets/147587058/d793e093-79b9-4359-b8d4-e873a751aa48)


## 🌐 API 설계서

### 네이버 Maps API
- **기능**: 지도 표시, 주소 검색, 길 찾기 등
- **요청 URL**: `https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode`
- **요청 방식**: GET
- **요청 파라미터**: `query` (주소)
- **응답 형식**: JSON
- **에러 코드**: 401 (인증 실패), 404 (찾을 수 없음)

### 카카오 API
- **기능**: 주소 검색, 길 찾기, 키워드 검색 등
- **요청 URL**: `https://dapi.kakao.com/v2/local/search/address.json`
- **요청 방식**: GET
- **요청 파라미터**: `query` (검색어)
- **응답 형식**: JSON
- **에러 코드**: 401 (인증 실패), 404 (찾을 수 없음)

### 네이버, 카카오, 구글 소셜로그인 API
- **기능**:사용자 회원가입 및 로그인 기능
- **요청 URL**:
  - 네이버: `https://nid.naver.com/oauth2.0/authorize`
  - 카카오: `https://kauth.kakao.com/oauth/authorize`
  - 구글: `https://accounts.google.com/o/oauth2/auth`
- **요청 방식**: GET
- **요청 파라미터**: `client_id`, `redirect_uri`, `response_type`, `scope`
- **응답 형식**: JSON
- **에러 코드**: 400 (잘못된 요청), 401 (인증 실패)

### GEMINI-Pro API
- **기능**: 챗봇 기능
- **요청 URL**: `https://api.gemini.com/v1/pubticker/:symbol`
- **요청 방식**: GET
- **요청 파라미터**: `symbol` (디지털 자산 심볼)
- **응답 형식**: JSON
- **에러 코드**: 400 (잘못된 요청), 403 (권한 없음), 404 (찾을 수 없음)

### UnSplash API
- **기능**: 무료 이미지 검색 및 다운로드
- **요청 URL**: `https://api.unsplash.com/photos/random`
- **요청 방식**: GET
- **요청 파라미터**: `query` (검색어)
- **응답 형식**: JSON
- **에러 코드**: 403 (요청 초과), 404 (찾을 수 없음```


## 🗃️ ERD
만들다 말았음
![만들다 말았음](https://github.com/PlaydataFinal/Final_project/assets/149549639/5d61004e-ea21-41bd-b9d1-9996d8713ff5)

## 🏗️ 시스템 아키텍처

![시스템 아키텍처](https://github.com/PlaydataFinal/Final_project/assets/149549639/e922191b-83a9-46bd-87c3-de38fbaafb78) 

- airflow(t2.small*3): 웹스크래핑 파이썬 셀레니움으로 동작하기에 시간이 많이 걸리므로 3대의 airflow서버를 구성하여 병렬처리로 관광지, 음식점, 숙박업소에 대해 데이터 수집 및 전처리 자동화
- hadoop cluster(t2.Large*3, t2.medium*1): 대용량의 학습용 이미지 데이터를 필요할 것으로 예상되어 3대의 데이터 노드를 구성 client서버로 관리
- colab(ML): 챗봇과 추천시스템을 학습시키는데 있어서 비용이 많이 발생할 것으로 예상되어 하둡 파일을 구글 코랩에 올려서 학습 하는것을 구상중
- docker(t2.Large): 개발환경을 좀 더 원활하고 빠르게 작업하기위해 도커 환경에서 was,web, mariadb를 구축
## 📄 데이터 명세서
(내용 추후 추가)
## 💻 기술 스택

| 분류 | 항목 |
|---|---|
| FRONT-END | Kakao Map, Naver Maps, GEMINI, HTML, CSS |
| BACK-END | Django, Python, MySQL(Maria DB), Kakao,Naver,Google Login API |
| DATA | Python, MySQL(Maria DB), spark, hadoop |
| CI/CD | Docker, AWS, Airflow |
| 협업 | Slack, Git |

## 🎈 결과물

(결과물 내용)
