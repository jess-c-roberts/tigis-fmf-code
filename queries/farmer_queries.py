#!/usr/bin/env python3

import cx_Oracle
import cgi
import datetime
from jinja2 import Environment, FileSystemLoader

with open("/web/s1434165/public_html/static/pw/pw.txt","r") as pwf:
    pw = pwf.read().strip()

"""
    This script of 1 of 2 potential pathways from the user.
    It comprises 4 main parts which take the user's choice, turn it into a valid
    query string, run that query through Oracle, and return a relevant
    introductory phrasing for the results box. This is all brought together
    by the final function results_html()
"""

form = cgi.FieldStorage()

# Pulling everything together for the output page
def results_html():
    env = Environment(loader=FileSystemLoader('../../../templates'))
    temp = env.get_template('results_page.html') # get the generic results page html
    intro, checkpoint2 = introHtml() # get the intro text with its relevant checkpoint
    if checkpoint2 == 0: # the query worked fine
        results = QueryUse() # so show the results
    else: # the query was set to default due to a fault
        results = '' # so don't know any results

    image = "farmer-results-page" # defining the background class of the results

    print(temp.render(results=results, intro=intro, image=image))

# Customising the introduction to correct English based on the results
def introHtml():
    checkpoint2 = 0 # Flag for results_html() whether to display results

    # Set up of variables
    html = ''
    html_var1 = ''
    html_var2 = ''
    # Getting validated user-variables
    query, u_target, u_criteria, u_choice1, u_choice2, chp1 = farmerQuery()

    # Selecting variants of English based on the criteria chosen by the user
    if u_criteria in ('crop','owner'):
        html_var1 = ' or '
        html_var2 = ' of '
    elif u_criteria in ('x_location','y_location', 'area'):
        html_var1 = ' and '
        html_var2 = ' between '
    elif u_criteria == 'season':
        u_choice1 = dateFormat(u_choice1)
        u_choice2 = dateFormat(u_choice2)
        html_var1 = ' and '
        html_var2 = ' between '
    elif u_criteria == 'Field_ID':
        html_var2 = ' = '
        html_var1 = ', '
    else:
        html_var1 = ' and/or/between ' # default in event of failure

    # This checks if the previous function farmerQuery() set the choices to be
    # the same for query integrity. This would have happened if the user did
    # not make a second choice for the query filter.
    if u_choice2 == u_choice1:
        u_choice2 = ''
        html_var1 = ''
        html_var2 = ' of '

    # Integrating english variables with HTML and the revelant user variables
    html = '<p style=color:#fff>The following ' + str(u_target) + '(s) have a ' + str(u_criteria) + str(html_var2) + str(u_choice1) + str(html_var1) + str(u_choice2) + ':</br>'

    # Using checkpoint of customQuery() to check whether the query failed
    if chp1 == 0: # set by customQuery() in the event of failure
        html = '<p style=color:#fff>Sorry! You did not complete the query properly. Try again.</p>'
        checkpoint2 = 1 # Flag for results display
    elif None in (u_target, u_criteria, u_choice1): # in case of checkpoint failure
        html = '<p style=color:#fff>Sorry! You did not complete the query properly. Try again.</p>'
        checkpoint2 = 1 # Flag for results display
    else:
        html = html # If the query appears to have worked, ignore the above!

    return html, checkpoint2

# Returning the month name for the season date variable
def dateFormat(mydate):
        # Turn date string into datetime format
        mydate_strip = datetime.datetime.strptime(mydate, "%d-%b-%Y")
        # Reformat that datetime format into month
        mydate_new = mydate_strip.strftime("%B")

        return mydate_new

# Running validated SQL query string from farmerQuery() through Oracle
def QueryUse():
    # Getting the validated query string and variables
    query, u_target, u_criteria, u_choice1, u_choice2, chp = farmerQuery()

    html = ''

    conn = cx_Oracle.connect(dsn="geoslearn", user="s1434165", password=pw)
    c = conn.cursor()
    c.execute(""+str(query)+"") # Use my query!

    for row in c:
        html = html + str(row[0]).capitalize() + '<br>' # List the results

    conn.close()

    return html

