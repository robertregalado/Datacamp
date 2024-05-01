------------------------------------------------------------------------

## ANALYZING CRIME IN LOS ANGELES 
![Los Angeles skyline](la_skyline.jpg)

Los Angeles, California 😎. The City of Angels. Tinseltown. The
Entertainment Capital of the World!

Known for its warm weather, palm trees, sprawling coastline, and
Hollywood, along with producing some of the most iconic films and songs.
However, as with any highly populated city, it isn\'t always glamorous
and there can be a large volume of crime. That\'s where you can help!

You have been asked to support the Los Angeles Police Department (LAPD)
by analyzing crime data to identify patterns in criminal behavior. They
plan to use your insights to allocate resources effectively to tackle
various crimes in different areas.

## The Data

They have provided you with a single dataset to use. A summary and
preview are provided below.

It is a modified version of the original data, which is publicly
available from Los Angeles Open Data.

# crimes.csv 

| Column        | Description                                                                                                                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `'DR_NO'`     | Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits.                                                                                                                                                   |
| `'Date Rptd'` | Date reported - MM/DD/YYYY.                                                                                                                                                                                                                 |
| `'DATE OCC'`  | Date of occurrence - MM/DD/YYYY.                                                                                                                                                                                                            |
| `'TIME OCC'`  | In 24-hour military time.                                                                                                                                                                                                                   |
| `'AREA NAME'` | The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles. |
| `'Crm Cd Desc'` | Indicates the crime committed.                                                                                                                                                                                                             |
| `'Vict Age'`  | Victim's age in years.                                                                                                                                                                                                                      |
| `'Vict Sex'`  | Victim's sex: `F`: Female, `M`: Male, `X`: Unknown.                                                                                                                                                                                       |
| `'Vict Descent'` | Victim's descent:                                                                                                                                                    |
|                | `<ul>`{=html}<li>{=html}`A` - Other Asian</li>{=html}<li>{=html}`B` - Black</li>{=html}<li>{=html}`C` - Chinese</li>{=html}<li>{=html}`D` - Cambodian</li>{=html}<li>{=html}`F` - Filipino</li>{=html}<li>{=html}`G` - Guamanian</li>{=html}<li>{=html}`H` - Hispanic/Latin/Mexican</li>{=html}<li>{=html}`I` - American Indian/Alaskan Native</li>{=html}<li>{=html}`J` - Japanese</li>{=html}<li>{=html}`K` - Korean</li>{=html}<li>{=html}`L` - Laotian</li>{=html}<li>{=html}`O` - Other</li>{=html}<li>{=html}`P` - Pacific Islander</li>{=html}<li>{=html}`S` - Samoan</li>{=html}<li>{=html}`U` - Hawaiian</li>{=html}<li>{=html}`V` - Vietnamese</li>{=html}<li>{=html}`W` - White</li>{=html}<li>{=html}`X` - Unknown</li>{=html}<li>{=html}`Z` - Asian Indian</li>{=html} |
| `'Weapon Desc'` | Description of the weapon used (if applicable).                                                                                                                                                                                            |
| `'Status Desc'` | Crime status.                                                                                                                                                                                                                               |
| `'LOCATION'`  | Street address of the crime.                                                                                                                                                                                                                |


### How to approach the project?

    1. Finding the frequencies of crimes by the hour of occurrence

    2. Identifying the area with the most night crime

    3. Crimes by age group

### Loading in the required libraries

# Import required libraries

``` python
# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes.head()
```

```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DR_NO</th>
      <th>Date Rptd</th>
      <th>DATE OCC</th>
      <th>TIME OCC</th>
      <th>AREA NAME</th>
      <th>Crm Cd Desc</th>
      <th>Vict Age</th>
      <th>Vict Sex</th>
      <th>Vict Descent</th>
      <th>Weapon Desc</th>
      <th>Status Desc</th>
      <th>LOCATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221412410</td>
      <td>2022-06-15</td>
      <td>2020-11-12</td>
      <td>1700</td>
      <td>Pacific</td>
      <td>THEFT FROM MOTOR VEHICLE - PETTY ($950 &amp; UNDER)</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>13600    MARINA POINT                 DR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>220314085</td>
      <td>2022-07-22</td>
      <td>2020-05-12</td>
      <td>1110</td>
      <td>Southwest</td>
      <td>THEFT OF IDENTITY</td>
      <td>27</td>
      <td>F</td>
      <td>B</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>2500 S  SYCAMORE                     AV</td>
    </tr>
    <tr>
      <th>2</th>
      <td>222013040</td>
      <td>2022-08-06</td>
      <td>2020-06-04</td>
      <td>1620</td>
      <td>Olympic</td>
      <td>THEFT OF IDENTITY</td>
      <td>60</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>3300    SAN MARINO                   ST</td>
    </tr>
    <tr>
      <th>3</th>
      <td>220614831</td>
      <td>2022-08-18</td>
      <td>2020-08-17</td>
      <td>1200</td>
      <td>Hollywood</td>
      <td>THEFT OF IDENTITY</td>
      <td>28</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>1900    TRANSIENT</td>
    </tr>
    <tr>
      <th>4</th>
      <td>231207725</td>
      <td>2023-02-27</td>
      <td>2020-01-27</td>
      <td>0635</td>
      <td>77th Street</td>
      <td>THEFT OF IDENTITY</td>
      <td>37</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>6200    4TH                          AV</td>
    </tr>
  </tbody>
</table>
</div>
```

