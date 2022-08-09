import PyPDF2

reader = PyPDF2.PdfFileReader('./a.pdf')


page_list = [
        16,
        17,
        21, 
        22,
        25, 
        26,
        29, 
        30,
        34, 
        35,
        36, 
        37,
        44, 
        45,
        47, 
        48,
        52, 
        53,
        57, 
        58,
        60, 
        61,
        64, 
        65,
        72, 
        73,
        76, 
        77,
        78, 
        79,
        81, 
        82,
        88, 
        89,
        91, 
        92,
        95, 
        96,
        101, 
        102,
        103, 
        104,
        106, 
        107,
        114, 
        115,
        119, 
        120,
        125, 
        126,
128, 
        129,
        131, 
        132,
        137,
        138,
        140, 
        141,
        147,
        148,
        153, 
        154,
        157,
        158,
        161,
        162,
        167, 
        168,
        174,
        175,
        176,
        177,
        182,
        183,
        184, 
        185,
        191,
        192,
        196,
        197
        ]

file_num = 1
for i in page_list:
    writer = PyPDF2.PdfFileWriter()
    page = reader.getPage(i-1)
    writer.addPage(page)

    file_name = str(file_num) + '.pdf'
    fpath = './pdfs/' + file_name
    with open(fpath, mode='wb') as f:
        writer.write(f)
    file_num += 1
