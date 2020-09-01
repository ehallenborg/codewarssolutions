def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    seconds = seconds - (hours * 3600) - (minutes * 60)
    
    return '%02d:%02d:%02d' % (hours, minutes, seconds)