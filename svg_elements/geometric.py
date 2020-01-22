#!/usr/bin/env python3

import cgi
import cgitb
import cx_Oracle
import colour as col
import filter as fil

cgitb.enable(format='text')

with open("/web/s1434165/public_html/static/pw/pw.txt","r") as pwf:
    pw = pwf.read().strip()

"""
    This modules has two important and complex functions which bring together
    all the relevant variables for drawing the svg fields and finds. The
    general structure is as follows...

    # STEP ONE: Take the database column chosen for colouring
    # STEP TWO: Take the values chosen for filtering (and the SQL construct)
    # STEP THREE: Set up any empty or default values (in the instance of no user choice)
    # STEP FOUR: Set up colour dictionary to match with chosen column
    # STEP FIVE: Query the Oracle database, taking onboard the user-added SQL filter
    # STEP SIX: Loop through query results for plotting, while matching with
                colour dictionary values
    # STEP SEVEN: Return the completed and customised fields/finds SVG code for
                integration with SVG template

"""

############################## FIELDS ########################################

def fieldsHtml():
    # taking all the user determined values for the svg
    n = col.fieldColour() # column number to use for colour
    column, value = fil.fieldSelect() # values to use for additional query
    filter = fil.QueryBuilder(column, value) # additional query statement

    # creationg of empty or default variales for use
    html = ''
    fillc = '#fff' #default for integrity
    fillc_dict = {
    "DEFAULT": "#fff"
    }

    # colour dictionary for reference and set up of variables
    field_colour_dict = {
    'TURNIPS': '#F0E68C',
    'OIL SEED RAPE': '#FFD700',
    'STRAWBERRIES': '#FF4500',
    'PEAS':'#228B22',
    'POTATOES':'#BDB76B',
    'FARMER BLACK': '#212121',
    'FARMER WHITE': '#fff',
    'FARMER GREEN': '#3cb44b',
    'FARMER BROWN': '#9a6324'
    }

    # oracle connection and querying
    conn = cx_Oracle.connect(dsn="geoslearn", user="s1434165", password=pw)
    c = conn.cursor()
    c.execute("SELECT GISTEACH.FIELDS.FIELD_ID, GISTEACH.FIELDS.LOWX,GISTEACH.FIELDS.LOWY, GISTEACH.FIELDS.HIX, GISTEACH.FIELDS.HIY, GISTEACH.FIELDS.AREA, GISTEACH.FIELDS.OWNER, GISTEACH.CROPS.NAME, GISTEACH.CROPS.START_OF_SEASON, GISTEACH.CROPS.END_OF_SEASON FROM GISTEACH.FIELDS, GISTEACH.CROPS WHERE GISTEACH.FIELDS.CROP = GISTEACH.CROPS.CROP"+filter)

    # loop through query result for drawing and matching with any relevant colours
    for row in c:
        for i in field_colour_dict.keys():
            if row[n] == i: # matching entity column value with colour
                fillc = field_colour_dict[i] # choosing the value of the colour key
                fillc_dict[i] = fillc # filling a new dictionary of the colours actually used (for use in the legend function)
        #integration of sql result with html
        html = html + '\n           <rect class="zoom" id='+str(row[0])+' x= '+str(row[1])+' y= '+str(row[2])+' width= '+str(row[3]-row[1])+' height= '+str(row[4]-row[2])+' fill= '+str(fillc)+' fill-opacity="0.85" owner="'+str(row[6]).capitalize()+'" crop="'+str(row[7]).capitalize()+'"  crop_start="' + '{:%B}'.format(row[8])+ '" crop_end="'+ '{:%B}'.format(row[9])+'" onClick=fieldInfo(event)><title>Field '+str(row[0])+'</title></rect>'

    conn.close()

    return html, fillc_dict

#################################### FINDS ###################################

def findsHtml():
    # taking the users pre-determined values for the svg
    n = col.findColour() # column number determining fill colour (from dict)
    column, value = fil.findSelect()
    filter = fil.QueryBuilder(column, value) # query determining which rows are returned

    # set up of empty and default variables
    html = ''
    fillc = "#fff" # default for integrity
    fillc_dict = {
    "DEFAULT": "#fff"
    } # default for integrity

    #colour dictionary for reference
    find_colour_dict = {
    "FLINT": "#e6194b",
    "METAL_WORK": "#42d4f4",
    "BONE": "#ffe119",
    "SHARD": "#469990",
    "MESOLITHIC": "#3cb44b",
    "RECENT": "#f032e6",
    "BRONZE": "#42d4f4",
    "IRON_AGE": "#4363d8",
    "DOMESTIC": "#F08080",
    "DECORATIVE": "#33FFDD",
    "HUNTING": "#8D018F",
    "FOOD": "#FBFF00"
    }

    #oracle connection and querying
    conn = cx_Oracle.connect(dsn="geoslearn", user="s1434165", password=pw)
    c = conn.cursor()
    c.execute("SELECT GISTEACH.FINDS.FIND_ID, GISTEACH.FINDS.XCOORD, GISTEACH.FINDS.YCOORD, GISTEACH.FINDS.DEPTH, GISTEACH.FINDS.FIELD_NOTES, GISTEACH.CLASS.NAME, GISTEACH.CLASS.PERIOD, GISTEACH.CLASS.USE FROM GISTEACH.FINDS, GISTEACH.CLASS WHERE GISTEACH.FINDS.TYPE = GISTEACH.CLASS.TYPE"+filter)

    # loop through sql query result
    for row in c:
        for i in find_colour_dict.keys():
            if row[n] == i: # matching entity column value with colour
                fillc = find_colour_dict[i]
                fillc_dict[i] = fillc
        #integration of query result with html
        html = html + '\n           <circle class="zoom" id='+str(row[0])+' cx= ' + str(row[1]) + ' cy= ' + str(row[2]) + ' r="0.15" fill="'+str(fillc)+'" onClick="findInfo(event)" depth="'+str(row[3])+' m" field_notes="'+str(row[4]).capitalize()+'" type="'+str(row[5]).capitalize()+'" era="'+str(row[6]).capitalize()+'" use="'+str(row[7]).capitalize()+'"><title>Find ' + str(row[0]) +'</title></circle></a>'

    conn.close()

    return html, fillc_dict
