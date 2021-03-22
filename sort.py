## https://www.w3schools.com/cssref/css_selectors.asp
## https://pastebin.com/TB0WrE4C
## https://help.eyeo.com/en/adblockplus/how-to-write-filters#elemhide_css

import re

f = open("filter.txt")
comments = []
for i in range(10):
    comments.append(f.readline())

lines = f.read().split('\n')
lines.sort()
p = re.compile('! Version: (.*)\n')
version = int(p.search(comments[3]).group(1))
comments[3] = p.sub('! Version: '+ str(version+1) + '\n', comments[3])
f = open("filter.txt", "w")
f.write("".join(comments))
f = open("filter.txt", "a")
f.write("\n".join(lines))