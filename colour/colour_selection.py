import cgi
import cgitb

cgitb.enable(format='text')

_all__ = ['colour_selection']

form = cgi.FieldStorage()

"""
    This module contains two simple functions (one for fields and one for finds)
    which determine the column number of the database to use in the SQL query
    when drawing the svg, based on the user's choice of what to display.
"""

############################ FIELDS ############################################

def fieldColour():
    # getting users display choice and set up of variables
    fieldc = form.getvalue('field-disp')
    n = ''

    # setting up the row number needed to query for colour choice, using 0 as default
    if fieldc == "plain":
        n = 0
    elif fieldc == "crop":
        n = 7
    elif fieldc == "farmer":
        n = 6
    else:
        n = 0

    return n

############################# FINDS #########################################

def findColour():
    # getting users display choice and set up of variables
    findc =  form.getvalue('find-disp')
    n = ''

    # setting up the row number needed to query for colour choice, using 0 as default for integrity
    if findc == "plain":
        n = 0 #default
    elif findc == "type":
        n = 5
    elif findc == "era":
        n = 6
    elif findc == "use":
        n = 7
    else:
        n = 0 #default

    return n
