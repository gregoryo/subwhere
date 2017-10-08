"""
Global helpers function
"""


from datetime import datetime as dt, date
import math


def clean_json_type(data):
    """
    Read the data information and change all the date/datetime by their
    strftime YYYY-MM-DD HH:MM:SS counterpart. Other objects are transformed
    into string
    """
    if isinstance(data, dt):
        return data.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(data, date):
        return data.strftime('%Y-%m-%d')
    elif isinstance(data, float) and (data in (float('inf'), float('-inf')) \
            or math.isnan(data)):
        return None
    elif isinstance(data, dict):
        for idx in data:
            data[idx] = clean_json_type(data[idx])
    elif isinstance(data, (tuple, list)):
        newdata = list()
        for idx in xrange(len(data)):
            newdata.append(clean_json_type(data[idx]))
        return newdata
    elif data is not None and not isinstance(data, (int, unicode, str, float)):
        return str(data)
    return data