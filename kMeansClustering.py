import numpy as np
import pandas as pd
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import frequencyAnalysis


def k_means_clustering_analysis(file_path, k):
    """
    호텔 1개에 대한 k_means_analysis 및 csv 파일로 저장
    :param file_path: hotel_en csv file path
    :param k: Number of clusters
    """
    df_hotel = pd.read_csv(file_path, engine="python", encoding='utf-8-sig', encoding_errors='ignore')
    print(df_hotel.head(3))

    df_hotel['comment'] = df_hotel['comment'].fillna('')
    print(df_hotel['comment'].isnull().sum())

    for row1 in df_hotel['comment']:
        row1 = re.sub('[^a-zA-z]', ' ', row1)
        row1 = row1.lower()

    comment = df_hotel['comment']
    print(comment)

    # TF-IDF 만들기
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # overview에 대해서 tf-idf 수행
    tfidf_matrix = tfidf_vectorizer.fit_transform(comment)
    print(tfidf_matrix.shape)  # 행(영화 개수) X 열(단어 개수)
    terms = tfidf_vectorizer.get_feature_names_out()

    km = KMeans(n_clusters=k)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()

    films = {'comment': comment, 'cluster': clusters}
    frame = pd.DataFrame(films)
    frame['cluster'].value_counts()
    print(frame.head(5))

    df_hotel.to_csv(file_path, index=False)

    stop_words = set(stopwords.words('english'))

    # comment에서 줄바꿈 문자 제거
    for index, row in df_hotel.iterrows():
        df_hotel.at[index, 'comment'] = row['comment'].replace('\n', ' ')

    # Cluster 별 분류
    df_hotel_cluster_0 = df_hotel[df_hotel['cluster'] == 0]
    df_hotel_cluster_1 = df_hotel[df_hotel['cluster'] == 1]
    df_hotel_cluster_2 = df_hotel[df_hotel['cluster'] == 2]
    df_hotel_cluster_3 = df_hotel[df_hotel['cluster'] == 3]
    df_hotel_cluster_4 = df_hotel[df_hotel['cluster'] == 4]
    df_hotel_cluster_5 = df_hotel[df_hotel['cluster'] == 5]
    df_hotel_cluster_6 = df_hotel[df_hotel['cluster'] == 6]
    df_hotel_cluster_7 = df_hotel[df_hotel['cluster'] == 7]
    df_hotel_cluster_8 = df_hotel[df_hotel['cluster'] == 8]
    df_hotel_cluster_9 = df_hotel[df_hotel['cluster'] == 9]

    # 각 DataFrame을 list로 변경
    list_hotel = df_hotel.to_dict('records')
    list_hotel_cluster_0 = df_hotel_cluster_0.to_dict("records")
    list_hotel_cluster_1 = df_hotel_cluster_1.to_dict("records")
    list_hotel_cluster_2 = df_hotel_cluster_2.to_dict("records")
    list_hotel_cluster_3 = df_hotel_cluster_3.to_dict("records")
    list_hotel_cluster_4 = df_hotel_cluster_4.to_dict("records")
    list_hotel_cluster_5 = df_hotel_cluster_5.to_dict("records")
    list_hotel_cluster_6 = df_hotel_cluster_6.to_dict("records")
    list_hotel_cluster_7 = df_hotel_cluster_7.to_dict("records")
    list_hotel_cluster_8 = df_hotel_cluster_8.to_dict("records")
    list_hotel_cluster_9 = df_hotel_cluster_9.to_dict("records")

    # comment를 하나의 string으로 join
    comment_string = ' '.join(row['comment'] for row in list_hotel)
    comment_string_cluster_0 = ' '.join(row['comment'] for row in list_hotel_cluster_0)
    comment_string_cluster_1 = ' '.join(row['comment'] for row in list_hotel_cluster_1)
    comment_string_cluster_2 = ' '.join(row['comment'] for row in list_hotel_cluster_2)
    comment_string_cluster_3 = ' '.join(row['comment'] for row in list_hotel_cluster_3)
    comment_string_cluster_4 = ' '.join(row['comment'] for row in list_hotel_cluster_4)
    comment_string_cluster_5 = ' '.join(row['comment'] for row in list_hotel_cluster_5)
    comment_string_cluster_6 = ' '.join(row['comment'] for row in list_hotel_cluster_6)
    comment_string_cluster_7 = ' '.join(row['comment'] for row in list_hotel_cluster_7)
    comment_string_cluster_8 = ' '.join(row['comment'] for row in list_hotel_cluster_7)
    comment_string_cluster_9 = ' '.join(row['comment'] for row in list_hotel_cluster_8)

    # 영문자를 제외하고 전체 제거
    comment_string = re.sub('[^a-zA-Z]', ' ', comment_string)
    comment_string_cluster_0 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_0)
    comment_string_cluster_1 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_1)
    comment_string_cluster_2 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_2)
    comment_string_cluster_3 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_3)
    comment_string_cluster_4 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_4)
    comment_string_cluster_5 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_5)
    comment_string_cluster_6 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_6)
    comment_string_cluster_7 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_7)
    comment_string_cluster_8 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_8)
    comment_string_cluster_9 = re.sub('[^a-zA-Z]', ' ', comment_string_cluster_9)

    # 소문자로 변환
    comment_string = comment_string.lower()
    comment_string_cluster_0 = comment_string_cluster_0.lower()
    comment_string_cluster_1 = comment_string_cluster_1.lower()
    comment_string_cluster_2 = comment_string_cluster_2.lower()
    comment_string_cluster_3 = comment_string_cluster_3.lower()
    comment_string_cluster_4 = comment_string_cluster_4.lower()
    comment_string_cluster_5 = comment_string_cluster_5.lower()
    comment_string_cluster_6 = comment_string_cluster_6.lower()
    comment_string_cluster_7 = comment_string_cluster_7.lower()
    comment_string_cluster_8 = comment_string_cluster_8.lower()
    comment_string_cluster_9 = comment_string_cluster_9.lower()

    # 단어 단위 list로 split
    comment_word_list = comment_string.split(' ')
    comment_word_list_cluster_0 = comment_string_cluster_0.split(' ')
    comment_word_list_cluster_1 = comment_string_cluster_1.split(' ')
    comment_word_list_cluster_2 = comment_string_cluster_2.split(' ')
    comment_word_list_cluster_3 = comment_string_cluster_3.split(' ')
    comment_word_list_cluster_4 = comment_string_cluster_4.split(' ')
    comment_word_list_cluster_5 = comment_string_cluster_5.split(' ')
    comment_word_list_cluster_6 = comment_string_cluster_6.split(' ')
    comment_word_list_cluster_7 = comment_string_cluster_7.split(' ')
    comment_word_list_cluster_8 = comment_string_cluster_8.split(' ')
    comment_word_list_cluster_9 = comment_string_cluster_9.split(' ')

    # stopwords 제거
    comment_word_list = [w for w in comment_word_list if not w in stop_words]
    comment_word_list_cluster_0 = [w for w in comment_word_list_cluster_0 if not w in stop_words]
    comment_word_list_cluster_1 = [w for w in comment_word_list_cluster_1 if not w in stop_words]
    comment_word_list_cluster_2 = [w for w in comment_word_list_cluster_2 if not w in stop_words]
    comment_word_list_cluster_3 = [w for w in comment_word_list_cluster_3 if not w in stop_words]
    comment_word_list_cluster_4 = [w for w in comment_word_list_cluster_4 if not w in stop_words]
    comment_word_list_cluster_5 = [w for w in comment_word_list_cluster_5 if not w in stop_words]
    comment_word_list_cluster_6 = [w for w in comment_word_list_cluster_6 if not w in stop_words]
    comment_word_list_cluster_7 = [w for w in comment_word_list_cluster_7 if not w in stop_words]
    comment_word_list_cluster_8 = [w for w in comment_word_list_cluster_8 if not w in stop_words]
    comment_word_list_cluster_9 = [w for w in comment_word_list_cluster_9 if not w in stop_words]

    # 빈칸 제거
    comment_word_list = [w for w in comment_word_list if w != '']
    comment_word_list_cluster_0 = [w for w in comment_word_list_cluster_0 if w != '']
    comment_word_list_cluster_1 = [w for w in comment_word_list_cluster_1 if w != '']
    comment_word_list_cluster_2 = [w for w in comment_word_list_cluster_2 if w != '']
    comment_word_list_cluster_3 = [w for w in comment_word_list_cluster_3 if w != '']
    comment_word_list_cluster_4 = [w for w in comment_word_list_cluster_4 if w != '']
    comment_word_list_cluster_5 = [w for w in comment_word_list_cluster_5 if w != '']
    comment_word_list_cluster_6 = [w for w in comment_word_list_cluster_6 if w != '']
    comment_word_list_cluster_7 = [w for w in comment_word_list_cluster_7 if w != '']
    comment_word_list_cluster_8 = [w for w in comment_word_list_cluster_8 if w != '']
    comment_word_list_cluster_9 = [w for w in comment_word_list_cluster_9 if w != '']

    # 2글자 이상 단어만 추출
    comment_word_list = [word for word in comment_word_list if len(word) >= 2]
    comment_word_list_cluster_0 = [word for word in comment_word_list_cluster_0 if len(word) >= 2]
    comment_word_list_cluster_1 = [word for word in comment_word_list_cluster_1 if len(word) >= 2]
    comment_word_list_cluster_2 = [word for word in comment_word_list_cluster_2 if len(word) >= 2]
    comment_word_list_cluster_3 = [word for word in comment_word_list_cluster_3 if len(word) >= 2]
    comment_word_list_cluster_4 = [word for word in comment_word_list_cluster_4 if len(word) >= 2]
    comment_word_list_cluster_5 = [word for word in comment_word_list_cluster_5 if len(word) >= 2]
    comment_word_list_cluster_6 = [word for word in comment_word_list_cluster_6 if len(word) >= 2]
    comment_word_list_cluster_7 = [word for word in comment_word_list_cluster_7 if len(word) >= 2]
    comment_word_list_cluster_8 = [word for word in comment_word_list_cluster_8 if len(word) >= 2]
    comment_word_list_cluster_9 = [word for word in comment_word_list_cluster_9 if len(word) >= 2]

    return [comment_word_list,
            comment_word_list_cluster_0,
            comment_word_list_cluster_1,
            comment_word_list_cluster_2,
            comment_word_list_cluster_3,
            comment_word_list_cluster_4,
            comment_word_list_cluster_5,
            comment_word_list_cluster_6,
            comment_word_list_cluster_7,
            comment_word_list_cluster_8,
            comment_word_list_cluster_9]


