import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# default is INFO
logger.setLevel(logging.INFO)


@contextmanager
def debug_context():
    level = logger.level
    try:
        # with文の間だけ、DEBUGに変更
        logger.setLevel(logging.DEBUG)
        yield
    finally:
        # 終わったら元のloglevelに戻す
        logger.setLevel(level)


def main():
    logger.info('befor: info log')
    logger.debug('befor: debug log')

    with debug_context():
        # この間だけDEBUGログが標示される
        logger.info('inside: info log')
        logger.debug('inside: debug log')

    logger.info('after: info log')
    logger.debug('after: debug log')


if __name__ == '__main__':
    main()
