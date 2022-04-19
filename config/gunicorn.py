import multiprocessing

name = 'penaval'
loglevel = 'info'
errorlog = '-'
accesslog = '-'
workers = multiprocessing.cpu_count() * 2 + 1
