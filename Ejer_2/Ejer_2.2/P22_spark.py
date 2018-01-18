from pyspark import SparkConf, SparkContext
import string

conf = SparkConf().setMaster('local').setAppName('P22_spark')
sc = SparkContext(conf = conf)

logs = sc.textFile("access_log")
# 64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] "GET /mailman/listinfo/hsdivision HTTP/1.1" 200 6291

urls = logs.map(lambda x: x.encode("ascii", "ignore").split()[6])
# /mailman/listinfo/hsdivision

urls2 = urls.map(lambda uri: (uri,1))
# (/mailman/listinfo/hsdivision, 1)

aggreg = urls2.reduceByKey(lambda acum,n: acum+n)
# (/mailman/listinfo/hsdivision, suma)

aggreg = aggreg.sortByKey()

aggreg.saveAsTextFile("output22")