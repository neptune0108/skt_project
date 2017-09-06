import json
from collections import OrderedDict

# file_directory = '/stt/mazinga/data/skt_ta_analysis_result.json'
# file_directory = './data/skt_ta_analysis_result.json'


def get_json_data(file_directory):
    with open(file_directory, encoding='utf-8') as data_file:
        data = json.load(data_file, object_pairs_hook=OrderedDict)

# print(len(data['ta_analysis_result']))

    total_length = len(data['ta_analysis_result']['file_list'])
    max_keyword_set_length = 0
    max_sentence_keyword_set_length = 0

    json_string_list = []

    for i in range(total_length):
        #    print(ta_tmp['file_name'])
        #    print(ta_tmp['service_number'])
        #    print(ta_tmp['date'])
        #    print(ta_tmp['type'])

        file_name = data['ta_analysis_result']['file_list'][i]
        service_number = file_name
        date = '2017-09-04'
        type_info = ''

    #    print(max(len(l) for l in ta_tmp['paragraph']['keyword_set'))

        for paragraph_tmp in data['ta_analysis_result']['paragraph_list'][i]:
            main_topic = paragraph_tmp['topic']
            sub_topic = paragraph_tmp['sub_topic']
            keyword = paragraph_tmp['keyword']
            keyword_set = paragraph_tmp['keyword_set']
            sentence_keyword_set = paragraph_tmp['sentence_keyword_set']

            string_list = []

            string_list.append(file_name)
            string_list.append(service_number)
            string_list.append(date)
            string_list.append(type_info)
            string_list.append(main_topic)
            string_list.append(sub_topic)
            string_list.append(keyword)
            string_list.append(keyword_set)
            string_list.append(sentence_keyword_set)

            if max_keyword_set_length < len(paragraph_tmp['keyword_set']):
                max_keyword_set_length = len(paragraph_tmp['keyword_set'])

            if max_sentence_keyword_set_length < len(paragraph_tmp['sentence_keyword_set']):
                max_sentence_keyword_set_length = len(paragraph_tmp['sentence_keyword_set'])

            json_string_list.append(string_list)

    return max_keyword_set_length, max_sentence_keyword_set_length, json_string_list
