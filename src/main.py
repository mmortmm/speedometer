from writer.speed_writer import SpeedWriter
from writer.status_writer import StatusWriter
import time
import logging
import os


DATABASE = "home_net_speed_stats"
DB_HOST = os.getenv("INFLUX_DB_HOST", "localhost")
DB_PORT = os.getenv("INFLUX_DB_PORT", 8086)


def _get_writers():
    writers = []
    writers.append(SpeedWriter(DATABASE, DB_HOST, DB_PORT))
    writers.append(StatusWriter(DATABASE, DB_HOST, DB_PORT))
    return writers


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
    )
    logging.info("Starting...")

    writers = _get_writers()
    for i in writers:
        i.write_data()

    logging.info("Finished writing datapoints, exiting...")


if __name__ == "__main__":
    main()
