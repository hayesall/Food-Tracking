# Copyright © 2021 Alexander L. Hayes

import os
from datetime import datetime
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import pytz
import seaborn as sns

import plotly.express as px


"""
My phone names images according to the pattern:

```
PXL_20210421_232845867.jpg
```

Where `20210421` represents 2021-04-21 and
`23:28:45.867` represents 19:28 PM (GMT-04:00).

Notice that the timestamps are stored in GMT, so we'll have to adjust to make
sure they make sense in EST.
"""

data = os.listdir("data/")


def parse_file_name(file_name):
    n_periods = Counter(file_name)["."]
    return file_name.split(".")[0].split("PXL_")[1]


class ESTLocalizer:

    def __init__(self):
        self.gmt = pytz.timezone("GMT")
        self.eastern = pytz.timezone("US/Eastern")

    def localize(self, stamp):
        date = datetime.strptime(stamp[:-3], "%Y%m%d_%H%M%S")
        dategmt = self.gmt.localize(date)
        return dategmt.astimezone(self.eastern)

if __name__ == "__main__":

    localizer = ESTLocalizer()

    stamps = []
    weekdays = []

    for fname in data:

        stamp = localizer.localize(parse_file_name(fname))

        stamps.append("1/1/2021 {}:{}".format(stamp.hour, stamp.minute))

        if stamp.strftime("%A") in ["Saturday", "Sunday"]:
            weekdays.append("Weekend")
        else:
            weekdays.append("Weekday")

    data = pd.DataFrame({"Stamps": stamps, "Weekday": weekdays})
    data["Stamps"] = pd.to_datetime(data["Stamps"])

    print(data)

    fig = px.histogram(data, x="Stamps", color="Weekday")
    fig.show()
