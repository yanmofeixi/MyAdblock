## https://www.w3schools.com/cssref/css_selectors.asp

f = open("filter.txt", "r")
lines = f.read().split('\n')
lines.sort()
f = open("filter.txt", "w")
f.write("\n".join(lines))