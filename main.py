import logging

logging.basicConfig(filemode='w', level=logging.DEBUG,
                    format="%(name)s %(levelname)s %(process)d %(asctime)s %(message)s",
                    filename='my_logs.log')


m = int
spam = 'hello'
summa = None

try:
    logging.info('Trying to get duble "hello"')
    summa = m * spam
except Exception:
    logging.error('error;(')









