"""
`string = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'`
7. Get date from string
"""
def find_date(i_str="Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"):
    import re
    match = re.findall(r'\d\d\-\d\d\-\d\d\d\d', i_str)
#   print(match)
    return(match)

#find_date()