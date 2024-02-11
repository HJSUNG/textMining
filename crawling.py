from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

hotel_comment_url_list = [
    { "key": "1", "hotel_name": "켄싱턴리조트 제주중문", "url" : "https://www.agoda.com/ko-kr/corea-condo-jeju/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&tspTypes=7&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e" },
    { "key": "2", "hotel_name": "제주 솔라시도 펜션", "url" : "https://www.agoda.com/ko-kr/jeju-solarseado-pension/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "3", "hotel_name": "더빌라스오션 커플화이트", "url" : "https://www.agoda.com/ko-kr/the-villas-ocean-couple-white/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&tspTypes=17&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "4", "hotel_name": "골든튤립 제주 성산 호텔", "url" : "https://www.agoda.com/ko-kr/golden-tulip-jeju-seongsan-hotel/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "5", "hotel_name": "에코랜드 호텔", "url" : "https://www.agoda.com/ko-kr/h31637172/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&tspTypes=8&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "6", "hotel_name": "파르나스 호텔 제주", "url" : "https://www.agoda.com/ko-kr/hyatt-regency-jeju_2/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&tspTypes=8&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "7", "hotel_name": "켄싱턴리조트 서귀포", "url" : "https://www.agoda.com/ko-kr/kensington-resort-seogwipo/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&tspTypes=-1&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "8", "hotel_name": "서귀포 칼 호텔", "url" : "https://www.agoda.com/ko-kr/seogwipo-kal-hotel/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&tspTypes=-1&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "9", "hotel_name": "스위트 호텔 제주", "url" : "https://www.agoda.com/ko-kr/the-suite-hotel-jeju/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
    { "key": "10", "hotel_name": "랜딩관 제주신화월드 호텔 앤 리조트", "url" : "https://www.agoda.com/ko-kr/jeju-shinhwa-world-landing-resort/hotel/jeju-island-kr.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891463&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2024-02-19&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=KRW&isFreeOccSearch=false&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&isCityHaveAsq=false&los=1&searchrequestid=5a3e18aa-8c2b-4285-819d-7b991627875e&ds=KdYBaFY5ylI3eczf" },
]

max_review_count = 500


def crawl_comments():
    """
    호텔 별 리뷰점소 + 리뷰 Text를 크롤링해서, csv 파일로 저장
    """
    for url_object in hotel_comment_url_list:
        # 스크롤 여부 확인용
        scroll_by = False

        print(url_object["hotel_name"])

        # 리뷰 건별 점수
        hotel_review_score_list = []
        # 리뷰 text
        hotel_review_comment_list = []

        driver = webdriver.Chrome()

        hotel_url = url_object["url"]

        driver.get(hotel_url);

        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')

        # 호텔 리뷰 총 갯수
        temp_hotel_total_review_count_element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span.Review__SummaryContainer--left.Review__SummaryContainer__Text'))
        )

        temp_hotel_total_review_count = soup.find('span', {
            'class': 'Review__SummaryContainer--left Review__SummaryContainer__Text'}).text

        hotel_total_review_count = int(
            temp_hotel_total_review_count.replace('[100% 실제 이용후기 ', '').replace('건 보기 중]', '').replace(',', ''))

        # 호텔 리뷰 중, 최대 500건만 사용
        hotel_total_review_count = max_review_count if int(hotel_total_review_count) > max_review_count else int(
            hotel_total_review_count)
        print(hotel_total_review_count)

        # 페이지 내 리뷰 건별 점수
        temp_hotel_review_score_list = soup.select('div.Review-comment-leftScore')
        # 페이지 내 리뷰 text
        temp_hotel_review_comment_list = soup.select('p.Review-comment-bodyText')

        # 해당 페이지에서 크롤링한 리뷰 점수, 리뷰 내용을 list 에 추가
        for score in temp_hotel_review_score_list:
            hotel_review_score_list.append(score.text)

        for comment in temp_hotel_review_comment_list:
            hotel_review_comment_list.append(comment.text.replace(",", " "))

        # max_review_count 보다 review 수가 적은 경우
        while len(hotel_review_score_list) < hotel_total_review_count:
            print(len(hotel_review_score_list))
            print(len(hotel_review_comment_list))
            print("==========")
            # 다음 리뷰 (>) 버튼 icon 클릭
            icon = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.ficon.ficon-24.ficon-carrouselarrow-right'))
            )

            icon.click()

            # Overlay component 회피 위해, 300px scrollDown 수행
            if not scroll_by:
                driver.execute_script('window.scrollBy(0,300)')
                scroll_by = True

            # icon 클릭 수, 데이터 load 될 때까지 대기
            WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.Review-comment-bodyText'))
            )

            html1 = driver.page_source
            soup = BeautifulSoup(html1, 'html.parser')

            # 페이지 내 리뷰 건별 점수
            temp_hotel_review_score_list = soup.select('div.Review-comment-leftScore')
            # 페이지 내 리뷰 text
            temp_hotel_review_comment_list = soup.select('p.Review-comment-bodyText')

            # 해당 페이지에서 크롤링한 리뷰 점수, 리뷰 내용을 list 에 추가
            for score in temp_hotel_review_score_list:
                hotel_review_score_list.append(score.text)

            for comment in temp_hotel_review_comment_list:
                hotel_review_comment_list.append(comment.text.replace(",", " "))

        # hotel_review_score_list, hotel_review_comment_list dataFrame 으로 묶어 csv로 저장
        print(len(hotel_review_score_list))
        print(len(hotel_review_comment_list))
        hotel_review_dict = {"score": hotel_review_score_list, "comment": hotel_review_comment_list}

        df = pd.DataFrame(hotel_review_dict)

        df.to_csv('hotelData/hotel' + url_object['key'] + '.csv', index=False, encoding='utf-8-sig')

        driver.quit()

    print("End Of crawl_comments()")


if (__name__ == "__main__"):
    crawl_comments()
