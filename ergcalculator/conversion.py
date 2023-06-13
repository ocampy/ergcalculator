def basic_conversion(tminutes, tseconds, sminutes, sseconds, distance):
    try:
        sseconds = float(sseconds)
    except :
        return 'Enter 0 in empty boxes. Only enter numbers.'
    
    try:
        sminutes = float(sminutes)
    except :
        return 'Enter 0 in empty boxes. Only enter numbers.'
    
    try:
        distance = float(distance)
    except :
        return 'Enter 0 in empty boxes. Only enter numbers.'
    
    try:
        tseconds = float(tseconds)
    except :
        return 'Enter 0 in empty boxes. Only enter numbers.'
    
    try:
        tminutes = float(tminutes)
    except :
        return 'Enter 0 in empty boxes. Only enter numbers.'
    
    # calculate time
    if tseconds == 0 and tminutes == 0:
        value = distance / 500
        split = sseconds + sminutes * 60
        tseconds = value * split
        minutes = tseconds / 60
        minutes = int(minutes)
        seconds = tseconds % 60
        result = 'Time: ' + str(minutes) + ':' +str(seconds)
        return result
    # calculate split
    elif sseconds == 0 and sminutes == 0:
        ttime = tminutes * 60 + tseconds
        value = distance / 500
        split = ttime / value
        minutes = split / 60
        minutes = int(minutes)
        seconds = split % 60
        result = 'Split: ' + str(minutes) + ':' + str(seconds)
        return result

    # calculate distance
    elif distance == 0:
        ttime = tminutes * 60 + tseconds
        stime = sseconds + sminutes * 60
        value = ttime / stime
        distance = value * 500
        result = 'Distance: ' + str(distance)
        return result
    else:
        return 'Enter Valid Input'