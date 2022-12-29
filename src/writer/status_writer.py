from .writer import Writer
import datetime
import logging
import requests


class StatusWriter(Writer):
    STATUS = {"UP": 1, "DOWN": 0}

    TEST_SOURCES = [
        "https://fast.com",
        "https://github.com",
        "https://google.com",
        "https://cnn.com",
    ]

    def _is_internet_up(self):
        for i in self.TEST_SOURCES:
            try:
                r = requests.head(i)
                if r.status_code < 400:
                    return True
            except Exception as e:
                logging.error(f"Request to {i} failed")
                continue
        logging.error("All status check requests failed, internet is not working")
        return False

    def get_data(self):
        logging.info("Getting data")
        status = None
        if self._is_internet_up():
            status = self.STATUS["UP"]
        else:
            status = self.STATUS["DOWN"]

        datapoint = {
            "measurement": "status_datapoint",
            "tags": {
                "type": "status",
            },
            "time": datetime.datetime.now(),
            "fields": {"value": status},
        }

        logging.info(f"Internet status: {status}")
        return [datapoint]

    def write_data(self):
        self.influx_client.write_points(
            self.get_data(),
            database=self.db_name,
            time_precision="ms",
            batch_size=10000,
        )
