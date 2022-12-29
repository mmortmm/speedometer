from influxdb import InfluxDBClient
import abc
import logging
import os
import time


class Writer(abc.ABC):
    db_name = None
    db_host = None
    db_port = None
    influx_client = None

    def __init__(self, db_name, db_host, db_port):
        self.db_name = db_name
        self.db_host = db_host
        self.db_port = db_port
        self._init_db()

    def _init_db(self):
        if not self.influx_client:
            client = InfluxDBClient(host=self.db_host, port=self.db_port)
            client.create_database(self.db_name)
            self.influx_client = client
            logging.info(
                f"Configured Influx [db={self.db_name}, host={self.db_host}:{self.db_port}]"
            )
        else:
            logging.info(
                "Influx client already configured, will not configure it again"
            )

    @abc.abstractmethod
    def write_data():
        pass

    @abc.abstractmethod
    def get_data():
        pass
