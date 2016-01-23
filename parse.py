import csv
import os
import sha
import codecs

from unidecode import unidecode

with codecs.open("data.csv", "wb", "utf-8") as dataf:
    writer = csv.DictWriter(dataf, fieldnames=["gender", "time", "birth", "competition", "date", "id", "dist", "year"])
    for filename in [x for x in os.listdir(".") if x.endswith(".txt")]:
        if filename.startswith("data"):
            dist, year = filename.replace("data_", "").replace(".txt", "").split("_")
            print dist, year
            with codecs.open(filename, "r", "utf-8") as f:
                content = f.readlines()
                for line in content:
                    data = line.split("\t")
                    if data[1].isdigit():
                        try:
                            rid= sha.new(unidecode(data[5]) + "_" + data[6]).hexdigest()
                            tmp = {'gender' : data[0],
                                    'time' : data[4],
                                    'birth' : data[6],
                                    'competition' : unidecode(data[8]),
                                    'date' : data[9],
                                    'id' : rid,
                                    'dist' : dist,
                                    'year' : year
                                    }
                            writer.writerow(tmp)
                        except IndexError:
                            pass
                        except UnicodeDecodeError:
                            print tmp
