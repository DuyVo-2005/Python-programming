import xlsxwriter
# tạo một file excel cùng 1 sheet
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
# thiết lập các cột cho file
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)
# định dạng tiêu đề cột in đậm
bold = workbook.add_format({'bold': True})
# thêm dòng tiêu đề và định dạng in đậm
worksheet.write('A1', 'STT',bold)
worksheet.write('B1', 'MÃ SẢN PHẨM',bold)
worksheet.write('C1', 'TÊN SẢN PHẨM',bold)
worksheet.write('D1', 'SỐ LƯỢNG',bold)
worksheet.write('E1', 'ĐƠN GIÁ',bold)

# thêm một dòng dữ liệu
worksheet.write('A2',1)
worksheet.write('B2','SP1')
worksheet.write('C2', 'Coca')
worksheet.write('D2', '15')
worksheet.write('E2', '15000')
# thêm một dòng dữ liệu
worksheet.write('A3',2)
worksheet.write('B3','SP2')
worksheet.write('C3', 'Pepsi')
worksheet.write('D3', '20')
worksheet.write('E3', '18000')
# chèn Logo vào
worksheet.insert_image('B5', 'logo_HCMUTE.png')

workbook.close()