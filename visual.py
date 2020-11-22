# Python program to convert
# CSV to HTML Table


import pandas as pd
a = pd.read_csv("law-firm-details.csv")
a.to_html("law-firm-details.html")
html_file = a.to_html()