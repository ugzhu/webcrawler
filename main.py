import xlwt
import os
import sys
import datetime
from lanjing_search import Searchlanjing
from lanjing_sheet import Configurelanjingsheet
from youwei_search import Searchyouwei
from youwei_sheet import Configureyouweisheet
from baidu_ads import Searchbaiduads
from baidu_ads_sheet import Configurebaiduadssheet
from baidu_search import configureBaiduSheet
from baidu_search import searchBaidu
from time import gmtime, strftime

workbook = xlwt.Workbook(encoding='utf-8')
keyword = input('请输入关键词：')
# pages = int(input('请输入要搜索的页面数量：'))
pages = 1

sheet1 = workbook.add_sheet("百度SEM")
sheet2 = workbook.add_sheet("百度SEO")
sheet3 = workbook.add_sheet("蓝鲸")
sheet4 = workbook.add_sheet("优维")

configureBaiduSheet(sheet2)
searchBaidu(sheet2, keyword, pages)

Configurebaiduadssheet(sheet1)
Searchbaiduads(sheet1, keyword)

Configurelanjingsheet(sheet3)
Searchlanjing(sheet3)

Configureyouweisheet(sheet4)
Searchyouwei(sheet4)

ISOTIMEFORMAT = '%Y-%m-%d %H点%M分%S秒'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
# theTime = strftime("%Y-%m-%d %H点%M分%S秒", gmtime())
path = os.getcwd() + '\搜索-' + keyword + '-' + theTime + '.xls'
print(path)
workbook.save(path)
