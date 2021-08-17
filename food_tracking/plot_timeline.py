# Copyright 2021 Alexander L. Hayes

"""
Plot a timeline showing how many photos were taken on each day.
"""

from .localize import ESTLocalizer

import pandas as pd
import plotly.express as px


def parse_file_name(file_name):
    return file_name.split(".")[0].split("PXL_")[1]

df = pd.read_csv("out.csv")
localizer = ESTLocalizer()

stamps = []
for name in df["fname"]:
    stamps.append(localizer.localize(parse_file_name(name)))

fig = px.histogram(stamps)
fig.update_traces(xbins_size="D1")
fig.update_layout(bargap=0.1)

fig.write_html("index.html")
