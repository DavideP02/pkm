#!/usr/bin/python

import os, sys, re

max = len(sys.argv)

for i in range(1, max):
    # receiving input
    fileepath = str(sys.argv[i])
    lookfor = '[0-9]{12}'
    file = re.findall(lookfor, fileepath)
    filepdf = file[0] + '.pdf'
    path = fileepath.replace(filepdf, '')

    #manipulating the name to extract days, month and year
    year = file[0][0:4]
    print year
    month = file[0][4:6]
    print month
    day = file[0][6:8]
    print day

    # making numerical month into mmm

    if month == '01':
        month = 'gen'
    elif month == '02':
        month = 'feb'
    elif month == '03':
        month = 'mar'
    elif month == '04':
        month = 'apr'
    elif month == '05':
        month = 'mag'
    elif month == '06':
        month = 'giu'
    elif month == '07':
        month = 'lug'
    elif month == '08':
        month = 'ago'
    elif month == '09':
        month = 'set'
    elif month == '10':
        month = 'ott'
    elif month == '11':
        month = 'nov'
    elif month == '12':
        month = 'dic'


    # name of the file to create
    creating = file[0] + ' ' + '(' + day + ' ' + month + ' ' + year +')'
    creatingmd = creating + '.md'

    # path + name of the file to create
    completeName = os.path.join(path, creatingmd)
    file1 = open(completeName, "w")
    file1.write('# ' + creating + '\n\n')
    file1.write('![](' + filepdf + ')\n')
    file1.write('[File](' + filepdf + ')')
    file1.close()
