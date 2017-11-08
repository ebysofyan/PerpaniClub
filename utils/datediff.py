from datetime import date

DAY_IN_YEAR = 365


def get_age_category(date_comparator):
    today = date.today()
    delta = today - date_comparator
    day_delta = delta.days
    year = day_delta / DAY_IN_YEAR

    if year < 12:
        return 'Anak'
    elif year >= 12 and year < 18:
        return 'Remaja'
    elif year >= 18:
        return 'Dewasa'
