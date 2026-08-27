import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading csv
data = pd.read_csv("Depth Data.csv")

#converts data to numeric and invalid ones become missing values
depth = pd.to_numeric(data["Depth (m)"], errors="coerce")
time = np.arange(len(depth))

print("Number of readings:", len(depth))
print("Invalid readings:", depth.isna().sum())

# identify invalid readings and also detect outliers in the dataset
bad_readings = depth.isna() | (depth >= 0)


valid = depth[~bad_readings]

#we use median and mad to indetify unsual readings without being affected by the outliers
median = valid.median()
mad = (valid - median).abs().median()

#multiplied mad by 6 here to take a conservative threshold for what we consider as acceptable data. anything more than 6 deviations is considered an outlier
lower_limit = median - 6 * mad
upper_limit = median + 6 * mad

bad_readings = bad_readings | (depth < lower_limit) | (depth > upper_limit)

print("bad_readings readings:")
print(data.loc[bad_readings, ["Point", "Depth (m)"]])

#removes the bad/invalid readings and makes them missing values
depth_clean = depth.copy()
depth_clean[bad_readings] = np.nan

#estimates missing reading by interpolation
depth_clean = depth_clean.interpolate()
depth_clean = depth_clean.bfill().ffill()

#smoothen small variations
depth_smooth = depth_clean.rolling(
    window=5,
    center=True
).mean()

depth_smooth = depth_smooth.bfill().ffill()

plt.figure(figsize=(10, 6))

plt.plot(
    time,
    depth,
    ".",
    alpha=0.4,
    label="Raw data"
)

plt.plot(
    time,
    depth_smooth,
    linewidth=2,
    label="Clean data"
)

#marks all invalid/rejected readings
plt.scatter(
    time[bad_readings],
    depth[bad_readings],
    marker="x",
    s=60,
    label="Corrupted Readings"
)

plt.xlabel("Time (s)")
plt.ylabel("Depth (m)")
plt.title("Ship Depth vs Time")

plt.grid()
plt.legend()
plt.show()

import plotly.graph_objects as go

frames = []

#makes animation for each time step to see the data progressively
for i in range(len(time)):
    frames.append(
        go.Frame(
            data=[
                go.Scatter(
                    x=time[:i + 1],
                    y=depth_smooth[:i + 1],
                    mode="lines+markers"
                )
            ]
        )
    )

fig = go.Figure(
    data=[
        go.Scatter(
            x=time[:1],
            y=depth_smooth[:1],
            mode="lines+markers",
            name="Depth"
        )
    ],
    frames=frames
)

fig.update_layout(
    title="Ship Depth vs Time",
    xaxis_title="Time (s)",
    yaxis_title="Depth (m)",
    xaxis=dict(range=[time.min(), time.max()]),
    yaxis=dict(
        range=[
            depth_smooth.min() - 20,
            depth_smooth.max() + 20
        ]
    ),
    updatemenus=[
        {
            "type": "buttons",
            "buttons": [
                {
                    "label": "Play",
                    "method": "animate",
                    "args": [
                        None,
                        {
                            "frame": {
                                "duration": 1000,
                                "redraw": True
                            },
                            "fromcurrent": True
                        }
                    ]
                }
            ]
        }
    ]
)

fig.show()