if __name__ == '__main__':
    analysis_result = k_means_clustering_analysis('hotelData_en/hotel1_en.csv', 10)
    frequencyAnalysis.draw_frequency_graph(analysis_result[1], "cluster #0")
    frequencyAnalysis.draw_frequency_graph(analysis_result[2], "cluster #1")
    frequencyAnalysis.draw_frequency_graph(analysis_result[3], "cluster #2")
    frequencyAnalysis.draw_frequency_graph(analysis_result[4], "cluster #3")
    frequencyAnalysis.draw_frequency_graph(analysis_result[5], "cluster #4")
    frequencyAnalysis.draw_frequency_graph(analysis_result[6], "cluster #5")
    frequencyAnalysis.draw_frequency_graph(analysis_result[7], "cluster #6")
    frequencyAnalysis.draw_frequency_graph(analysis_result[8], "cluster #7")
    frequencyAnalysis.draw_frequency_graph(analysis_result[9], "cluster #8")
    frequencyAnalysis.draw_frequency_graph(analysis_result[10], "cluster #9")
    frequencyAnalysis.draw_word_cloud(analysis_result[1], "cluster #0")
    frequencyAnalysis.draw_word_cloud(analysis_result[2], "cluster #1")
    frequencyAnalysis.draw_word_cloud(analysis_result[3], "cluster #2")
    frequencyAnalysis.draw_word_cloud(analysis_result[4], "cluster #3")
    frequencyAnalysis.draw_word_cloud(analysis_result[5], "cluster #4")
    frequencyAnalysis.draw_word_cloud(analysis_result[6], "cluster #5")
    frequencyAnalysis.draw_word_cloud(analysis_result[7], "cluster #6")
    frequencyAnalysis.draw_word_cloud(analysis_result[8], "cluster #7")
    frequencyAnalysis.draw_word_cloud(analysis_result[9], "cluster #8")
    frequencyAnalysis.draw_word_cloud(analysis_result[10], "cluster #9")

    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel2_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel3_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel4_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel5_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel6_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel7_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel8_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel9_en.csv', 10)
    # analysis_result = k_means_clustering_analysis('hotelData_en/hotel10_en.csv', 10)
