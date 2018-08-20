# -*- coding: utf-8 -*-
# Created by apple on 2017/2/16.

import logging
from config import LoggingConfig

__formatter = logging.Formatter(LoggingConfig.format)
__handle = logging.FileHandler(LoggingConfig.path, encoding='utf-8')
__handle.setFormatter(__formatter)

log = logging.getLogger(__name__)
log.setLevel(LoggingConfig.level)
log.addHandler(__handle)


def info(param):
    return None