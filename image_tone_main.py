# from venv.test import testvs
import time
from venv.sql_require_image import query

if __name__ == '__main__':
    start  = time.process_time()
    # testvs()
    datalist=query()
    print(datalist)
    print("All Time cost: {0}".format(time.process_time() - start))