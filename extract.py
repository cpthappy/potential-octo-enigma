# -*- coding: utf-8 -*-
import pickle
from BeautifulSoup import BeautifulSoup
import codecs
import os


for file_name in [x for x in os.listdir(".") if x.endswith('.pkl')]:
    print file_name
    with open(file_name, "rb") as f:
        result = pickle.load(f)

    m = len(result)
    i = 0
    output = file_name.replace("raw", "data").replace(".pkl", ".txt")
    print output
    with codecs.open(output, "wb", "utf-8") as f:
        for url, html in result.iteritems():
            print i+1, '/', m
            soup = BeautifulSoup(html)
            if 'sex=W' in url:
                gender = "W"
            else:
                gender = "M"

            for row in soup.findAll('tr'):
                row_data = [gender]
                for entry in row.findAll('td'):
                    row_data.append(entry.text)

                if len(row_data) > 1:
                    print >>f, '\t'.join(row_data)
            i += 1
