# pylint: disable=line-too-long
"""
Logging Module
"""
from enum import Enum, unique
import logging
import sys
import inspect
import traceback
from logging import DEBUG


@unique
class Color(Enum):
    """A class for terminal color codes."""

    BOLD = "\033[1m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    PURPLE = "\033[95m"
    LIME = "\033[38;5;154m"
    ORANGE = "\033[38;5;215m"
    DARKGREY = "\033[90m"
    MAROON = "\033[38;5;52m"
    LIGHTBLUE = "\033[38;5;51m"
    JADE = "\033[38;5;35m"
    BOLD_WHITE = BOLD + WHITE
    BOLD_BLUE = BOLD + BLUE
    BOLD_GREEN = BOLD + GREEN
    BOLD_YELLOW = BOLD + YELLOW
    BOLD_RED = BOLD + RED
    END = "\033[0m"


class Logs:
    """Logging class"""

    format = "%(asctime)s | %(moduleName)-35s | %(levelname)-8s | %(function)-28s | %(message)s"
    console_formatter = logging.Formatter(format)
    console_logger = logging.StreamHandler(sys.stdout)
    console_logger.setFormatter(console_formatter)
    logger = logging.getLogger("pixitrend")
    logger.setLevel(level=DEBUG)
    logger.addHandler(console_logger)
    log_file = logging.FileHandler("logs.log")
    log_file.setFormatter(console_formatter)
    logger.addHandler(log_file)

    def __init__(self, level=DEBUG):
        self.extra = {}
        self.level = level

    def info(self, msg):
        """INFO override function"""
        self.set_function_name()
        self.logger.info(msg, extra=self.extra)

    def error(self, msg):
        """ERROR override function"""
        self.set_function_name()
        _, _, tba = sys.exc_info()
        try:
            filename, lineno, funname, line = traceback.extract_tb(tba)[-1]
            debug = f"Filename = {filename} -- Line = {lineno} -- function = {funname} -- codeline = {line}"
            self.logger.error(f"{debug} -- msg = {msg}", extra=self.extra)
        except IndexError:
            self.logger.error(msg, extra=self.extra)

    def debug(self, msg):
        """DEBUG override function"""
        self.set_function_name()
        self.logger.debug(msg, extra=self.extra)

    def warn(self, msg):
        """WARN override function"""
        self.set_function_name()
        self.logger.warning(msg, extra=self.extra)

    def set_function_name(self):
        """Set the caller function"""
        # Get call function's name
        func = inspect.currentframe().f_back.f_back.f_code
        filename = func.co_filename.split("/" if "/" in func.co_filename else "\\")[-1]
        self.extra["function"] = f"{Color.PURPLE.value}{func.co_name}{Color.END.value}"
        self.extra["moduleName"] = f"{Color.ORANGE.value}{filename}{Color.END.value}"