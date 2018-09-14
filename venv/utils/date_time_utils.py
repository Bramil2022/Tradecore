import time

class DateTimeUtils():
    """Class with methods which work with date and time"""

    '''
    Returns current date as timestamp timestamp
    Useful for making uniqe objects (such as emails)
    @return timestamp
    '''
    def get_timestamp(self):
        timestamp = time.time()
        timestamp = round(timestamp)
        return timestamp

