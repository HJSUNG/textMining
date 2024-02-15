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

    df_hotel['k' + str(k)] = frame['cluster']
    df_hotel.to_csv(file_path, index=False)


if __name__ == '__main__':
    print("kMeansClustering.py")
    k_means_clustering_analysis('hotelData_en/hotel1_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel2_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel3_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel4_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel5_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel6_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel7_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel8_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel9_en.csv', 10)
    k_means_clustering_analysis('hotelData_en/hotel10_en.csv', 10)
