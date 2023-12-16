# get a monthly breakdown of most-played songs
from utils import *
from secret_config import *

song_history = read_song_history(SONG_HISTORY_FILEPATH)
month_stats = dict()

for date, song_name in song_history:
    month = date[:2]
    if month not in month_stats.keys():
        month_stats[month] = {}
    month_dict = month_stats[month]
    month_dict[song_name] = month_dict.get(song_name, 0) + 1

for month in sorted(month_stats.keys()):
    month_list = list(month_stats[month].items())
    month_list.sort(key=lambda a: a[1], reverse=True)
    print('\n\n' + str(month))
    for it in month_list[:10]:
        print(str(it[1]) + '\t' + it[0])
