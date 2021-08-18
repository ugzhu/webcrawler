def Configureyouweisheet(sheet):
    sheet.write(0, 0, "日期")
    sheet.write(0, 1, "标题")
    sheet.write(0, 2, "链接")
    sheet.col(0).width = 256 * 20
    sheet.col(1).width = 256 * 70
