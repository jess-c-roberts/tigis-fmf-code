#!/usr/bin/env python3

import cx_Oracle
import cgi
from jinja2 import Environment, FileSystemLoader

form = cgi.FieldStorage()

with open("/web/s1434165/public_html/static/pw/pw.txt","r") as pwf:
    pw = pwf.read().strip()

"""
    This script of 1 of 2 potential pathways from the user.
    It comprises 4 parts which take the user's choice, turn it into a valid
    query string, run that query through Oracle, and return a relevant
    introductory phrasing for the results box. This is all brought together
    by the final function results_html()
"""

# Pulling everything together
def results_html():
    env = Environment(loader=FileSystemLoader('../../../templates'))
    temp = env.get_template('results_page.html') # results template
    intro, checkpoint2 = introHtml()

    if checkpoint2 == 0: # if the query seems valid
        results = QueryUse() # display its results
    else: # otherwise
        results = '' # show nothing

    image = "archaeo-results-page" # background image class

    print(temp.render(results=results, intro=intro, image=image))

# Customising the intro with relevant English
def introHtml():
    checkpoint2 = 0 # Flag for results_html()
    html = ''
    html_var1 = ''
    html_var2 = ''
    query, u_target, u_criteria, u_choice1, u_choice2, chp1 = archQuery()

    # Relevant English joiners for each type of query used
    if u_criteria in ('use','crop','owner','type','era','comments'):
        html_var1 = ' or '
        html_var2 = ' of '
    elif u_criteria in ('x_location','y_location'):
        html_var1 = ' and '
        html_var2 = ' between '
    elif u_criteria in ('Find_ID','Field_ID'):
        html_var2 = ' = '
        html_var1 = ', '
    else:
        html_var1 = ' and/or/between ' # default in event of failure

    # in the event that the user did not make a different second choice
    if u_choice2 == u_choice1:
        u_choice2 = ''
        html_var1 = ''
        html_var2 = ' of '

    # Integrating English variables with user variables and HTML
    html = '<p style=color:#fff>The following ' + str(u_target) + '(s) have a ' + str(u_criteria) + str(html_var2) + str(u_choice1) + str(html_var1) + str(u_choice2) + ':</br>'

    if chp1 == 0: # flag from archQuery() to indicate the query failed
        html = '<p style=color:#fff>Sorry! You did not complete the query properly. Try again.</p>'
        checkpoint2 = 1 # flag for results_html()
    elif None in (u_target, u_criteria, u_choice1):
        html = '<p style=color:#fff>Sorry! You did not complete the query properly. Try again.</p>'
        checkpoint2 = 1
    else:
        html = html # if all okay, ignore the above!

    return html, checkpoint2

#Taking the validated query and running through Oracle
def QueryUse():
    query, u_target, u_criteria, u_choice1, u_choice2, chp = archQuery()
    html = ''

    conn = cx_Oracle.connect(dsn="geoslearn", user="s1434165", password=pw)
    c = conn.cursor()
    c.execute(""+str(query)+"")

    for row in c: # list the results!
        html = html + str(row[0]).capitalize() + '<br>'

    conn.close()
    return html

