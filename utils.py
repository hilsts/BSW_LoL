from datetime import datetime, timedelta


def create_weeks_ranges(initial_date):
    today = datetime.today()
    today = datetime(today.year, today.month, today.day, 0, 0)
    initial_date = datetime.fromisoformat(initial_date)
    print(f'today: {today}')
    print(f'initial: {initial_date}')
    x = today - initial_date
    total_day = x.days
    print(f'total days: {total_day}')
    weeks = int(total_day / 7)

    print(f'weeks: {weeks}')
    weeks_ranges = []
    for i in range(weeks):
        week_range = [int(datetime.timestamp(initial_date)) * 1000,
                      int(datetime.timestamp(initial_date + timedelta(days=7))) * 1000]
        print(week_range)
        weeks_ranges.append(week_range)
        initial_date = initial_date + timedelta(days=7)
    print('\n')
    weeks_ranges.append(
        [weeks_ranges[-1][-1],
         int(datetime.timestamp(today)) * 1000]

    )
    print(weeks_ranges)

    return weeks_ranges