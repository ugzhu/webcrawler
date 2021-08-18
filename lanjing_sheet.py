def Configurelanjingsheet(sheet):
    sheet.write(0, 0, "年份")
    sheet.write(0, 1, "日期")
    sheet.write(0, 2, "标题")
    sheet.write(0, 3, "链接")
    sheet.col(2).width = 256 * 100