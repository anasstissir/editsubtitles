import re
from datetime import datetime
from datetime import timedelta

with open('First.Man.2018.HC.HDRip.XviD.AC3-EVO-HI.srt', 'r') as myfile:
    data = myfile.read()
tablSplit = re.split(r'\n', data)
array = re.findall(r'\d+:\d+:\d+.\d+', data)
for i in range(0, len(array)):
    tmp = re.sub(array[i],
                 str((datetime.strptime(array[i][0:8], '%H:%M:%S') + timedelta(seconds=-11)))[11:] + array[i][8:12],
                 data, flags=re.IGNORECASE)
    data = tmp
with open("firstman.srt", "a") as myfile:
    myfile.write(data[3:])
print("done")
