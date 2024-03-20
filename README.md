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
- 타인의 여행 스케줄을 공유받고 자신의 여행 기록을 관리
- 여행 기간, 인원, 취향별 여행지 추천과 여행코스등을 한번에 누릴 All-In-One 서비스를 원하는 인원이 많음
## ⏰ 프로젝트 기간

24년 2월 19일 ~ 24년 3월 22일

## 👥 팀원 소개

| 이름 | 역할 |
|---|---|
| 구주완(팀장) | 데이터 엔지니어(클라우드 기반 서버 구축, 백엔드 기능 구현, 데이터 수집) |
| 이슬희 | 데이터 엔지니어 (클라우드 기반 서버 구축, 백엔드 기능 구현) |
| 최상윤 | 데이터 사이언티스트(데이터 수집, 챗봇 모델 개발, 이미지 추천시스템, 관광지 추천시스템) |
| 김태현 | 데이터 사이언티스트(이미지 추천시스템 개발) |
| 이유정 | 데이터 사이언티스트(챗봇 모델 개발) |
| 김겨레 | 백엔드 & 프론트엔드(웹 설계 및 기능 구현) |


## 🎁 기능 소개

| 기능 | 상세 설명 |
|---|---|
| 회원 관리 | 회원가입 설문조사 / 로그인 / 로그아웃 |
| 메인페이지 | 서비스 소개 및 팀원 소개 |
| 여행지 조회 및 상세 페이지 | 여행지 주소, 소개 등 기본정보 조회. 해당 여행지 카카오맵 마커 및 지도 표시. 해당 여행지와 비슷한 여행지 추천 |
| 여행지 길찾기 페이지 | 여행지 출발지, 도착지 키워드와 여러가지 교통 옵션으로 최적의 길찾기를 제공 |
| 마이페이지 | 사용자 기본정보 및 수정|
| 여행지 추천 | 인기 여행지 추천 |
| 챗봇 | ex) 액티비티 여행지 추천, 반려동물과 갈 수 있는 숙소 추천, 흑돼지 음식점 추천 등 |

## 📄 모델 설계서
  ### 🎉 추천시스템
서비스 운영 전이라 Cold start issue가 있는 상황. 유저 정보나 선택 정보가 없어서 Collaborative Filtering을 적용하기 힘들다. Content-Based Filtering을 채택.<br>

Ai Hub에서 여행 방문지, 경로 데이터를 발견하여 Collaborative Filtering이나 Hybrid 기법 적용을 고려했다. 다만 후술할 데이터 출처인 제주관광공사 홈페이지인 visitjeju의 데이터와 idx가 달라서 테이블 join 전처리의 어려움이 있었음. 여러 데이터 출처를 선택하기보단 visitjeju 홈페이지에서 크롤링해올 수 있는 데이터를 최대한 활용하기로 했다.

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/69652d49-93d6-4bfe-9008-ca439633f218)
<br>


좋아요, 별점, 리뷰 데이터와 해당 유저의 메타 데이터가 없는 상황에서 관광지 간 유사도를 얻을 수 있는 방법을 고민했다.
-> Contents에 대한 특징을 담고 있는 데이터를 백터화하여 백터 간 코사인 값을 계산하면 우리 추천시스템의 궁극적인 타겟 피쳐인 관광지 간 유사성을 도출할 수 있다고 생각했다.

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/0a474f48-b14c-42e9-8289-e8c4247a826d)

<br>

#### 태그 유사도
insight
동백과 수국, 동백과 온천 중 전자가 더 유사하다. 이것을 아는 방법은 동백과 수국 태그를 동시에 가지고 있는 관광지가 후자보다 많다는 점만으로 태그 간 유사성을 시사할 수 있다.. 태그들이 특정 관광지라는 하나의 오브젝트로 묶임으로서 라벨이 생기는 느낌.
-> 태그 클러스터링, 태그 유사도 기반 추천시스템
-> 제주관광공사 홈페이지 visitjeju에서 제공하는 관광지별 태그 데이터 크롤링

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/961dded5-5459-4b5d-a036-d200e0ad0afd)
<br>

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/93c8f042-4b67-49b9-a319-21ac42a60949)

