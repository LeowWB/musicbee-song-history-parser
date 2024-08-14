import pandas as pd
import sys
from datetime import date
from utils import *
from secret_config import *

target_year = int(sys.argv[1])

song_history = read_song_history(SONG_HISTORY_FILEPATH)
song_history = [s for s in song_history if s[0][0] == target_year]
song_names = sorted(list(set([s[1] for s in song_history])))
dates_in_year = pd.date_range(date(target_year, 1, 1), date(target_year, 12, 31), freq='d')

df_unsmoothed = pd.DataFrame(0, index=song_names, columns=dates_in_year)

for listen_date, song in song_history:
    listen_date = str(date(*listen_date))
    df_unsmoothed.loc[song, listen_date] += 1

df_smoothed = pd.DataFrame(0, index=song_names, columns=dates_in_year, dtype=float)

for date_in_year in dates_in_year:
    for song_name in song_names:
        if df_unsmoothed[date_in_year][song_name] == 0:
            continue
        df_smoothed.loc[song_name, day_delta(date_in_year, -3)] += df_unsmoothed[date_in_year][song_name] * 0.01
        df_smoothed.loc[song_name, day_delta(date_in_year, -2)] += df_unsmoothed[date_in_year][song_name] * 0.04
        df_smoothed.loc[song_name, day_delta(date_in_year, -1)] += df_unsmoothed[date_in_year][song_name] * 0.2
        df_smoothed.loc[song_name, day_delta(date_in_year, 0)] += df_unsmoothed[date_in_year][song_name] * 0.5
        df_smoothed.loc[song_name, day_delta(date_in_year, 1)] += df_unsmoothed[date_in_year][song_name] * 0.2
        df_smoothed.loc[song_name, day_delta(date_in_year, 2)] += df_unsmoothed[date_in_year][song_name] * 0.04
        df_smoothed.loc[song_name, day_delta(date_in_year, 3)] += df_unsmoothed[date_in_year][song_name] * 0.01

with open('output.csv', 'wb') as f:
    df_smoothed.to_csv(f)
