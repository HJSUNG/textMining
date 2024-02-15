import pandas as pd
from afinn import Afinn
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

import re

import frequencyAnalysis

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

    stop_words = set(stopwords.words('english'))

    # comment에서 줄바꿈 문자 제거
    for index, row in df_hotel.iterrows():
        df_hotel.at[index, 'comment'] = row['comment'].replace('\n', ' ')

    # Vader Score 기준 분류
    df_hotel_positive = df_hotel[df_hotel['vader_score'] >= 0.05]
    df_hotel_negative = df_hotel[df_hotel['vader_score'] <= -0.05]

    # 각 DataFrame을 list로 변경
    list_hotel = df_hotel.to_dict('records')
    list_hotel_positive = df_hotel_positive.to_dict("records")
    list_hotel_negative = df_hotel_negative.to_dict("records")

    # comment를 하나의 string으로 join
    comment_string = ' '.join(row['comment'] for row in list_hotel)
    comment_string_positive = ' '.join(row['comment'] for row in list_hotel_positive)
    comment_string_negative = ' '.join(row['comment'] for row in list_hotel_negative)

    # 영문자를 제외하고 전체 제거
    comment_string = re.sub('[^a-zA-Z]', ' ', comment_string)
    comment_string_positive = re.sub('[^a-zA-Z]', ' ', comment_string_positive)
    comment_string_negative = re.sub('[^a-zA-Z]', ' ', comment_string_negative)

    # 소문자로 변환
    comment_string = comment_string.lower()
    comment_string_positive = comment_string_positive.lower()
    comment_string_negative = comment_string_negative.lower()

    # 단어 단위 list로 split
    comment_word_list = comment_string.split(' ')
    comment_word_list_positive = comment_string_positive.split(' ')
    comment_word_list_negative = comment_string_negative.split(' ')

    # stopwords 제거
    comment_word_list = [w for w in comment_word_list if not w in stop_words]
    comment_word_list_positive = [w for w in comment_word_list_positive if not w in stop_words]
    comment_word_list_negative = [w for w in comment_word_list_negative if not w in stop_words]

    # 빈칸 제거
    comment_word_list = [w for w in comment_word_list if w != '']
    comment_word_list_positive = [w for w in comment_word_list_positive if w != '']
    comment_word_list_negative = [w for w in comment_word_list_negative if w != '']

    # 2글자 이상 단어만 추출
    comment_word_list = [word for word in comment_word_list if len(word) >= 2]
    comment_word_list_positive = [word for word in comment_word_list_positive if len(word) >= 2]
    comment_word_list_negative = [word for word in comment_word_list_negative if len(word) >= 2]

    return [comment_word_list, comment_word_list_positive, comment_word_list_negative]


if __name__ == '__main__':
    analysis_result = sentiment_analysis('hotelData_en/hotel1_en.csv')
    frequencyAnalysis.draw_frequency_graph(analysis_result[1], "Positive Comment")
    frequencyAnalysis.draw_frequency_graph(analysis_result[2], "Negative Comment")
    frequencyAnalysis.draw_word_cloud(analysis_result[1], "Positive Comment")
    frequencyAnalysis.draw_word_cloud(analysis_result[2], "Negative Comment")

    # sentiment_analysis('hotelData_en/hotel2_en.csv')
    # sentiment_analysis('hotelData_en/hotel3_en.csv')
    # sentiment_analysis('hotelData_en/hotel4_en.csv')
    # sentiment_analysis('hotelData_en/hotel5_en.csv')
    # sentiment_analysis('hotelData_en/hotel6_en.csv')
    # sentiment_analysis('hotelData_en/hotel7_en.csv')
    # sentiment_analysis('hotelData_en/hotel8_en.csv')
    # sentiment_analysis('hotelData_en/hotel9_en.csv')
    # sentiment_analysis('hotelData_en/hotel10_en.csv')