<br>

유사도 행렬을 사용하면 유저가 한 관광지를 골랐을 때 그와 비슷한 관광지를 추천해줄 수 있다.
최종적으로 태그 유사도 추천시스템은 챗봇에 사용한 상세설명을 임베딩한 값과 함께
웹페이지 중 관광지 상세정보 페이지에서 해당 관광지와 유사한 3곳을 추천해주는 서비스로서 적용되었다.
<br>

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/ba04be0c-9b71-4321-946a-215aff36b22d)

<br>

#### 텍스트 유사도
태그 유사도 모델링에서 사용한 데이터는 제주관광공사에서 도메인 지식에 따라 labeling한 정제된 태그 데이터이다. 관광지에 대한 정성적인 정보들을 더 잘 담고 있는 자유도 높은 low-level 데이터로부터 유사도를 도출하고 싶었다.
-> 네이버 리뷰, 블로그 리뷰로부터 명사를 추출하고 어휘집을 만들어서 유의어를 처리하는 모델링을 구상했다.

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/53c8fe35-65b2-42fc-8d52-8a5ce702e921)

![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/411810bf-8751-40ac-9ad7-d9a0aa544d9f)



그러나 데이터 merge 시 난점때문에 활용하기 어려웠다. 그래서 텍스트 유사도 모델링의 데이터로  visitjeju에 관광지별 상세설명 글을 채택했다. 텍스트 유사도 모델링은 챗봇 서비스로 적용하였다.

<br>

#### 이미지 유사도
##### reference
<오늘의 집> 이미지 유사도 모델
브랜드 <오늘의 집>에서 주어진 인테리어 이미지와 비슷한 공간, 비슷한 상품을 추천해주는 서비스의 알고리즘을 참고했다. <오늘의 집>에서는 비슷한 공간을 추천해줄 때 이미지 분류 모델로 알려진 VGGNet을 사용하여 classifier 전 layer에서 이미지 백터를 얻어냈다. 이후 백터들 간 코사인 유사도를 계산하였다. 이 모델링이 정성적으로 비슷한 인테리어 스타일의 이미지를 추천해주기 위해 설계되었다는 점에서 우리가 활용하기 적합하다고 보았다.
![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/8ee0ff82-71f4-4d02-bd33-d0da43dcd9db)
<br>


다만, 이미지 유사도에 왜 지도학습을 써야 되는지?, 분류모델을 모델링에 포함하면 유사도 추출에 긍정적인 영향을 주는지?는 의문이 되었다. -> 해당 레퍼런스에서는 모던, 한옥, 네추럴 등 인테리어 카테고리를 이미지 추천에 활용하려 했지만 우리의 모델링에서는 필요없는 과정이라 생각하고 VGGNet을 개별 이미지의 feature extraction하는 과정으로만 활용했다.
<br><br>
##### 모델링
데이터셋은 visitjeju의 관광지별 대표이미지 한 장씩을 크롤링해서 활용했다. 이 1473개의 관광지별 이미지에 VGG16을 적용해 이미지 vector를 도출하고 백터를 데이터프레임의 새로운 컬럼으로 만들었다. 이 데이터프레임을 db에 저장해놓는다. 서비스 시에는 유저가 관광지 이미지 10-20개 중에서 자기 취향인 관광지 이미지 4개를 고른다. 이 4개의 목록을 받아서 선택한 관광지의 백터와 1473개의 관광지의 백터 간 유사도를 계산한 뒤 sorting하여 유사한 관광지를 도출하는 방식을 만들었다.
![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/beaaef5b-8405-4cc5-90a2-eb5c72ba6f0e)

<br>

##### 모델 학습 및 추론 결과

