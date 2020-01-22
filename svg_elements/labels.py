#!/usr/bin/env python3

import cgi
import cgitb
import cx_Oracle
import filter as fil
import colour as col

cgitb.enable(format='text')

with open("/web/s1434165/public_html/static/pw/pw.txt","r") as pwf:
    pw = pwf.read().strip()

################### LABELS #######################

#field ID label to be near-centre of field
def fields_IDhtml():
    # set up of variables
    html = ''
    column, value = fil.fieldSelect()
    filter = fil.QueryBuilder(column, value) # only show labels for fields the user has selected

    #oracle connection and query to retrieve field geometry
    conn = cx_Oracle.connect(dsn="geoslearn", user="s1434165", password=pw)
    c = conn.cursor()
    c.execute("SELECT * FROM GISTEACH.FIELDS, GISTEACH.CROPS WHERE GISTEACH.FIELDS.CROP = GISTEACH.CROPS.CROP"+filter)

    for row in c:
        # label position (x,y) where x approx = (hix + lowx)/2 and y approx = (hiy+lowy)/2 (reversed to keep corrected number orientation)
        # rectangle around label
        html = html + '         <rect x= ' +str(((row[3]+row[1])/2)-0.25) + ' y=' + str((15.6-((row[4]+row[2])/2))) + ' width="0.50" height="0.50" fill="white" stroke="black" stroke-width="0.05"><title>Field '+str(row[0])+'</title></rect>\n'
        # text of label
        html = html + '         <text x= ' +str(((row[3]+row[1])/2)) + ' y= ' + str(16-((row[4]+row[2])/2)) + ' text-anchor="middle" > ' + str(row[0]) + ' </text>\n'

    conn.close()

    return html

#find ID label slightly offset from find position
def finds_IDhtml():
    # set up variables
    html = ''
    column, value = fil.findSelect()
    filter = fil.QueryBuilder(column, value) # only show labels for fields the user has selected

    #oracle connection and query to retrieve find location
    conn = cx_Oracle.connect(dsn="geoslearn", user="s1434165", password=pw)
    c = conn.cursor()
    c.execute("SELECT * FROM GISTEACH.FINDS, GISTEACH.CLASS WHERE GISTEACH.FINDS.TYPE = GISTEACH.CLASS.TYPE"+filter)

    for row in c:
        #label position (x,y) where x = approx x of find, y = y of find (reversed to keep corrected number orientation)
        html = html + '\n       <text x= ' + str(row[1]+0.19) + ' y= ' + str(16-row[2]) + ' text-anchor="right" > ' + str(row[0]) + ' </text>'

    conn.close()

    return html

# looping through range for grid labels with slight offset
def labelsHtml():
    html = ''

    for i in range(0,17):
        html = html + '\n           <text x="16.2" y= '+str(16.2-i)+' fill="gray" font-size="0.45"> '+str(i)+'</text>'
        html = html + '\n           <text x='+str(i-0.1)+' y="-0.25" fill="gray" font-size="0.45"> '+str(i)+'</text>'

    return html
