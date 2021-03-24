from absl import app
from absl import flags
from absl import logging
import time
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

from settings import LOG_LEVEL, WEBSITE_URL, ELEMENT_ID, POLL_INTERVAL

FLAGS = flags.FLAGS
flags.DEFINE_string("url", None, "URL of the website to scrape", short_name="u")
flags.DEFINE_string(
    "id",
    None,
    "DOM element ID of the element that contains the required text value",
    short_name="i",
)
flags.DEFINE_integer("interval", None, "Polling interval in seconds", short_name="p")


def convert_kvdict_to_dict(kvdict):
    logging.debug(f"List of dictionaries before conversion: {kvdict}")
    cdict = {}
    for pair_dict in kvdict:
        cdict[pair_dict["key"]] = pair_dict["value"]
    logging.debug(f"Dictionary after conversion: {cdict}")
    return cdict


def main(argv):
    del argv  # Unused.
    logging.set_verbosity(getattr(logging, LOG_LEVEL.upper()))

    logging.info(f"JAWS - Just Another Web Scraper starting...")
    if FLAGS.url == None:
        FLAGS.url = WEBSITE_URL
    logging.debug(f"Website URL to scrape: '{FLAGS.url}'.")
    if FLAGS.id == None:
        FLAGS.id = ELEMENT_ID
    logging.debug(f"Element ID: '{FLAGS.id}'.")
    if FLAGS.interval == None:
        FLAGS.interval = POLL_INTERVAL
    logging.debug(f"Polling interval: '{FLAGS.interval}'.")

    clean_url = FLAGS.url
    special_chars = ["/", ";", "?", "@", ":", "!", "*"]
    for i in special_chars:
        clean_url = clean_url.replace(i, "")
    filename = f"{clean_url}-{FLAGS.id}.log"
    logging.debug(f"Writing to log file: '{filename}'.")

    logging.info(f"JAWS - Just Another Web Scraper running...")

    while True:
        http_response = urlopen(FLAGS.url)
        soup = BeautifulSoup(http_response.read(), features="html.parser")
        value = soup.find(id=FLAGS.id).getText()
        with open(filename, "a") as f:
            f.writelines(f"{datetime.datetime.now()}: {value}\n")
        time.sleep(FLAGS.interval)


if __name__ == "__main__":
    app.run(main)
