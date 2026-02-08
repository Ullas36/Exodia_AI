import logging

logging.basicConfig(
    filename="chat.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_event(event):
    logging.info(event)
