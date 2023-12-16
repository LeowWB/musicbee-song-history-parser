# reads song history txt file and outputs list corresponding to contents
CHINESE_NUMS = '一二三四五六七八九十'

def read_song_history(filepath):
    with open(filepath, 'rb') as f:
        lines = f.readlines()
    rv = []
    for line in lines:
        line = line.decode('utf-8')
        date, song = line.split('-', 1)
        date = parse_date(date)
        song = song.strip()
        rv.append((date, song))
    return rv

def parse_date(date):
    if date[0] == '星': # chinese
        split_date = date.split(' ')
        date, month, year = split_date[1:4]
        
        date = int(date)
        year = int(year)

        month = month[:-1]
        assert len(month) == 1 or len(month) == 2
        month_num = 0
        for month_char in month:
            month_num += CHINESE_NUMS.index(month_char) + 1

        return (year, month_num, date)
    else: # english
        raise 'date is in english, pls write the code'

