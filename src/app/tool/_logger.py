# REMEMBER:
# log early
# log often

import logging  # using standard library
from logging.handlers import RotatingFileHandler
from pathlib import Path


class InternalLogger:
    def __init__(self, verbosity: str, log_path: Path) -> None:
        # The streamlit logger is not working properly, this is a workaround:
        # https://github.com/streamlit/streamlit/issues/4742

        # Disable the Streamlit's overrides
        # import streamlit.logger

        # streamlit.logger.get_logger = logging.getLogger
        # streamlit.logger.setup_formatter = None
        # streamlit.logger.update_formatter = lambda *a, **k: None
        # streamlit.logger.set_log_level = lambda *a, **k: None

        # from logging.handlers import TimeRotatingFileHandler

        # using rich library
        # from rich.logging import RichHandler

        # Set the logs constants (You can use env var)
        # -------------------------------------------------
        # VERBOSITY log level
        VERBOSITY: str = verbosity
        # log folder
        LOG_PATH: Path = log_path
        # log main filename
        LOGGER_FILENAME: str = "daemon.log"
        FILE_TIME_WHEN = "D"  # Days
        FILE_TIME_INTERVAL = 30
        FILE_BACKUP_COUNT = 12  # Number of backup
        FILE_MAX_BYTES = 100 * 1024 * 1024  # 100 MB
        FILE_ENCODING = "utf-8"
        FILE_DELAY = False

        # shell formatter syntax
        SHELL_FORMATTER_SYNTAX = "%(asctime)s (%(levelname)s) \t| [%(filename)s:%(funcName)s:%(lineno)d] \t| %(message)s"
        # file formatter syntax
        FILE_FORMATTER_SYNTAX = "%(asctime)s (%(levelname)s) \t| [%(filename)s:%(funcName)s:%(lineno)d] \t| %(message)s"

        # handler for file (make the folder if not exist)
        if not LOG_PATH.exists():
            LOG_PATH.mkdir(parents=True, exist_ok=True)
        FILE_LOG_PATH = LOG_PATH / LOGGER_FILENAME
        # -------------------------------------------------

        # Define the logger
        logger = logging.getLogger(__name__)

        # For your application you can just use this: from logger import logger
        log_name = VERBOSITY.upper().strip()
        log_level = logging.getLevelName(log_name)

        # handler for shell
        shell_handler = logging.StreamHandler()

        # Rotating handler for file
        # (Rotating = auto-delete by space and backup number to avoid oversized logs)
        file_handler = RotatingFileHandler(
            str(FILE_LOG_PATH),
            mode="a",
            maxBytes=FILE_MAX_BYTES,
            backupCount=FILE_BACKUP_COUNT,
            encoding=FILE_ENCODING,
            delay=FILE_DELAY,
        )

        # TimeRotating handler for file
        # (TimeRotating = auto-delete by time to avoid oversized logs)
        # file_handler = logging.handlers.TimeRotatingFileHandler(
        #     FILE_LOG_PATH,
        #     when=FILE_TIME_WHEN,
        #     interval=FILE_TIME_INTERVAL,
        #     backupCount=FILE_BACKUP_COUNT,
        #     encoding=FILE_ENCODING,
        #     delay=FILE_DELAY,
        # )

        # beautiful log with rich library
        # shell_handler = RichHandler()
        # rich_fmt = "%(message)s"

        if isinstance(log_level, int):
            # set the verbosity of the logs
            logger.setLevel(log_level)
            shell_handler.setLevel(log_level)
            file_handler.setLevel(log_level)
        else:
            raise NotImplementedError(f"Logging level error: {log_name}")

        # register the formatter with the formatter syntax
        shell_formatter = logging.Formatter(SHELL_FORMATTER_SYNTAX)
        file_formatter = logging.Formatter(FILE_FORMATTER_SYNTAX)

        # set the formatter
        shell_handler.setFormatter(shell_formatter)
        file_handler.setFormatter(file_formatter)

        # add the handler (to catch the logs)
        logger.addHandler(shell_handler)
        logger.addHandler(file_handler)

        # application logger
        self.logger: logging.Logger = logger
        # streamlit logger
        self.streamlit_handler: logging.Logger = logger

    def get_logger(self) -> logging.Logger:
        return self.logger


# Logger usage (by level)
# logger.debug("debug statement")
# logger.info("info statement")
# logger.warning("warning statement")
# logger.critical("critical statement")
# logger.error("error statement")
# logger.exception("exception statement")
