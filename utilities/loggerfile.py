import logging
import inspect


class Log_Generator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(".\\log\ORM_log.log")
        logformat = logging.Formatter(
            "%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s : %(lineno)d : %(message)s"
        )
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
