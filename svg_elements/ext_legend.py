#!/usr/bin/env python3

import cgi
import cgitb
import svg_elements.geometric as svgg

cgitb.enable(format='text')

"""
    This module consists of functions which dynamically integrates the colours
    used to draw the svg (previously determined in other functions)
    with svg and html code to form the legend below the svg telling the user which
    colours (and the related category) are currently in use
"""

############### Extract colours being used to draw the svg ######################

def legendColours(): # enables a dynamic legend
    # extraction of (input and) colours used to draw svg (based on user choice) in previous functions
    fieldsInp, fieldsColours = svgg.fieldsHtml()
    findsInp, findsColours = svgg.findsHtml()

    # inputting these colours into function which converts them into an svg to later integrate into the table
    findc_html = legendColSelection(findsColours)
    fieldc_html = legendColSelection(fieldsColours)

    # return this unique svg
    return findc_html, fieldc_html


############# Dynamically draw svg in legend showing the colours/categories which are live ###############

def legendColSelection(x): # asking for any x (dict) to parse variable and colour into svg code
    # set up of svg html
    html = '\n   <svg width=121px height=21px>\n    <g style=stroke:black;stroke-width:1>\n'
    i = 0 # default start position for rectangle

    for var, vals in x.items(): # take variable name as title and fill associated colour value
        html = html + '         <rect style=cursor:help x='+str(i)+' y=1 width=20px height=20px fill="'+str(vals)+'"><title>'+str(var).capitalize()+'</title></rect>\n'
        i = i + 20 # move along 20px (size of rect) for each rect drawn

    # ending the svg code
    html = html + '     </g>\n   </svg>\n'

    return html
