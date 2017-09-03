import xlsxwriter

# excel_file_name = "./data/skt_ta_analysis_result.xlsx"


def get_excel_file(excel_file_name, keyword_set_max, sentence_keyword_set_max, result_list):

    with xlsxwriter.Workbook(excel_file_name, {'constant_memory': True}) as workbook:

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 8,
            'fg_color': '#D9D9D9'
        })

        string_format = workbook.add_format({
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 8
        })

        number_format = workbook.add_format({
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 8,
            'num_format': 'yyyy-mm-dd'
        })

        cell_multi_line_format = workbook.add_format({
            'text_wrap': True,
            'align': 'left',
            'valign': 'vcenter',
            'font_size': 9
        })

        col = 0
        row = 0
#        keyword_set_max = 7
#        sentence_keyword_set_max = 8

        total_col = 3 + keyword_set_max + sentence_keyword_set_max

        caption = "TA 결과 (Topic, 키워드 뭉치 추출)"
        description = "1. Paragraph 별로 Main Topic 과 키워드 뭉치, 문장별 키워드 뭉치, 특징이 있는 키워드 작성\n" \
                      "2. 키워드 뭉치 및 문장별 키워드 뭉치는 각각의 덩어리 별로 분리하여 키워드 뭉치 혹은 " \
                      "문장별 키워드 뭉치 1, 2, 3, ..., N 으로 구분하여 작성"

        worksheet = workbook.add_worksheet()

        worksheet.set_column(col, total_col, 20)
        worksheet.set_row(row, 20)
        worksheet.set_row(row + 1, 40, cell_multi_line_format)

    #    worksheet.write('A1', caption)
        worksheet.merge_range(0, 0, 0, total_col, caption, cell_multi_line_format)
        worksheet.merge_range(1, 0, 1, total_col, description, cell_multi_line_format)

        worksheet.write(2, 0, '날짜', header_format)
        worksheet.write(2, 1, '서비스관리번호', header_format)
        worksheet.write(2, 2, 'Main Topic', header_format)
        worksheet.write(2, 3, 'Feature Extraction', header_format)

        k_col_num = 4
        for i in range(keyword_set_max):
            worksheet.write(2, k_col_num + i, '키워드 뭉치 ' + str(i + 1), header_format)

        s_col_num = k_col_num + keyword_set_max
        for i in range(sentence_keyword_set_max):
            worksheet.write(2, s_col_num + i, '문장별 키워드 뭉치 ' + str(i + 1), header_format)

#        print(len(result_list))

        row = 3
        for paragraph_data in result_list:
            date_info = paragraph_data[2]
            service_num = paragraph_data[1]
            main_topic = ', '.join(paragraph_data[3])
            feature_extraction = ', '.join(paragraph_data[4])
            keyword_set = paragraph_data[5]
            sentence_keyword_set = paragraph_data[6]

            worksheet.write(row, 0, date_info, number_format)
            worksheet.write(row, 1, service_num, string_format)
            worksheet.write(row, 2, main_topic, string_format)
            worksheet.write(row, 3, feature_extraction, string_format)

            col = 4
            keyword_set_length = len(keyword_set) + col

            for j in range(keyword_set_max):
                if keyword_set_length > col:
                    worksheet.write(row, col, ', '.join(keyword_set[j]), string_format)
                else:
                    worksheet.write_blank(row, col, None, string_format)
                col += 1

            s_col = 4 + keyword_set_max
            sentence_keyword_set_length = len(sentence_keyword_set) + s_col

            for k in range(sentence_keyword_set_max):
                if sentence_keyword_set_length > s_col:
                    worksheet.write(row, s_col, ', '.join(sentence_keyword_set[k]), string_format)
                else:
                    worksheet.write_blank(row, s_col, None, string_format)
                s_col += 1

            row += 1

        workbook.close()