### 1. Finding the frequencies of crimes by the hour of occurrence 

``` python
# Extract the first two digits from "TIME OCC", representing the hour,
# and convert to integer data type
crimes["HOUR OCC"] = crimes["TIME OCC"].str[:2].astype(int)
```

``` python
# Preview the DataFrame to confirm the new column is correct
crimes.head()
```

```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DR_NO</th>
      <th>Date Rptd</th>
      <th>DATE OCC</th>
      <th>TIME OCC</th>
      <th>AREA NAME</th>
      <th>Crm Cd Desc</th>
      <th>Vict Age</th>
      <th>Vict Sex</th>
      <th>Vict Descent</th>
      <th>Weapon Desc</th>
      <th>Status Desc</th>
      <th>LOCATION</th>
      <th>HOUR OCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221412410</td>
      <td>2022-06-15</td>
      <td>2020-11-12</td>
      <td>1700</td>
      <td>Pacific</td>
      <td>THEFT FROM MOTOR VEHICLE - PETTY ($950 &amp; UNDER)</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>13600    MARINA POINT                 DR</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>220314085</td>
      <td>2022-07-22</td>
      <td>2020-05-12</td>
      <td>1110</td>
      <td>Southwest</td>
      <td>THEFT OF IDENTITY</td>
      <td>27</td>
      <td>F</td>
      <td>B</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>2500 S  SYCAMORE                     AV</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>222013040</td>
      <td>2022-08-06</td>
      <td>2020-06-04</td>
      <td>1620</td>
      <td>Olympic</td>
      <td>THEFT OF IDENTITY</td>
      <td>60</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>3300    SAN MARINO                   ST</td>
      <td>16</td>
    </tr>
    <tr>
      <th>3</th>
      <td>220614831</td>
      <td>2022-08-18</td>
      <td>2020-08-17</td>
      <td>1200</td>
      <td>Hollywood</td>
      <td>THEFT OF IDENTITY</td>
      <td>28</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>1900    TRANSIENT</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>231207725</td>
      <td>2023-02-27</td>
      <td>2020-01-27</td>
      <td>0635</td>
      <td>77th Street</td>
      <td>THEFT OF IDENTITY</td>
      <td>37</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>Invest Cont</td>
      <td>6200    4TH                          AV</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>
```

``` python
# Produce a countplot to find the largest frequency of crimes by hour
sns.countplot(data=crimes, x="HOUR OCC")
plt.show()
```

``` python
# Midday has the largest volume of crime
peak_crime_hour = 12
print(f"Therefore the largest volume of crime is: {peak_crime_hour} NN or MIDDAY!")
```

    Therefore the largest volume of crime is: 12 NN or MIDDAY!

### 2. Identifying the area with the most night crime {#2-identifying-the-area-with-the-most-night-crime}

``` python
## Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? 
## Save as a string variable called peak_night_crime_location
# Filter for the night-time hours
# 0 = midnight; 3 = crimes between 3am and 3:59am, i.e., don't include 4
night_time = crimes[crimes["HOUR OCC"].isin([22,23,0,1,2,3])]
night_time["HOUR OCC"].head()
```

```
    9      0
    12     1
    36     0
    39    23
    42     0
    Name: HOUR OCC, dtype: int64
```
``` python
# Group by "AREA NAME" and count occurrences, filtering for the largest value and saving the "AREA NAME"
peak_night_crime_location = night_time.groupby("AREA NAME", 
                                               as_index=False)["HOUR OCC"].count().sort_values("HOUR OCC",
                                                                                               ascending=False).iloc[0]["AREA NAME"]
```

``` python
# Print the peak night crime location
print(f"The area with the largest volume of night crime is {peak_night_crime_location}")
```


    The area with the largest volume of night crime is Central

### 3. Crimes by age group {#3-crimes-by-age-group}

``` python
## Identify the number of crimes committed against victims by age group (0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+) 
## Save as a pandas Series called victim_ages
# Create bins and labels for victim age ranges
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
```

``` python
# Add a new column using pd.cut() to bin values into discrete intervals
crimes["Age Bracket"] = pd.cut(crimes["Vict Age"],
                               bins=age_bins,
                               labels=age_labels)

# Find the category with the largest frequency
victim_ages = crimes["Age Bracket"].value_counts()
print(victim_ages)
```
```python
    26-34    47470
    35-44    42157
    45-54    28353
    18-25    28291
    55-64    20169
    65+      14747
    0-17      4528
    Name: Age Bracket, dtype: int64
``` python
```