def farmerQuery():
    # Set up of empty variables for query
    target = ''
    criteria1 = ''
    criteria2 = ''
    add1 = ' = '
    add2 = ''
    add3 = "'"
    # Flag for introHtml() to indicate whether the query failed
    checkpoint1 = 0

    u_target = form.getvalue('target') # User's choice of target results
    u_criteria = form.getvalue('criteria') # User's choice of result criteria
    u_choice1 = form.getvalue('choice1') # User's custom criteria
    u_choice2 = form.getvalue('choice2') # Second value where necesssary/desired

    # Dictionary containing the necessary SQL joiners between the relevant
    # variables being tested. These comprise:
    # [add1,add2,checkpoint1]
    query_dict = {
    'Field_ID': [' = ','', 1],
    'crop': [' = ', '', 1],
    'owner': [' = ', '', 1],
    'area': [' BETWEEN ',  '', 2],
    'x_location': [' >= ', ' <= ', 3],
    'y_location': [' >= ', ' <= ', 3],
    'season': [' >= ', ' <= ', 3]
    }

    # Checking the criteria submitted is relevant
    # Assigning the associated SQL joiners / checkpoint
    for k in query_dict.keys():
        if u_criteria == k:
            add1 = query_dict[k][0]
            add2 = query_dict[k][1]
            checkpoint1 = query_dict[k][2]
            break

    # Dictionary containing the relevant database column for
    # the SELECT variable
    target_dict = {
    'Field_ID': 'GISTEACH.FIELDS.FIELD_ID',
    'owner': 'GISTEACH.FIELDS.OWNER',
    'crop': 'GISTEACH.CROPS.NAME',
    'area': 'GISTEACH.FIELDS.AREA',
    'Find_ID': 'GISTEACH.FINDS.FIND_ID',
    'Find_era': 'GISTEACH.CLASS.PERIOD',
    'Find_type': 'GISTEACH.CLASS.NAME',
    'Find_use': 'GISTEACH.CLASS.USE'
    }


    # Checking the target submitted is relevant
    # Assigning the associated SELECT column
    for i in target_dict.keys():
        if u_target == i:
            target = target_dict[i]
            break
        else:
            target = '*' # else select everything (default)

    # Checking if the user selected a second variable
    if u_choice2 in ('none', None): # if they didn't
        u_choice2 = u_choice1 # make it equal to the first choice1
        # Ensuring the query still runs without a second choice
        # but not return any extra results
    else:
        u_choice2 = u_choice2 # otherwise, keep as is!

    # Checking if the user selected a first variable
    if u_choice1 in ('none', None): # if they didn't
        u_choice1 = '<!-- choice 1 -->' # set choice to be redundant
        checkpoint1 = 0 # Flag for query selection
        # This means a query will still run but as nothing was selected
        # it will just be a generic default
    else:
        u_choice1 = u_choice1 # otherwise, keep as is!

    # Checking if the user selected a numerical variable
    if u_choice1.isdigit() == True:
        add3 = '' # remove quotation marks
    else:
        add3 = add3 # if its not a digit, keep the quotation marks

    # Dictionary containing the relevant columns to test with WHERE statement
    # Each criteria has two columns for integrity (to ensure ranges can be tested)
    # as well as multiple values (max 2)
    criteria_dict = {
    'season': ['GISTEACH.CROPS.START_OF_SEASON', 'GISTEACH.CROPS.END_OF_SEASON'],
    'Field_ID': ['GISTEACH.FIELDS.FIELD_ID','GISTEACH.FIELDS.FIELD_ID'],
    'crop': ['GISTEACH.CROPS.NAME', 'GISTEACH.CROPS.NAME'],
    'owner': ['GISTEACH.FIELDS.OWNER', 'GISTEACH.FIELDS.OWNER'],
    'area': ['GISTEACH.FIELDS.AREA', 'GISTEACH.FIELDS.AREA'],
    'x_location': ['GISTEACH.FIELDS.LOWX', 'GISTEACH.FIELDS.HIX'],
    'y_location': ['GISTEACH.FIELDS.LOWY', 'GISTEACH.FIELDS.HIY']
    }

    # Checking if the criteria submitted is valid
    # Assigned each of the columns to query variable
    for i in criteria_dict.keys():
        if u_criteria == i:
            criteria1 = criteria_dict[i][0]
            criteria2 = criteria_dict[i][1]
            break

    # Begin the query
    query = 'SELECT ' +str(target)

    # If they are asking for finds
    if u_target in ('Find_ID', 'Find_era', 'Find_type', 'Find_use'):
        # Make all the necessary spatial etc joins
        query = query + ' FROM GISTEACH.FINDS, GISTEACH.FIELDS, GISTEACH.CROPS, GISTEACH.CLASS WHERE GISTEACH.FINDS.XCOORD BETWEEN GISTEACH.FIELDS.LOWX AND GISTEACH.FIELDS.HIX AND GISTEACH.FINDS.YCOORD BETWEEN GISTEACH.FIELDS.LOWY AND GISTEACH.FIELDS.HIY AND GISTEACH.FIELDS.CROP = GISTEACH.CROPS.CROP AND GISTEACH.FINDS.TYPE = GISTEACH.CLASS.TYPE AND ('
    else: # Else just join the fields and crops
        query = query + ' FROM GISTEACH.FIELDS, GISTEACH.CROPS WHERE GISTEACH.FIELDS.CROP = GISTEACH.CROPS.CROP AND ('

    if checkpoint1 == 1: # Testing for two different values of same column
        query = query + str(criteria1) + str(add1) + str(add3) + str(u_choice1).upper() + str(add3) + ' OR ' + str(criteria1) + str(add1) + str(add3) + str(u_choice2).upper() + str(add3) + ') GROUP BY ' + str(target)
    elif checkpoint1 == 2: # Testing if something falls within a range of values in one column
        query = query + str(criteria1) + str(add1) + str(u_choice1) + ' AND ' + str(u_choice2) + ') GROUP BY ' + str(target)
    elif checkpoint1 == 3: # Testing if something falls within two values in two columns
        query = query + str(criteria1) + str(add1) + str(add3) + str(u_choice1) + str(add3) + ' AND ' + str(criteria2) + str(add2) + str(add3) + str(u_choice2) + str(add3) + ') GROUP BY ' + str(target)
    else:
        query = 'SELECT * FROM GISTEACH.FIELDS, GISTEACH.CROPS WHERE GISTEACH.FIELDS.CROP = GISTEACH.CROPS.CROP'

    return query, u_target, u_criteria, u_choice1, u_choice2, checkpoint1


if __name__ == '__main__':
    results_html()
