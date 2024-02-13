import pandas as pd
import os

import googletrans


def translate_single_file(file_path):
    """
    호텔 1개에 대하여 번역하고, hotelData_en 디렉토리에 csv 파일 저장
    :param file_path: hotel csv file path (ex. 'hotelData/hotel1.csv')
    """
    df_hotel = pd.read_csv(file_path)
    translator = googletrans.Translator()

    print('Translating ' + file_path + ' to English...')

    for index, row in df_hotel.iterrows():
        df_hotel.at[index, 'comment'] = translator.translate(row['comment'], 'en').text

    df_hotel.to_csv('hotelData_en/' + file_path.split('/')[-1].split('.')[0] + '_en.csv')

def translate_all_files():
    """
    hotelData 디렉토리 내 모든 csv 파일을 번역하여 hotelData_en 디렉토리에 저장
    """
    directory = 'hotelData/'
    for file_name in os.listdir(directory):
        file_path = directory + file_name
        if os.path.isfile(file_path) & file_name.startswith('hotel') & file_name.endswith('.csv'):
            translate_single_file(file_path)

if __name__ == "__main__":
# print(googletrans.LANGUAGES)
#     translate_all_files()
#     translate_single_file('hotelData/hotel4.csv') #
#     translate_single_file('hotelData/hotel5.csv')
#     translate_single_file('hotelData/hotel6.csv') #
#     translate_single_file('hotelData/hotel7.csv') #
    translate_single_file('hotelData/hotel8.csv')
    # translate_single_file('hotelData/hotel9.csv')
