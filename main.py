import pandas as pd
import math

df_popolazione = pd.read_csv("popolazione.csv")[["Country Name", "Country Code", "2023"]]
df_coordinate = pd.read_csv("coordinate.csv")[["Alpha-3 code", "Latitude (average)", "Longitude (average)"]]



### z earth axis, x towards Greenwich, y accordingly

Fx = 0
Fy = 0
Fz = 0


for index, paese in df_coordinate.iterrows():
    popolazione = df_popolazione[df_popolazione["Country Code"] == paese["Alpha-3 code"]]
    if popolazione.size == 0:
        continue

    name = popolazione['Country Name'].iloc[0]
    pop = int(popolazione["2023"].iloc[0])
    lat = paese["Latitude (average)"] * math.pi / 180
    lon = paese["Longitude (average)"] * math.pi / 180

    print(f"Adding the contribution of {name} ({pop} inhabitants)")

    Fx += pop * math.cos(lat) * math.cos(lon)
    Fy += pop * math.cos(lat) * math.sin(lon)
    Fz += pop * math.sin(lat)



longitudine = [math.atan(Fy/Fx) * 180 / math.pi,
               math.atan(Fy/Fx) * 180 / math.pi - 180]
latitudine = [math.atan(Fz/math.sqrt(pow(Fy,2) + pow(Fx,2))) * 180 / math.pi,
              - math.atan(Fz/math.sqrt(pow(Fy,2) + pow(Fx,2))) * 180 / math.pi]



print(f"The axis goes through\n({latitudine[0]}, {longitudine[0]}) - Afghanistan\n({latitudine[1]}, {longitudine[1]}) - Southern Pacific Ocean")