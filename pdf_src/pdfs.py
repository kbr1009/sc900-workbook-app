import PyPDF2

reader = PyPDF2.PdfFileReader('./az-900/az-900.pdf')

page_list = [
        14, 15, 16, 17, 18, 19, 20, 21, 23, 24,
        25, 26, 27, 28, 29, 30, 35, 36, 37, 38,
        39, 40, 42, 43, 45, 46, 47, 48, 50, 51, 
        52, 53, 54, 55, 56, 57, 60, 61, 63, 64,
        65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
        76, 77, 78, 79, 80, 81, 85, 86, 87, 88,
        89, 90, 91, 92, 96, 97, 99, 100, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
        126, 127, 128, 129, 131, 132, 133, 134, 135, 136
        ]


file_num = 1
for i in page_list:
    writer = PyPDF2.PdfFileWriter()
    page = reader.getPage(i-1)
    writer.addPage(page)

    file_name = str(file_num) + '.pdf'
    fpath = './az-900/' + file_name
    with open(fpath, mode='wb') as f:
        writer.write(f)
    file_num += 1
