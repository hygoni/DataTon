# Date: 2020.12.23
# Author: hygoni
# Description: 데이터를 불러옴

from collections import Counter
import pickle



timeList = list()
counter = Counter()

with open('time_lst.bin', 'rb') as f:
    while True:
        try:
            timeList += pickle.load(f)
        except:
            break

with open('counter.bin', 'rb') as f:
    counter = pickle.load(f)

