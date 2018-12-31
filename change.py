import json
import os
#from elasticsearch import Elasticsearch

with open('fix.json') as f:
    data = json.load(f)

with open('values.json') as f:
    values = json.load(f)

with open("outputfinal.txt","r") as file:
    lines = file.readlines()
finalString = ""
output = open("output.dat","w")

for a in lines:
    a = a.replace("||","|")
    a = a.replace("|","")
    b=a.split('8=FIX.4.2')
    s= '8=FIX.4.2'+b[-1]
    finalString += s+" \n"

    #d = json.loads(finalString)
output.write(finalString)

fii=""
outt = open("text.json","w")
outt.write("{ \n")
os.system("fix2json -p FIX42.xml output.dat > tet.json")

with open("tet.json","r") as file:
    tet = file.readlines()

for l in tet:
    l= l.replace("}","},")
    fii += l
    #print(fii)

outt.write(fii+" }")

    #esclient = Elasticsearch(['localhost:9200'])
    #esclient.index(index="in", doc_type="fix_message", body=finStr)
    #esclient.get(index="in", doc_type="fix_message", id=1)