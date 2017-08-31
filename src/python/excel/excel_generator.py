import xlsxwriter
import json

with open('./data/skt_voc_analysis_result.json', encoding='utf-8') as data_file:
    data = json.load(data_file)

print(data)
'''
workbook = xlsxwriter.Workbook('./data/skt_voc_analysis_result.xlsx')
worksheet = workbook.add_worksheet()

expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50]
)

row = 0
col = 0

for item, cost in expenses:
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
'''

with xlsxwriter.Workbook('./data/skt_voc_analysis_result.xlsx', {'constant_memory': True}) as workbook:

    header_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 9,
        'fg_color': '#D9D9D9'
    })

    string_format = workbook.add_format({
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 9
    })

    number_format = workbook.add_format({
        'border': 1,
        'align': 'right',
        'valign': 'vcenter',
        'font_size': 9,
        'num_format': '#,##0'
    })

    cell_multi_line_format = workbook.add_format({'text_wrap': True,
                                                  'align': 'left',
                                                  'valign': 'vcenter',
                                                  })

    caption = "TA 결과 (Topic, 키워드 뭉치 추출)"
    description = "1. Paragraph 별로 Main Topic 과 키워드 뭉치, 문장별 키워드 뭉치, 특징이 있는 키워드 작성 " \
                  "\n2. 키워드 뭉치 및 문장별 키워드 뭉치는 각각의 덩어리 별로 분리하여 키워드 뭉치 혹은 " \
                  "문장별 키워드 뭉치 1, 2, 3, ..., N 으로 구분하여 작성"

    worksheet = workbook.add_worksheet()

    worksheet.write('A1', caption)
    worksheet.merge_range('A1:L1', caption)
    worksheet.merge_range('A2:L2', description, cell_multi_line_format)

    worksheet.write('A3', '날짜', header_format)
    worksheet.write('B3', '서비스관리번호', header_format)
    worksheet.write('C3', 'Main Topic', header_format)
    worksheet.write('D3', 'Feature Extraction', header_format)
    worksheet.write('E3', '키워드 뭉치 1', header_format)
    worksheet.write('F3', '키워드 뭉치 2', header_format)
    worksheet.write('G3', '키워드 뭉치 3', header_format)
    worksheet.write('H3', '키워드 뭉치 4', header_format)
    worksheet.write('I3', '문장별 키워드 뭉치 1', header_format)
    worksheet.write('J3', '문장별 키워드 뭉치 2', header_format)
    worksheet.write('K3', '문장별 키워드 뭉치 3', header_format)
    worksheet.write('L3', '문장별 키워드 뭉치 4', header_format)

    worksheet.set_column('A:L', 20)
    worksheet.set_row(1, 60, cell_multi_line_format)

    workbook.close()
