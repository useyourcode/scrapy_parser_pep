import csv
import datetime as dt

from pep_parse.settings import (
    FIELDS_NAME, expected_status,
    FILE_NAME, BASE_DIR, DT_FORMAT
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}
        self.result_dir = BASE_DIR / 'results'
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        expected_status[item['status']] = expected_status.get(
            item['status'], 0
        ) + 1
        return item

    def close_spider(self, spider):
        current_time = dt.datetime.now().strftime(DT_FORMAT)
        file_dir = self.result_dir / FILE_NAME.format(time=current_time)

        data_to_write = [[key, val] for key, val in expected_status.items()]
        data_to_write.append(['Total', sum(expected_status.values())])

        with open(file_dir, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerow(FIELDS_NAME)
            writer.writerows(data_to_write)
