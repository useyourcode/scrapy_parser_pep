import csv
import datetime as dt

from pep_parse.settings import (
    FIELDS_NAME, EXPECTED_STATUS,
    FILE_NAME, BASE_DIR
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {}
        self.result_dir = BASE_DIR / 'results'
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        pep_status = item['status']
        EXPECTED_STATUS[pep_status] = EXPECTED_STATUS.get(pep_status, 0) + 1

        return item

    def close_spider(self, spider):
        DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
        TIME_NOW = dt.datetime.now().strftime(DT_FORMAT)
        file_dir = self.result_dir / FILE_NAME.format(time=TIME_NOW)

        data_to_write = [[key, val] for key, val in EXPECTED_STATUS.items()]
        data_to_write.append(['Total', sum(EXPECTED_STATUS.values())])

        with open(file_dir, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerow(FIELDS_NAME)
            writer.writerows(data_to_write)