이미지 백터를 계산하는 함수를 정의하고 모든 image_names에 대한 백터 계산을 수행하게 하였다. 계산 시간은 40분~1시간이 걸렸는데 개발환경은 코랩 프로로 바꾸어도 계산 시간이 개선되지는 않았다. 모델 학습이 아니라 결국 추론 상황이어서 GPU 리소스의 영향력이 적용되지는 않는 것 같았다.
계산한 백터를 포함한 데이터프레임을 만들고 이를 db에 저장해놓을 것이다.<br>
![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/f0807ce9-de68-47d2-a23d-2a6f04c2451b)
<br>

계산된 백터는 25088차원이었다.<br>

서비스 개발 코드를 통해 총 4x1473 개의 계산된 유사도를 얻을 수 있다. 이를 sorting한 뒤 [4:9]로 슬라이싱하면 유저가 선택한 관광지 4개와 유사한 관광지 5개를 도출할 수 있다.<br>
![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/495f98cc-2463-477e-995c-202c542a9db3)

<br>

##### 벡터 저장 방식
1473개 이미지의 백터를 구한 뒤 db에 저장해놓는 적절한 방식을 고민했다. 기존에 구축해놓은 관계형db인 mariadb에 테이블 형식으로 저장할 수도 있겠다. 다만 용량이 비교적 크며 메모리를 많이 잡아먹을 것이고 그래서 조회에 시간이 더 걸린다는 맹점이 존재했다. 따라서 비정형 NoSQL 중 몽고db에 백터를 저장할 것을 구상했다. 테이블 형태가 아니라 백터 같은 비관계형 데이터 베이스를 지원하기 때문. 물론 결과적으로 몽고db의 저장 공간 부족으로 이미지 백터는 csv 파일로 저장해서 필요할 때 사용했다.
이 과정에서 csv파일로 저장할 때 csv파일이 백터를 리스트로 저장하지 않고 리스트에 ‘’를 양쪽에 붙인 문자열로 저장하는 이슈가 있어 문자열을 배열로 변환하는 로직을 추가해야 했다.
![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/c753f31b-84ed-4ebf-aaa2-a01fa930d7f2)


<br>


