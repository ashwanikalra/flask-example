#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module contains utility about logging

"""
import logging
from logging.handlers import RotatingFileHandler

from config import LOG_PATH


class MyLogger:
    """ This is MyLogger class , to catch the error
        while accessing the basket API
    """

    def __init__(self):
        self.formatter = logging.Formatter(
            "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
        self.logHandler = RotatingFileHandler(
            LOG_PATH, mode='a', maxBytes=0, backupCount=0, encoding=None,
            delay=False
        )
        self.logHandler.setLevel(logging.INFO)
        self.logHandler.setFormatter(self.formatter)
        self.info = logging.INFO
        self.error = logging.ERROR
