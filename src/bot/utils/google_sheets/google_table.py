import sys
import os
from http import client
from gspread import Client, Spreadsheet, Worksheet, service_account
from datetime import datetime

sys.path.append(os.path.join(sys.path[0], 'bot'))

from config import GOOGLE_TABLE_LINK


#декоратор синглтон, чтобы было только одно подключение
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Google_sheets:

    TABLE_URL = GOOGLE_TABLE_LINK
    FILENAME = 'utils/google_sheets/test-project-telegram-428811-e352966445f7.json'
    __position = 2

    def __init__(self) -> None:
        self._CLIENT = self.client_init_json()
        self.table = self.get_table_by_id(self._CLIENT,self.TABLE_URL)



    def client_init_json(self) -> Client:
    # Создание клиента для работы с Google Sheets.
        return service_account(filename=self.FILENAME)

    
    def get_table_by_id(self, client: Client, TABLE_URL):
    # """Получение таблицы из Google Sheets по ID таблицы."""
        return client.open_by_url(TABLE_URL)
    

    async def extract_data_from_sheet(self, sheet_name: str):
    # получение данных из ячейки А2
            worksheet = self.table.worksheet(sheet_name)
            A2 =  worksheet.cell(row=2, col=1).value
            return A2

    async def check_data(self,sheet_name:str, date:str) -> str:
        date_format = r"%d.%m.%y"
        try:
            #проверка даты по регулярному выражению
            datetime.strptime(date, date_format)
            worksheet = self.table.worksheet(sheet_name)
            worksheet.update_cell(self.__position,2,str(date))
            #запоминаем позицию последнего добавленого элемента
            self.__position +=1
            return 'Дата верна, и супешно добавлена'


        except ValueError:
            return 'Дата не верна!\n Дата не соответствует формату dd.mm.yy'

    



