# Author Michael Coppolino
# michael_coppolino@brown.edu

# example data used for testing
dates = [
    {"start_date": "2015-02-04", "end_date": "2017-02-04"},
    {"start_date": "2015-02-04", "end_date": "2016-02-04"},
    {"start_date": "2016-01-01", "end_date": "2017-01-01"},
    {"start_date": "2018-02-04", "end_date": "2019-02-04"},
    {"start_date": "2019-05-06", "end_date": "2019-09-12"},
    {"start_date": "2019-05-06", "end_date": "2019-09-12"},
    {"start_date": "2019-05-06", "end_date": "2019-12-12"},
    {"start_date": "2015-02-04", "end_date": "2016-10-11"},
    {"start_date": "2021-02-04", "end_date": "2022-02-04"}
]

# original version
def find_gaps_v0():
    ordered_dates = sorted(dates, key=lambda x: x['start_date'])

    gaps = []
    latest_end_date = ordered_dates[0]['end_date']
    for index in range(0, len(dates)-1):
        cur_end_date = ordered_dates[index]['end_date']
        if latest_end_date < cur_end_date:
            latest_end_date = cur_end_date

        if latest_end_date >= ordered_dates[index+1]['start_date']:
            continue

        gaps.append({'start_date': latest_end_date,
                     'end_date': ordered_dates[index+1]['start_date']})

    return gaps

# make copy of input and sort in place and change input to range call(redundant)
def find_gaps_v1():
    ordered_dates = dates
    ordered_dates.sort(key=lambda x: x['start_date'])

    gaps = []
    latest_end_date = ordered_dates[0]['end_date']
    for index in range(len(dates)-1):
        cur_end_date = ordered_dates[index]['end_date']
        if latest_end_date < cur_end_date:
            latest_end_date = cur_end_date

        if latest_end_date >= ordered_dates[index+1]['start_date']:
            continue

        gaps.append({'start_date': latest_end_date,
                     'end_date': ordered_dates[index+1]['start_date']})

    return gaps

# append gap immediately instead of continuing if no gap is found
def find_gaps_v2():
    ordered_dates = dates
    ordered_dates.sort(key=lambda x: x['start_date'])

    gaps = []
    latest_end_date = ordered_dates[0]['end_date']
    for index in range(len(dates)-1):
        cur_end_date = ordered_dates[index]['end_date']
        if latest_end_date < cur_end_date:
            latest_end_date = cur_end_date

        if latest_end_date < ordered_dates[index+1]['start_date']:
            gaps.append({'start_date': latest_end_date,
                         'end_date': ordered_dates[index+1]['start_date']})

    return gaps

# refactor code to use an iterator object instead of indexing into list (fast!!)
def find_gaps_v3():
    ordered_dates = dates
    ordered_dates.sort(key=lambda x: x['start_date'])

    gaps = []
    latest_end_date = ordered_dates[0]['end_date']
    for date in ordered_dates:
        if latest_end_date < date['start_date']:
            gaps.append({'start_date': latest_end_date,
                         'end_date': date['start_date']})

        cur_end_date = date['end_date']
        if latest_end_date < cur_end_date:
            latest_end_date = cur_end_date

    return gaps
