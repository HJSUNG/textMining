import os
import pandas as pd
from collections import Counter
from wordcloud import WordCloud

import re
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = 'C:/Windows/Fonts/HMFMMUEX.TTC'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 긍정적 리뷰, 부정적 리뷰 기준 점수
positive_criteria = 9  # 점 이상
negative_criteria = 5  # 점 미만


def analyze_dataframe(df_hotel):
    """
    입력받은 호텔 comment dataframe 빈도 분석
    :param df_hotel: comment dataframe
    :return: [comment_word_list, comment_word_list_positive, comment_word_list_negative]
    """
    # comment에서 줄바꿈 문자 제거
    for index, row in df_hotel.iterrows():
        df_hotel.at[index, 'comment'] = row['comment'].replace('\n', ' ')

    # 9점 이상 : 호텔의 장점 or 강점 / 7점 미만 : 호텔의 단점 or 불만사항
    df_hotel_positive = df_hotel[df_hotel['score'] >= positive_criteria]
    df_hotel_negative = df_hotel[df_hotel['score'] < negative_criteria]

    # 각 DataFrame을 list로 변경
    list_hotel = df_hotel.to_dict('records')
    list_hotel_positive = df_hotel_positive.to_dict("records")
    list_hotel_negative = df_hotel_negative.to_dict("records")

    # comment를 하나의 string으로 join
    comment_string = ' '.join(row['comment'] for row in list_hotel)
    comment_string_positive = ' '.join(row['comment'] for row in list_hotel_positive)
    comment_string_negative = ' '.join(row['comment'] for row in list_hotel_negative)

    # 영문자, 특수문자 제거
    comment_string = re.sub('[a-zA-Z!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]', '', comment_string)
    comment_string_positive = re.sub('[a-zA-Z!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]', '', comment_string_positive)
    comment_string_negative = re.sub('[a-zA-Z!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]', '', comment_string_negative)

    # 단어 단위 list로 split
    comment_word_list = comment_string.split(' ')
    comment_word_list_positive = comment_string_positive.split(' ')
    comment_word_list_negative = comment_string_negative.split(' ')

    # 2글자 이상 단어만 추출
    comment_word_list = [word for word in comment_word_list if len(word) >= 2]
    comment_word_list_positive = [word for word in comment_word_list_positive if len(word) >= 2]
    comment_word_list_negative = [word for word in comment_word_list_negative if len(word) >= 2]

    return [comment_word_list, comment_word_list_positive, comment_word_list_negative]


def draw_frequency_graph(word_list, title='전체'):
    """
    word_list를 받아서, pyplot 빈도 그래프 생성
    :param word_list: word_list
    :param title: plt.title 명
    """
    x, y = [], []
    for word, count in Counter(word_list).most_common(20):
        x.append(word)
        y.append(count)

    colors = sns.color_palette("pastel", len(x))

    plt.figure(figsize=(10, 10))
    plt.title(title)
    ax = sns.barplot(x=y, y=x, palette=colors)
    ax.set(xlabel='빈도', ylabel='단어')

    plt.show()


def draw_word_cloud(word_list, title=''):
    """
    word_list를 받아서, wordCloud 생성
    :param word_list: word_list
    :param title: plt.title 명
    """
    wordcloud = WordCloud(font_path=font_path).generate(' '.join(word_list))
    plt.title(title)
    plt.axis("off")
    plt.imshow(wordcloud, interpolation='bilinear')  # 이미지를 출력
    plt.show()
    wordcloud.to_array().shape


def analyze_single_hotel(file_path):
    """
    호텔 1개 comment에 대한 빈도분석
    """
    df_hotel = pd.read_csv(file_path)
    analysis_result = analyze_dataframe(df_hotel)

    draw_frequency_graph(analysis_result[0], '전체 comment')
    draw_frequency_graph(analysis_result[1], '긍정 comment')
    draw_frequency_graph(analysis_result[2], '부정 comment')
    draw_word_cloud(analysis_result[0], '전체 comment')
    draw_word_cloud(analysis_result[1], '긍정 comment')
    draw_word_cloud(analysis_result[2], '부정 comment')


def analyze_total_hotel():
    """
    호텔 전체 comment에 대한 빈도분석
    """
    df_hotel = pd.DataFrame(columns=['score', 'comment'])

    # hotelData/ 하위의 전체 csv 파일을 대상으로 통합 df 생성
    for file_name in os.listdir('hotelData'):
        if (file_name.endswith('.csv')):
            file_path = 'hotelData/' + file_name
            temp_df_hotel = pd.read_csv(file_path)
            df_hotel = pd.concat([df_hotel, temp_df_hotel])

    analysis_result = analyze_dataframe(df_hotel)

    draw_frequency_graph(analysis_result[0], '전체 comment')
    draw_frequency_graph(analysis_result[1], '긍정 comment')
    draw_frequency_graph(analysis_result[2], '부정 comment')
    draw_word_cloud(analysis_result[0], '전체 comment')
    draw_word_cloud(analysis_result[1], '긍정 comment')
    draw_word_cloud(analysis_result[2], '부정 comment')


if __name__ == '__main__':
    analyze_single_hotel('hotelData/hotel1.csv')
    # analyze_total_hotel()
