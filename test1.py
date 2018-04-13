#1
from collections import Counter
urls = ["http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png"]
nameLists = []
for i in urls:
    tmp = i.split("/")
    nameLists.append(tmp[len(tmp)-1])
print(nameLists)

# count_times = []
# for i in lists :
#         count_times.append(lists.count(i))
#
# print (lists[lists.index(max(count_times))])
lists = sorted(nameLists)
listsed = set(nameLists)

#dic = Counter(lists).keys()
print(Counter(lists))
for i in Counter(lists).most_common(3):
    print(i[0],i[1])
