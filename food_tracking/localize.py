# Copyright 2021 Alexander L. Hayes

"""
All names are stored in terms of GMT, but everything in Alexander's
schedule makes more sense if viewed in terms of Eastern Standard Time
(GMT-4:00). This is a collection of objects for localizing timezones.
"""

from datetime import datetime

import pytz


class ESTLocalizer:

    def __init__(self):
        self.gmt = pytz.timezone("GMT")
        self.eastern = pytz.timezone("US/Eastern")
    
    def localize(self, stamp):
        date = datetime.strptime(stamp[:-3], "%Y%m%d_%H%M%S")
        dategmt = self.gmt.localize(date)
        return dategmt.astimezone(self.eastern)
