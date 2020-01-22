#!/usr/bin/env python3

# importing external packages
import cgi
import cgitb
from jinja2 import Environment, FileSystemLoader

# importing custom built packages and modules
import svg_elements.geometric as svgg
import svg_elements.labels as svgl
import svg_elements.ext_legend as lgd

cgitb.enable('text')

# connecting to the html forms posted by the user
form = cgi.FieldStorage()

"""
    This is the main script for the mapping page of the site. It brings together
    the templated header html, the svg (map) html and the dynamic legend html
    all into their rightful place in the map page html.
"""


def main_html():
    env = Environment(loader=FileSystemLoader('../../templates'))
    temp = env.get_template('map_page.html') # getting overall page template
    header = header_html() # getting static header html
    svg_render = svg_html() # getting dynamic svg html
    legend_render = legendHtml() # getting dynamic legend html
    print(temp.render(head_parent=header, svg=svg_render, legend=legend_render)) #integrating all the blocks of html built


################################# HEADER ####################################
# Retrieval of the header html, containing the navigation, stylesheets and scripts

def header_html():
    env = Environment(loader=FileSystemLoader('../../templates'))
    temp = env.get_template('template.html')
    return(temp.render())


################################# SVG MAP #######################################
# Integration of all the coded svg elements into a skeleton svg html template file

def svg_html():
    env = Environment(loader=FileSystemLoader('../../templates'))

    # getting base svg html which has pattern and transform set ups in place
    temp = env.get_template('svg.html')

    #filling with various separated elements, grouped separately for clarity
    fieldsInp, fieldsColours = svgg.fieldsHtml()
    findsInp, findsColours = svgg.findsHtml()
    fieldsIDinp = svgl.fields_IDhtml()
    findsIDinp = svgl.finds_IDhtml()
    gridLabels = svgl.labelsHtml()

    return(temp.render(fields = fieldsInp, finds = findsInp, fields_ID = fieldsIDinp, finds_ID = findsIDinp, grid_labels=gridLabels)) #integration


################################ LEGEND ##########################################
# Taking the final user choices and creating a dynamic legend from it

def legendHtml():
    # set up of variables
    html = ''
    findc_svg, fieldc_svg = lgd.legendColours() # extraction of svg html code for fields and finds

    # storing user chosen values as variables in dictionary for extraction later in code
    x = {
    'find_sel': form.getvalue('find-sel'),
    'find_filter': form.getvalue('find-filter'),
    'field_sel': form.getvalue('field-sel'),
    'field_filter': form.getvalue('field-filter'),
    'find_disp': form.getvalue('find-disp'),
    'field_disp': form.getvalue('field-disp')
    }

    # checking if user has chosen a value
    for var, val in x.items():
        if val == None:
            x[var] = 'None' # if they haven't, return the string 'none' so the code may continue
        else:
            val = val # else use the user's choice

    # integrate users choice with a 'results' legend table, alongside svg displaying associated colours in the 'key' column
    html = html + "\n<table class='legend-table center'>\n<tr><th>Element</th>\n<th>Category</th>\n<th>Subvalue</th>\n<th>Colour</th>\n<th style=text-align:left>Key</th>\n</tr>\n<tr><td>Fields</td>\n<td>" +str(x['field_sel']).capitalize()+ "</td>\n<td>" +str(x['field_filter']).capitalize()+ "</td>\n<td>" +str(x['field_disp']).capitalize()+ "</td>\n<td>"+fieldc_svg+"</td>\n</tr><tr>\n<td>Finds</td>\n<td>" +str(x['find_sel']).capitalize()+ "</td>\n<td>" +str(x['find_filter']).capitalize()+ "</td><td>\n" +str(x['find_disp']).capitalize()+ "</td>\n<td>"+findc_svg+"</td></tr>\n</table>"

    return html



if __name__ == '__main__':
    main_html()
