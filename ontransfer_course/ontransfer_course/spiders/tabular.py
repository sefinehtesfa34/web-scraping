# Scrapy
import scrapy
from openpyxl import Workbook
class TabularSpider(scrapy.Spider):
    name = 'tabular'
    start_urls = ['https://c2c.ontransfer.ca/index_en.php?page=c2c&user_action=search_t2&C2CTargetInstitution=366&back_link=page%3Dc2c%26user_action%3Dsearch_t2&results=Find+Equivalencies']
    def parse(self, response):
        workbook = Workbook()
        sheet = workbook.active
        if response.status == 200:
            table = response.xpath('//*[@id="form_c2c_search_results"]/fieldset/table')
            try:
                thead = table.xpath('//*[@id="form_c2c_search_results"]/fieldset/table/thead')
                rows = thead.xpath('.//tr')
                print("Len thead rows: ", len(rows))
                for row in rows:
                    cells = row.xpath('.//th')
                    cells_data = [cell.xpath('.//text()').get() for cell in cells]
                    print(cells_data)
                    sheet.append(cells_data)
                tbody = table.xpath('//*[@id="form_c2c_search_results"]/fieldset/table/tbody')
                rows = tbody.xpath('.//tr')
                
                for index, row in enumerate(rows, 1):
                    first = row.xpath(f'//*[@id="form_c2c_search_results"]/fieldset/table/tbody/tr[{index}]/td[2]/text()').get()
                    second = row.xpath(f'//*[@id="form_c2c_search_results"]/fieldset/table/tbody/tr[{index}]/td[3]/a/text()').get()
                    third = row.xpath(f'//*[@id="form_c2c_search_results"]/fieldset/table/tbody/tr[{index}]/td[4]/text()').get()
                    fourth = row.xpath(f'//*[@id="form_c2c_search_results"]/fieldset/table/tbody/tr[{index}]/td[5]/text()').get()
                    fifth = row.xpath(f'//*[@id="form_c2c_search_results"]/fieldset/table/tbody/tr[{index}]/td[6]/text()').get()
                    seventh = row.xpath(f'//*[@id="form_c2c_search_results"]/fieldset/table/tbody/tr[{index}]/td[7]/a/text()').get()
                    sheet.append([first, second, third, fourth, fifth, seventh])
                    if index == 100:
                        break
                workbook.save('tabular.xlsx')
            except:
                pass 
# https://c2c.ontransfer.ca/index_en.php?page=c2c&user_action=search_t2&C2CTargetInstitution=366&back_link=page%3Dc2c%26user_action%3Dsearch_t2&results=Find+Equivalencies
