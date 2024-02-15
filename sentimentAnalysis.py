import pandas as pd
from afinn import Afinn
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_analysis(file_path):
    """
    호텔 1개에 대한 감성분석 수행 및 결과값 저장
    :param file_path: hotel_en csv file path
    """
    df_hotel = pd.read_csv(file_path, encoding='utf-8-sig', encoding_errors='ignore')

    afinn_result = []
    vader_result = []

    # Afinn 분석
    afinn = Afinn()
    for i in range(0, len(df_hotel)):
        afinn_result.append(afinn.score(df_hotel.iloc[i].comment))

    # Vador 분석 (negative : score <= -0.05 / neutral : -0.05 < score < 0.05 / positive : 0.05 <= score )
    vader_analyzer = SentimentIntensityAnalyzer()
    for i in range(0, len(df_hotel)):
        vader_result.append(vader_analyzer.polarity_scores(df_hotel.iloc[i].comment)['compound'])

    df_hotel['afinn_score'] = afinn_result
    df_hotel['vader_score'] = vader_result

    print(df_hotel.head(1))

    # # 삭제할 column 리스트 정의
    # columns_to_keep = ["score", "comment", "afinn_score", "vader_score"]
    #
    # # 삭제할 column을 제외한 나머지 column들을 찾아서 삭제
    # columns_to_drop = [col for col in df_hotel.columns if col not in columns_to_keep]
    # df_hotel.drop(columns=columns_to_drop, inplace=True)

    df_hotel.to_csv(file_path, index=False)


if __name__ == '__main__':
    sentiment_analysis('hotelData_en/hotel1_en.csv')
    sentiment_analysis('hotelData_en/hotel2_en.csv')
    sentiment_analysis('hotelData_en/hotel3_en.csv')
    sentiment_analysis('hotelData_en/hotel4_en.csv')
    sentiment_analysis('hotelData_en/hotel5_en.csv')
    sentiment_analysis('hotelData_en/hotel6_en.csv')
    sentiment_analysis('hotelData_en/hotel7_en.csv')
    sentiment_analysis('hotelData_en/hotel8_en.csv')
    sentiment_analysis('hotelData_en/hotel9_en.csv')
    sentiment_analysis('hotelData_en/hotel10_en.csv')

