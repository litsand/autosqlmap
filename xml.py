
#!/usr/bin/python
#check the xml syntax

import re
import sys

def findfieldCount(line):
    fieldCount = re.match(r"""<entry key=.*fieldCount">(\d*)</entry>""", line)
    return fieldCount
    
def checkfield(count,line):
    rematch = r"""<entry key=.*field\[%s\]">.*</entry>""" % count
    original = re.match(rematch, line)
    return original

def checkfieldvalue(count,line):
    rematch = r"""<entry key=.*field\[%s\]\..+">.*</entry>""" % count
    original = re.match(rematch, line)
    return original

def check(linenum, xmllist):
    count = 0
    while True:
        if len(xmllist[linenum]) <= 2:
            return count
            break
            
        if checkfield(count,xmllist[linenum]) == None:
            print linenum ,'line has a wrong field number'
            return count
            break
            
        else:
            linenum = linenum + 1
            while True:
                
                if checkfieldvalue(count,xmllist[linenum]) == None:
                    count = count + 1
                    break
                else:
                    linenum = linenum + 1
                    continue
                    
                
                
            
filename = sys.argv[1]            

xml = open(filename)
xmllist = list(xml)

# print xmllist[20]
# print len(xmllist[2])
# print xmllist[2]
# print len(xmllist)

i = 0
while True:
    if i == len(xmllist):
        print "check complete"
        break
    line = xmllist[i]
    if findfieldCount(line) == None:
        i = i + 1
        continue
    else:
        count = findfieldCount(line).group(1)
        i = i + 1
        if int(check(i, xmllist)) != int(count):
          
            print i,"line has a wrong field count"
            # print count,check(i,xmllist)
        

#         while true:
            
            
    
    
    
# # test  = open('test.xml')
# # line = test.readline()
# # findfieldCount(line)
# # findfieldCount("""<entry key="mapper[2].fieldCount">17</entry>""")


# xml = open('map.xml')
# xmllist = list(xml)
# for line in xmllist:
#     print line
# xml.close()