# Taking and validating the user's query choices, turning into a valid
# SQL query for Oracle
def archQuery():
    # set up of empty variables for query
    target = ''
    criteria = ''
    add1 = ' = '
    add2 = ''
    add3 = "'"
    checkpoint1 = 0 # flag to indicate any failure (and thus set the default query)

    u_target = form.getvalue('target') # user's choice of target results
    u_criteria = form.getvalue('criteria') # user's choice of result criteria
    u_choice1 = form.getvalue('choice1') # user's custom criteria
    u_choice2 = form.getvalue('choice2') # a range (two values) where necesssary or desired

    # Dictionary containing the necessary SQL joiners between the relevant
    # variables being tested. These comprise:
    # [add1,add2,checkpoint1]
    query_dict = {
    'Find_ID': [' = ','', 1],
    'era': [' = ', '', 1],
    'type': [' = ', '', 1],
    'use': [' = ', '', 1],
    'x_location': [' >= ', ' <= ', 2],
    'y_location': [' >= ', ' <= ', 2],
    'Field_ID': [' = ','', 1],
    'crop': [' = ', '', 1],
    'owner': [' = ', '', 1],
    }

    # Testing the submitted criteria
    for k in query_dict.keys():
        if u_criteria == k: # is it a criteria we were expecting
            add1 = query_dict[k][0]
            add2 = query_dict[k][1]
            checkpoint1 = query_dict[k][2]
            break # set the relevant variables if so

    # Dictionary of column to integrate with SELECT statement
    target_dict = {
    'Find_ID': 'GISTEACH.FINDS.FIND_ID',
    'era': 'GISTEACH.CLASS.PERIOD',
    'type': 'GISTEACH.CLASS.NAME',
    'use': 'GISTEACH.CLASS.USE',
    'comments': 'GISTEACH.FINDS.FIELD_NOTES'
    }

    # Testing if the target is one that's expected
    for i in target_dict.keys():
        if u_target == i:
            target = target_dict[i] # set the variable
            break
        else:
            target = '*' # else select all (default)

    # Testing if user specified a second variable
    if u_choice2 in ('none', None):
        u_choice2 = u_choice1  # make it equal to the first choice1
        # Ensuring the query still runs without a second choice
        # but not return any extra results
    else:
        u_choice2 = u_choice2 # otherwise, keep as is!

    # Testing if user selected a first variable
    if u_choice1 in ('none', None): # if they didn't
        u_choice1 = '<!-- choice 1 -->' # set redundant choice
        checkpoint1 = 0 # Flag for query selection
        # This means a query will still run but as nothing was selected
        # it will just be a generic default
    else:
        u_choice1 = u_choice1 # otherwise, keep as it!

    # Testing if the user chose a numerical variable
    if u_choice1.isdigit() == True: # if so
        add3 = '' # remove quotation marks
    else:
        add3 = add3 # otherwise, keep em!

    # Dictionary containing the relevant columns to test with WHERE statement
    criteria_dict = {
    'Find_ID': 'GISTEACH.FINDS.FIND_ID',
    'era': 'GISTEACH.CLASS.PERIOD',
    'type':'GISTEACH.CLASS.NAME',
    'use': 'GISTEACH.CLASS.USE',
    'x_location':'GISTEACH.FINDS.XCOORD',
    'y_location':'GISTEACH.FINDS.YCOORD',
    'Field_ID': 'GISTEACH.FIELDS.FIELD_ID',
    'crop': 'GISTEACH.CROPS.NAME',
    'owner': 'GISTEACH.FIELDS.OWNER'
    }

    # CHecking the criteria is one of the expected
    for i in criteria_dict.keys():
        if u_criteria == i:
            criteria = criteria_dict[i] # set the variable

    # Begin the query
    query = 'SELECT ' +str(target)

    # If they are asking for fields
    if u_criteria in ('Field_ID', 'crop', 'owner'):
        # Make all the necessary spatial etc joins
        query = query + ' FROM GISTEACH.FIELDS, GISTEACH.CROPS, GISTEACH.FINDS, GISTEACH.CLASS WHERE GISTEACH.FINDS.XCOORD BETWEEN GISTEACH.FIELDS.LOWX AND GISTEACH.FIELDS.HIX AND GISTEACH.FINDS.YCOORD BETWEEN GISTEACH.FIELDS.LOWY AND GISTEACH.FIELDS.HIY AND GISTEACH.FIELDS.CROP = GISTEACH.CROPS.CROP AND GISTEACH.FINDS.TYPE = GISTEACH.CLASS.TYPE AND ('
    else: # Else just join the fields and crops
        query = query + ' FROM GISTEACH.FINDS, GISTEACH.CLASS WHERE GISTEACH.FINDS.TYPE = GISTEACH.CLASS.TYPE AND ('

    if checkpoint1 == 1: # testing for one (or two) values
        query = query + str(criteria) + str(add1) + str(add3) + str(u_choice1).upper() + str(add3) + ' OR ' + str(criteria) + str(add1) + str(add3) + str(u_choice2).upper() + str(add3) + ') GROUP BY ' + str(target)
    elif checkpoint1 == 2: # testing if value falls within range
        query = query + str(criteria) + str(add1) + str(add3) + str(u_choice1) + str(add3) + ' AND ' + str(criteria) + str(add2) + str(add3) + str(u_choice2) + str(add3) + ') GROUP BY ' + str(target)
    else: # checkpoint == 0, default
        query = 'SELECT ' + str(target) +  ' FROM GISTEACH.FINDS, GISTEACH.CLASS WHERE GISTEACH.FINDS.TYPE = GISTEACH.CLASS.TYPE'

    return query, u_target, u_criteria, u_choice1, u_choice2, checkpoint1


if __name__ == '__main__':
    results_html()
