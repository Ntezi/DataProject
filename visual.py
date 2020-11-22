# Python program to convert
# CSV to HTML Table


import pandas as pd
a = pd.read_csv("law-firm.csv")
a.to_html("law-firm.html")

# To generate aw-firm-details table, please un-comment those two line below (line 12 and 13).
# But You will need to comment out line 6 and 7

# a = pd.read_csv("law-firm-details.csv")
# a.to_html("law-firm-details.html")
html_file = a.to_html()