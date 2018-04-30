import numpy as np
import pandas as pd
import time
from datetime import date
from datetime import datetime
# package for .weekday()

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    countriesString = []
    while(True):
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                    'Would you like to see data for Chicago, New York, or Washington?\n')
        if city.lower() == "chicago" or city.lower() == "new york" or city.lower() == "washington":
            if city.lower() == "chicago":
                city = chicago
            elif city.lower() == "new york":
                city = new_york_city
            else:
                city = washington
            return city
            break
        else:
            countriesString.append(city)
            print("Invalid city")

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Time Period(month/day/none) for filtering bikeshare data.
    '''
    timeString = []
    while(True):
        time_period = input('\nWould you like to filter the data by \'month\', \'day\', or not at'
                            ' all? (Type "none" for no time filter.)\n')
        if time_period.lower() == "none" or time_period.lower() == "month" or time_period.lower() == "day":
            return time_period.lower()
            break
        else:
            timeString.append(time_period)
            print("Invalid time_period")

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) Month name(January, February, March, April, May, or June) for filtering bikeshare data.
    '''
    monthString = []
    while(True):
        month = input('\nWhich month?(Jan-Jun) Please type your response as an integer.(January=1, February=2, etc.)\n')
        monthList = ['1','2','3','4','5','6']
        if month in monthList:
            print(month + ' selected')
            return month
        else:
            monthString.append(month)
            print('Invalid month, please enter again')

