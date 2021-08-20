

def format_time(the_time):

    the_time = str(the_time)
    if len(the_time) == 1:
        the_time = '0' + the_time
    
    return the_time
