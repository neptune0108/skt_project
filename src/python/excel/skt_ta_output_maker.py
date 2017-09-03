import json_parser
import excel_generator

file_directory = './data/skt_ta_analysis_result.json'
excel_file_name = './data/skt_ta_analysis_result.xlsx'

keyword_set_max, sentence_keyword_max, json_data_list = json_parser.get_json_data(file_directory)
excel_generator.get_excel_file(excel_file_name, keyword_set_max, sentence_keyword_max, json_data_list)

# print(keyword_set_max)
# print(sentence_keyword_max)
# print(json_data_list)

