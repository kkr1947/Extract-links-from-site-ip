# x = 0
# for i in range(46):
#     x = x+1
#     # st = "le"+str(i+1)+" = response.css('#sites_tbl > tbody > tr:nth-child(" + \
#     #     str(i+x)+") > td.row_name > a::text').extract()"
#     # st = "items['le"+str(i+1)+"'] = le"+str(i+1)
#     # st = "le"+str(i+1)+" = scrapy.Field()"
#     st = "file:///home/dduc-cc/Downloads/"+str(i+1)+".html"
#     print(st)


import csv
site_ref = []
for i in range(50):
    with open('/home/dduc-cc/Documents/leadthree/leadthree/last2.csv', 'r') as file:
        reader = csv.reader(file)
        c = 1
        for row in reader:
            if c == 1:
                c = 2
            else:
                site_ref.append(row[i])


with open("out.txt", "w") as output:
    for i in range(len(site_ref)):
        output.write("https://"+site_ref[i]+"\n")