def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (int) Day of week as an integer(Range from 1-7. Monday=1, Tuesday=2, etc.)
    '''
    dayString = []
    while(True):
        day = input('\nWhich day? Please type your response as an integer.(1-30)\n')
        dayList = np.arange(1,32)
        if int(day) in dayList:
            if int(month) == 1 or int(month) == 3 or int(month) == 5:
                if int(day) >= 1 and int(day) <= 31:
                    print('day ' + day + ' selected')
                    return day
            elif int(month) == 4 or int(month) == 6:
                if int(day) >= 1 and int(day) <= 30:
                    print('day ' + day + ' selected')
                    return day
            elif int(month) == 2:
                if int(day) >= 1 and int(day) <= 28:
                    print('day ' + day + ' selected')
                    return day
        else:
            dayString.append(day)
            print('Invalid day, please enter again')


def popular_month(city_file, time_period):
    '''Finds the most popular month for start time and returns the specified month.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (str) Most popular month for start time
    '''
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
    city_file['month'] = city_file['Start Time'].dt.month

    max_month = city_file['month'].value_counts().head(1).idxmax()
    def month_converter(month):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return months[month -1]
    print('The most popular month is: ' + month_converter(max_month))

def popular_day(city_file, time_period):
    '''Finds the most popular day of week (Monday, Tuesday, etc.) for start time and returns the specified day.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (str) Most popular day of week (Monday, Tuesday, etc.) for start time
    '''
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
    city_file['weekday'] = city_file['Start Time'].dt.weekday
    max_weekday = city_file['weekday'].value_counts().head(1).idxmax()
    def weekday_converter(day):
        weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fri', 'Saturday', 'Sunday']
        return weekday[day]
    print(weekday_converter(max_weekday) + ' is the Most popular day of week.')

def popular_hour(city_file, time_period):
    '''Finds the most popular hour of day for start time and returns the specified day.

    Args:1
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (str) Most popular hour of day for start time

    '''
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
    city_file['hour'] = city_file['Start Time'].dt.hour
    max_hour = city_file['hour'].value_counts().head(1).idxmax()
    print(str(max_hour) + ' o\' clock is the Most popular hour of week.')


def trip_duration(city_file, time_period):
    '''Finds the total trip duration and average trip duration.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (float) total trip duration and average trip duration
    '''
    sum_dur = city_file['Trip Duration'].sum()
    mean_dur = city_file['Trip Duration'].mean()
    print( 'The total trip duration is ' + str(sum_dur) + ' second(s).')
    print( 'The average trip duration is ' + str(mean_dur) + ' second(s).')

def popular_stations(city_file, time_period):
    '''Finds the most popular start station and most popular end station.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (str) most popular start station and most popular end station
    '''
    start_station = city_file['Start Station'].value_counts().head(1).idxmax()
    end_station = city_file['End Station'].value_counts().head(1).idxmax()
    print('The most popular start station is ' + start_station)
    print('The most popular end station is ' + end_station + '\n')

def popular_trip(city_file, time_period):
    '''Finds the most popular trip.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (str) most popular trip
    '''
    city_file['Trip'] = 'from ' + city_file['Start Station'] + ' to ' + city_file['End Station']
    popular_trip = city_file['Trip'].value_counts().head(1).idxmax()
    print('The most popular trip is ' + popular_trip)


def users(city_file, time_period):
    '''Finds the the counts of each user type.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (Series) counts of each user type
    '''
    users_info = city_file['User Type'].value_counts()
    print(users_info)


def gender(city_file, time_period):
    '''Finds the counts of gender.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (Series) counts of gender
    '''
    gender = city_file['Gender'].value_counts()
    print(gender)


def birth_years(city_file, time_period):
    '''Finds the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years.

    Args:
        city_file, the csv file for the city specified by the user
        time_period, time period specified by the user
    Returns:
        (str) the earliest (i.e. oldest user), most recent (i.e. youngest user),
        and most popular birth years.
    '''
    old = city_file['Birth Year'].min()
    young = city_file['Birth Year'].max()
    popular_birth = city_file['Birth Year'].value_counts().head(1).idxmax()
    print('The oldest user is born at ' + str(old))
    print('The youngest user is born at ' + str(young))
    print('The most popular birth years is ' + str(popular_birth))

def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    ansString = []
    i = 0
    k = 5
    while(True):
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        if display.lower() == "no":
            break
        elif display.lower() == "yes":
            print(city_file.iloc[i:k])
            i = i + 5
            k = k + 5
        else:
            ansString.append(display)
            print("Invalid Input")


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city_name = get_city()
    print('Importing ' + city_name + '...')
    city = pd.read_csv(city_name)
    print('Success!')

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    # Adding time filter to the data
    def time_convertor(city, time_period):
        '''Copy and returns the Series after applying time filter.

        Args:
            city- raw csv from cities.
            time_period- time period specified by the user.
        Returns:
            Series with time_period filtered.
        '''
        df = city.copy()
        df = df[df['Start Time'] >= str(time_period) ]
        return df

    print('Calculating the first statistic...')
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        popular_month(city, time_period)
        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    start_time = time.time()
    if time_period == 'none':
        popular_day(city, time_period)
    elif time_period == 'month':
        month = '2017-0'+str(get_month())+'-01'
        df = time_convertor(city, month)
        popular_day(df, month)
    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular hour of day for start time?
    if time_period == 'none':
        popular_hour(city, time_period)
    elif time_period == 'month':
        popular_hour(df, month)
    elif time_period == 'day':
        month = get_month()
        day = get_day(month)
        if int(day) <= 9:
            day_t = '2017-0'+str(month)+'-0'+str(day)
        else:
            day_t = '2017-0'+str(month)+'-'+str(day)
        df_d = time_convertor(city, day_t)
        popular_hour(df_d, day_t)
    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()


    # What is the total trip duration and average trip duration?
    if time_period == 'none':
        trip_duration(city, time_period)
    elif time_period == 'month':
        trip_duration(df, month)
    elif time_period == 'day':
        trip_duration(df_d, day_t)
    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    if time_period == 'none':
        popular_stations(city, time_period)
    elif time_period == 'month':
        popular_stations(df, month)
    elif time_period == 'day':
        popular_stations(df_d, day_t)
    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    if time_period == 'none':
        popular_trip(city, time_period)
    elif time_period == 'month':
        popular_trip(df, month)
    elif time_period == 'day':
        popular_trip(df_d, day_t)
    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    if time_period == 'none':
        users(city, time_period)
    elif time_period == 'month':
        users(df, month)
    elif time_period == 'day':
        users(df_d, day_t)
    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    if city_name != 'washington.csv':
        if time_period == 'none':
            gender(city, time_period)
        elif time_period == 'month':
            gender(df, month)
        elif time_period == 'day':
            gender(df_d, day_t)
        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years
    if city_name != 'washington.csv':
        if time_period == 'none':
            birth_years(city, time_period)
        elif time_period == 'month':
            birth_years(df, month)
        elif time_period == 'day':
            birth_years(df_d, day_t)
        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    if time_period == 'none':
        display_data(city)
    elif time_period == 'month':
        display_data(df)
    elif time_period == 'day':
        display_data(df_d)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
