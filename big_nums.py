# Module for representing big numbers

def shorten_value(value):
    value = str(value)
    if 7 <= len(value) <= 9: # million
        if value[-6:] == "000000":
            value = value[:-6] + "M"
        else:
            mil = value[:-6]
            ht = value[-6:-5]
            value = f"{mil}.{ht}M"
        
    return value