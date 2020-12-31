import logging


class LoggingHandler:
    def __init__(self, classname, level):
        # create logger
        self.log = logging.getLogger(classname)
        self.log.setLevel(level)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.log.addHandler(ch)
        # self.log.debug("LoggingHandler works")
