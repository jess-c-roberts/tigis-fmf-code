import cgi
import cgitb

cgitb.enable(format='text')

_all__ = ['filter_selection']

form = cgi.FieldStorage()

"""
    This module contains three functions which ultimately take the user's choice
    of what they want to display, for fields and finds, and construct the corrected
    query language in preparation for use in other functions. General pattern is...

    # STEP ONE: Take user's choice
    # STEP TWO: Validate choice (check if its empty or 'all' ie no filter)
    # STEP THREE: Assign relevent SQL snippets based on choice (from dictionary)
    # STEP FOUR: Output two halves, (1) is the column to query, (2) is the value to check for

    Then take column (1) and value (2) from fields / fields and built into a query
    that can be integrated

    # STEP FIVE: Test the value to determine its formatting
    # STEP SIX: Query is ready for integration with other functions!
"""

############################## STEP FIVE AND SIX ###############################

def QueryBuilder(column, value): # take column and value from field/find selection functions
    query = ''

    test_char = value[0] # taking first character to test for numerical criteria for between statements

    # query language formatting for integration
    if test_char.isdigit() == True or value == 'GISTEACH.FIELDS.CROP' or value == 'GISTEACH.FINDS.TYPE': # if its a number OR the default (redundant) value
        query = column + value # no quotation marks necessary
    else:
        # if its a custom verbose query then quote and capitalize the filter selected
        query = column + "'" + str(value).upper() + "'"

    return query # return the total query statement


###############################################################################
########################### FIELD SELECTION FUNCTION ##########################
####### TAKING THE USER CHOICE OF FIELD SELECTION AND VALIDATING IT ###########
###############################################################################

def fieldSelect():
    ##### set up of empty variables #####
    column = ''

    ##### retrieving user choice #####
    sel = form.getvalue('field-sel') # selection of filter type (column) by user
    choice = form.getvalue('field-filter') # selection of filter (value) by user

    ###### controlling for null field or user selection of 'all' ######
    if sel == None or sel == 'all': # if nothing has been chosen for a filter
        sel = 'default'
        choice = 'GISTEACH.FIELDS.CROP' # add a redundant query
    else:
        sel = sel # otherwise keep all the same

    ###### dictionary relating user choice of filter with relevant column in database ########
    field_query_dict = {
    'ids': ' AND GISTEACH.FIELDS.FIELD_ID = ',
    'crops': ' AND GISTEACH.CROPS.NAME = ',
    'owner': ' AND GISTEACH.FIELDS.OWNER = ',
    'area': ' AND GISTEACH.FIELDS.AREA BETWEEN ',
    'default': ' AND GISTEACH.CROPS.CROP = '
    }

    ####### customising query using dictionary according to the user choice ##########
    for i in field_query_dict.keys():
        if sel == i: # matching entity column value with selected filter
            column = field_query_dict[i]
            choice = choice
            break # if it matches then stop and keep that variable value
        elif sel != i: # if it doesn't match then continue looking through dict
            continue
        else: # if it matches none then set a default but redundant addition so query will still run (reversed but same join)
            column = ' AND GISTEACH.CROPS.CROP = ' # redundant additions
            choice = 'GISTEACH.FIELDS.CROP' # redundant additions

    return column, choice # return the relevant database column and user choice after necessary tests


###############################################################################
########################### FIND SELECTION FUNCTION ###########################
####### TAKING THE USER CHOICE OF FIELD SELECTION AND VALIDATING IT ###########
###############################################################################

def findSelect():
    #set up of empty default values
    column = ''

    ######## retrieving user choice ###########
    sel = form.getvalue('find-sel') # users selection of column type
    choice = form.getvalue('find-filter') # users choice of column value

    ####### controlling for null field or user selection of 'all' #########
    if sel == None or sel == 'all':
        sel = 'default'
        choice = 'GISTEACH.FINDS.TYPE'
    else:
        sel = sel

    find_query_dict = {
    'ids': ' AND GISTEACH.FINDS.FIND_ID = ',
    'eras': ' AND GISTEACH.CLASS.PERIOD = ',
    'types': ' AND GISTEACH.CLASS.NAME = ',
    'uses': ' AND GISTEACH.CLASS.USE = ',
    'default': ' AND GISTEACH.CLASS.TYPE = '
    }

    # customising query using dictionary according to the user choice
    for i in find_query_dict.keys():
        if sel == i: # matching entity column value with selected filter
            column = find_query_dict[i]
            choice = choice
            break # if it matches then stop and keep that variable value
        elif sel != i: # if it doesn't match then continue looking through dict
            continue
        else: # if it matches none then set a default but redundant addition so query will still run (reversed but same join)
            column = ' AND GISTEACH.CLASS.TYPE = ' # redundant additions
            choice = 'GISTEACH.FINDS.TYPE' # redundant additions

    return column, choice