##### 모델 서빙 플로우 설계
![image](https://github.com/PlaydataFinal/Final_project/assets/145752714/299fe36f-f400-4a70-a145-48e207289051)

추천 모델 서빙 플로우. 유사도 행렬이 아니라 백터를 db에 저장해놓기로 했기 때문에 혹시 서비스 코드 실행 시 유사도 계산 및 sorting에 시간이 많이 걸리는지 관찰해야했다. 다행히 시간이 오래 걸리는 이슈는 없었다.
<br><br>


##### 추천서비스 로직 구성
이는 4x1473개의 계산된 유사도를 sorting한 것이다. row3에 대해서만 즉, 결국 한 관광지에 대한 추천만 하게 되는 문제가 있었다. 발라드, 힙합, 락 을 골랐는데 결국 발라드와 유사한 것들만 추천하게 되는 상황이었다. 편향 문제 개선을 위해 각각 추천해주는 방식으로 바꿨다.
<br><br>


##### Evaluation과 Future Work
-유저의 선택 데이터가 있었다면 협업 필터링이나 하이브리드 기법을 적용해볼 수 있었을텐데 실제 기업 비즈니스 과정이 아니어서 이를 실현하지 못 한 것이 아쉽다. 기회가 된다면 협업 필터링이나 하이브리드 기법을 구현해보고 싶다. A/B test 같은 성능 평가도 해보고 싶다.<br>
<br>
-태그 유사도, 텍스트 유사도를 동시에 고려한 추천시스템을 구성해보고 결과를 확인해보고 싶었으나 이미지 유사도에 치중하느라 달성하지 못했다.<br>
<br>
-최종적인 관광지 추천에서 특정 관광지에 편향이 생기는 이슈를 교정하였다. 다만 실제 더욱 복잡한 input 데이터를 다루는 상황에서는 더 정교한 추천 로직 구성이 요구될 것이다. 실제 기업에서 쓰는 추천 로직을 추가적으로 조사해볼 것이다.<br>
<br>
-기업 활동이 아니어서 사실상 추천시스템의 성능 테스트가 부재중이라는 점이 아쉽다.<br>
<br>
-AiHub에서 찾은 여행 경로 데이터를 가지고 관광지 간 사회연결망 분석, 관광지 클러스터링 등을 궁리했으나 서비스화하지 못했다.<br>
<br>
-추천시스템과 이미지 분류에 있어 SOTA라 할 수 있는 transformer를 고려하지 않았다. 선도적인 모델을 찾아서 적용하는 것보다 조금은 구식의 모델이라도 직접 구조와 이론을 공부하고 해당 맥락에서 참신한 플로우를 짜기 위해 치열하게 고민해보는 것이 좀 더 내실있는 과정이라고 생각했기 때문이다. 또한 이렇게 직접 설계하고 구현해낸 경험은 이후 SOTA 모델을 활용하고 그 이상을 뚫기 위한 제반이 될 것이다. 


  ### 💬 챗봇

  ![001](https://github.com/PlaydataFinal/Final_project/assets/147587058/4a480aa5-5488-4923-8350-61bd02245fdb)
  ![002](https://github.com/PlaydataFinal/Final_project/assets/147587058/d5826717-4c6c-4f84-8c47-99f85b138579)
  ![003](https://github.com/PlaydataFinal/Final_project/assets/147587058/d793e093-79b9-4359-b8d4-e873a751aa48)

-------
![004](https://github.com/PlaydataFinal/Final_project/assets/147587058/2be2787b-af39-4caf-8c34-2605d40965ed)
![005](https://github.com/PlaydataFinal/Final_project/assets/147587058/fd49b37b-e290-4637-b651-dcdd07ac4961)

## 🌐 API 설계서

### 카카오 API
- **기능**: 키워드 검색을 통한 관광지 위치 조회 및 상세페이지 이동 가능 
- **요청 URL**: `https://dapi.kakao.com/v2/maps/sdk.js?appkey=5b475d258fb5e345e3944cb9418a3f5b&libraries=services`
- **요청 방식**: GET
- **요청 파라미터**: `query` (검색어)
- **응답 형식**: JSON
- **에러 코드**: 401 (인증 실패), 404 (찾을 수 없음)

### tmap API
- **기능**:키워드를 통한 길찾기 (여러가지 옵션 포함)
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

## 🗃️ ERD
만들다 말았음
![만들다 말았음](https://github.com/PlaydataFinal/Final_project/assets/149549639/5d61004e-ea21-41bd-b9d1-9996d8713ff5)

## 🏗️ 시스템 아키텍처

![시스템 아키텍처](![image](https://github.com/PlaydataFinal/Final_project/assets/149549639/be32c290-de60-4018-b4d5-8544e846b33b)
)

- docker(t2.2xLarge): 개발환경을 좀 더 원활하고 빠르게 작업하기위해 도커 환경에서 was,web, mariadb를 구축
- nginx(web server):
  역할: 역방향 프록시 및 로드 밸런서 역할을 수행합니다.
  기능: 클라이언트로부터의 HTTP 요청을 받아 백엔드 웹 서버(web1, web2, web3)로 전달하며, 로드 밸런싱을 통해 요청을 분산합니다. 또한 정적 파일을 제공하기 위해 정적 파일 볼륨을 마운트하고 있습니다.
- web1, web2, web3 (was server):
  역할: Django 애플리케이션을 실행하는 웹 서버 역할을 합니다.
  기능: Django 애플리케이션을 실행하고 클라이언트로부터의 HTTP 요청을 처리합니다. 각각의 웹 서버는 Gunicorn을 사용하여 Django 애플리케이션을 실행하고 있습니다. 각 웹 서버는 다른 포트(8001, 8002, 8003)에서 실행됩니다.
- rabbitmq:
  역할: 메시지 큐 시스템인 RabbitMQ를 실행합니다.
  기능: 비동기 작업 처리를 위해 Celery와 함께 사용됩니다. Celery 작업 큐와 브로커로서의 역할을 합니다.
- redis:
  역할: 인메모리 데이터 구조 스토어인 Redis를 실행합니다.
  기능: 데이터 캐싱 및 세션 관리 등 다양한 용도로 사용될 수 있습니다.
- celery_worker:
  역할: Celery 워커로 비동기 작업을 처리합니다.
  기능: Celery를 사용하여 백그라운드에서 비동기 작업을 처리합니다. RabbitMQ 브로커와 통신하여 작업을 받아 처리합니다.
- celery_beat:
  역할: Celery 스케줄러로 주기적인 작업을 실행합니다.
  기능: Celery Beat를 사용하여 정기적으로 실행되어야 하는 작업을 스케줄링합니다.
- flower:
  역할: Celery 모니터링 도구인 Flower를 실행합니다.
  기능: Celery 작업 및 큐의 상태를 모니터링하고 관리할 수 있는 웹 인터페이스를 제공합니다.
## 📄 데이터 명세서

### 1. 관광지(음식점, 숙박) 기본 데이터

- **항목**: 관광지(음식점, 숙박) 기본 데이터
- **칼럼**: 이름, 별점, 태그, 주소, 전화번호, 좋아요, 찜하기, 리뷰, 방문자, 조회, SNS공유, 상세설명, 이용안내, 이미지URL, 설명 핵심 키워드
- **갯수**: 1488
- **데이터타입**:
  - 이름, 별점, 태그, 주소, 전화번호, 좋아요, 찜하기, 리뷰, 방문자, SNS공유, 상세설명, 이용안내, 이미지URL, 설명 핵심 키워드: object
  - 조회: float

### 2. 관광지 설명 데이터

- **항목**: 관광지 설명 데이터
- **칼럼**: ID, 이름, 주소, 위도, 경도, 전화번호, 이미지URL
- **갯수**: 1480
- **데이터타입**:
  - ID: int (웹페이지 구분자)
  - 이름, 주소, 위도, 경도, 전화번호, 이미지URL: object

### 3. 챗봇 데이터

- **항목**: 챗봇 데이터
- **칼럼**: 이름, 주소, 조회, 상세설명, 이용안내, 임베딩, 태그임베딩
- **갯수**: 1487
- **데이터타입**:
  - 이름, 주소, 이용안내, 상세설명: object
  - 조회: float
  - 임베딩, 태그임베딩: array

### 4. 이미지 추천 데이터

- **항목**: 이미지 추천 데이터
- **칼럼**: 이름, 이미지URL, 이미지임베딩, 관광지간 유사도
- **갯수**: 1472
- **데이터타입**:
  - 이름, 이미지URL: object
  - 이미지임베딩: array
  - 관광지간 유사도: object

### 5. 관광지별 추천 데이터

- **항목**: 관광지별 추천 데이터
- **칼럼**: ID, 이름, 태그, 조회, 임베딩, 태그임베딩, 유사관광지1, 유사관광지2, 유사관광지3, 유사관광지1의 유사도, 유사관광지2의 유사도, 유사관광지3의 유사도
- **갯수**: 1465
- **데이터타입**:
  - ID: object (웹페이지 구분자)
  - 조회: float
  - 임베딩(설명 핵심키워드의 임베딩 값), 태그 임베딩(태그 임베딩 값): array
  - 이름, 태그, 유사관광지1, 유사관광지2, 유사관광지3(각 관광지별 유사 관광지), 유사관광지1의 유사도, 유사관광지2의 유사도, 유사관광지3의 유사도(각 관광지별 유사 관광지 유사도): object

## 💻 기술 스택

| 분류 | 항목 |
|---|---|
| FRONT-END | Tmap API,KAKAO API, HTML, CSS |
| BACK-END | Django, Python, Kakao API, GEMINI-Pro API, Tmap API |
| DATA | Python, MySQL(Maria DB), MongoDB |
| CI/CD | Docker, AWS S3 |
| 협업 | Slack, Git |

## 🎈 결과물

(결과물 내용)
