import time
import numpy as np
import pandas as pd

def get_filters():
    """
    Prompt user's input.

    This function asks user to specify a `city`, `month`, and `day` through
    input in the command line, which has to be matched to the database.

    Parameters
    ----------
    city : input str
        Name of the city (case-insensitive).
        Possible values:
        
        * Chicago
        * New York City
        * Washington
    month : input str, optional
        Name of the month in Gregorian/Julian calendar (case-insensitive).
        Must not be specified when no filter should be applied on the dataset.
    day : input str, optional
        Name of the day of week (case-insensitive).
        Must not be specified when no filter should be applied on the dataset.

    Returns
    -------
    city : str
        Path or filename to the dataset.
    month : str or None
        Dataset will be filtered by `month`, or None if not specified.
    day : str or None
        Dataset will be filtered by `day`, or None if not specified.
    """
    # Dictionaries to easily exclude unwanted inputs by user.
    CITY_DATA = {'chicago': 'chicago.csv',
                 'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv'}
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
               'august', 'september', 'october', 'november', 'december']
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 
            'friday', 'saturday', 'sunday']
    
    while True:
        # Ask the user which city to be analyzed.
        city = input("Would you like to see data for Chicago, New York City or Washington? ").lower()
        if city in CITY_DATA:
            break
        else:
            print(f"Unknown city '{city}'!")

    while True:
        # Ask the user whether they want to apply time filter to the dataset.
        filter = input("Would you like to filter the data by month, day, both or not at all? Press Enter for no time filter! ").lower()
        match filter:
            case 'both':
                while True:
                    month = input("\tWhich month? Please write the month name completely: ").lower()
                    if month in MONTHS:
                        while True:
                            day = input("\tWhich day? Please write the day name completely: ").lower()
                            if day in DAYS:
                                return CITY_DATA[city], month.title(), day.title()
                                break
                            else:
                                print(f"\tUnknown day '{day}'!")
                        break
                    else:
                        print(f"\tUnknown month '{month}'!")
                break
            case 'month':
                while True:
                    month = input("\tWhich month? Please write the month name completely: ").lower()
                    if month in MONTHS:
                        return CITY_DATA[city], month.title(), None
                        break
                    else:
                        print(f"\tUnknown month '{month}'!")
                break
            case 'day':
                while True:
                    day = input("\tWhich day? Please write the day name completely: ").lower()
                    if day in DAYS:
                        return CITY_DATA[city], None, day.title()
                        break
                    else:
                        print(f"\tUnknown day '{day}'!")
                break
            case '':
                return CITY_DATA[city], None, None
                break
            case _:
                print(f"Unknown filter '{filter}'!")

def load_data(city, month, day):
    """
    Parse data to DataFrame.

    This function implements :func:`pandas.read_csv` to read csv file which is
    stored in `city`. It then calls :func:`pandas.to_datetime` to convert time-related
    columns to pandas datetime object. Lastly it applies specified filter(s), 
    if any, which is/are stored in `month` and/or `day`.

    Parameters
    ----------
    city : str
        Path to a filename where the dataset is stored.
    month : str, optional
        Name of the month to be used as filter or None if not specified.
    day : str, optional
        Name of the day of week to be used as filter or None if not specified.

    Returns
    -------
    df : DataFrame
        If the data for specified filter does not exist, it returns DataFrame
        with zero `size`.
    """
    try:
        # Load dataset into Python.
        df = pd.read_csv(city)

        # Converting time-related columns (object type) into datetime type.
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])

        # This way, further information extraction is much easier to conduct.
        df['Month'] = df['Start Time'].dt.month_name()
        df['Day of Week'] = df['Start Time'].dt.day_name()

        print("\nLoading data succeeded...")
        time.sleep(1)

        # Applying filter(s) to the dataset, if any filter applied.
        if month is not None or day is not None:
            print("Applying filter...")
            if month:
                df = df.loc[df['Month'] == month]
            
            if day:
                df = df.loc[df['Day of Week'] == day]
        time.sleep(1)

        return df
    except FileNotFoundError:
        print("Error: File not found!")

def info_prompt(city, month, day):
    """
    Display information.

    This function indicates the choices which have been made by user in the
    terminal.

    Parameters
    ----------
    city : str
        Path to a filename where the dataset is stored.
    month : str, optional
        Name of the month to be used as filter or None if not specified.
    day : str, optional
        Name of the day of week to be used as filter or None if not specified.
    Returns
    -------
    None
    """
    # Transforming city's filename back into city name.
    city = city.rstrip('_.csv').replace('_', ' ').title()

    # Prompting informations for user based on their choices.
    print("-" * 10, end=' ')
    print(f"City: {city}", end=' ')
    if month != None:
        print(f"|| Month: {month}", end=' ')
    if day != None:
        print(f"|| Day: {day}", end=' ')
    print("-" * 10)    

def data_preview(df):
    """
    Display preview of dataset.

    This function displays, on user confirmation, the preview of the dataset.

    Parameters
    ----------
    df : DataFrame
        (Filtered) Dataset to be previewed, if filter specified.
    preview : input str
        It takes every possible user's entries to enter preview mode or B or b
        to not entering preview mode.
    next_preview : input str
        It takes every possible user's entries to continue previewing or L or l
        to exiting preview mode.
    Returns
    -------
    None
    """
    # Asking user whether they want to see the raw data.
    try:
        preview = input("\nWould you like to enter the raw data preview mode? Press anything to enter or B/b to go back: ").lower()
        if preview != 'b':
            rows, columns = df.shape
            index = np.arange(0, rows, 5)
            start = 0
            finish = 1
            # Looping through the dataset for 5 factor of rows (rows % 5 == 0).
            while finish < len(index):
                    print("\n")
                    print(df.iloc[index[start] : index[finish]])
                    print(f"Page {finish} of {len(index)}")
                    next_preview = input("\nPress anything for more or L/l to leave the preview mode: ").lower()
                    if next_preview == 'l':
                        break
                    start += 1
                    finish += 1
                    time.sleep(0.5)
            # In case of 5 is not factor of rows (rows % 5 != 0), display the last rest row(s).
            else:
                print(df.iloc[index[start]:])
                print(f"Page {finish} of {len(index)}")
    except IndexError:
        print("No preview available!")

def time_stats(df, month, day):
    """
    Display statistics of times of travel.

    This function implements :func:`pandas.DataFrame.mode` to get the mode(s) of
    the elements in selected axis.

    Parameters
    ----------
    df : DataFrame
        Dataset on which statistic calculations will be performed.
    month : str, optional
        Name of the month to be used as filter or None if not specified.
    day : str, optional
        Name of the day of week to be used as filter or None if not specified.
    Returns
    -------
    None
    """
    print("\n#1)", end=' ')
    print("Calculating The Most Frequent Times of Travel ...\n")
    time.sleep(1.5)
    start_time = time.time()

    if df.size != 0:
        # Looking for the most common month.
        if month == None:
            popular_month = df['Month'].mode()[0]
            print(f"\tThe most frequent month to travel: {popular_month}")

        # Looking for the most common day of week.
        if day == None:
            popular_day = df['Day of Week'].mode()[0]
            print(f"\tThe most frequent day to travel: {popular_day}")

        # Looking for the most common start hour.
        popular_start_time = df['Start Time'].dt.hour.mode()[0]
        print(f"\tThe most frequent hour of day to travel: {popular_start_time} O'Clock")

    else:
        print("No data available")
    
    print(f"\n\t*This took {time.time() - start_time} seconds\n")

def station_stats(df):
    """
    Display statistics of bike stations.

    This function implements :func:`pandas.DataFrame.mode` to get the mode(s) of
    the elements in selected axis. It also implements :func:`pandas.DataFrame.groupby`
    prior the statistical calculation.

    Parameters
    ----------
    df : DataFrame
        Dataset on which statistic calculations will be performed.
    Returns
    -------
    None
    """
    print("#2)", end=' ')
    print("Calculating The Most Popular Stations and Trip ...\n")
    time.sleep(1.5)
    start_time = time.time()

    if df.size != 0:
        # Looking for the most commonly used start station.
        popular_start = df['Start Station'].mode()[0]
        print(f"\tThe most popular start station: {popular_start}")

        # Looking for the most commonly used end station.
        popular_end = df['End Station'].mode()[0]
        print(f"\tThe most popular end station: {popular_end}")

        # Looking for the most frequent combination of start station and end station trip.
        popular_station_pair = df.groupby(['Start Station'])['End Station'].value_counts().idxmax()
        print(f"\tThe most popular start and end stations pair: {str(popular_station_pair[0])} -> {str(popular_station_pair[1])}")

    else:
        print("No data available")
    
    print(f"\n\t*This took {time.time() - start_time} seconds\n")

def trip_duration_stats(df):
    """
    Display statistics of trip duration.

    This function implements :func:`pandas.DataFrame.mode` to get the mode(s) of
    the elements in selected axis. It also implements :func:`pandas.to_timedelta`
    prior the statistical calculation.

    Parameters
    ----------
    df : DataFrame
        Dataset on which statistic calculations will be performed.
    Returns
    -------
    None
    """
    print("#3)", end=' ')
    print("Calculating Trip Duration ...\n")
    time.sleep(1.5)
    start_time = time.time()

    if df.size != 0:
        # Looking for the total traveling done in day(s).
        total_duration = pd.to_timedelta(df['Trip Duration'].sum(), unit='s')
        print(f"\tThe total traveling done: {total_duration}")

        # Looking for the average travel time for each trip in day(s).
        average_duration = pd.to_timedelta(df['Trip Duration'].mean(), unit='s')
        print(f"\tThe average time spent for each trip: {average_duration}")

    else:
        print("No data available")
    
    print(f"\n\t*This took {time.time() - start_time} seconds\n")    

def user_stats(df):
    """
    Displays statistics of users.

    This function implements :func:`pandas.DataFrame.mode` to get the mode(s) of
    the elements in selected axis. It also implements :func:`pandas.DataFrame.min`,
    :func:`pandas.DataFrame.max`, :func:`pandas.DataFrame.value_counts`.

    Parameters
    ----------
    df : DataFrame
        Dataset on which statistic calculations will be performed.
    Returns
    -------
    None
    """
    print("#4)", end=' ')
    print("Calculating User Stats ...\n")
    time.sleep(1.5)
    start_time = time.time()

    if df.size != 0:
        try:
            # Counting the amounts of users for each membership category.
            user_types = df['User Type'].value_counts()
            print("\tUser type categories:")
            for user, count in user_types.items():
                print(f"\t\t{user}: {count}")

            # Counting the amounts of users for each gender category.
            user_genders = df['Gender'].value_counts()
            print("\tUser gender categories:")
            for user, count in user_genders.items():
                print(f"\t\t{user}: {count}")

            # Looking for the oldest user(s).
            oldest_user = df['Birth Year'].min()
            print(f"\tOldest user(s) was(were) born in {oldest_user}")

            # Looking for the youngest user(s).
            youngest_user = df['Birth Year'].max()
            print(f"\tYoungest user(s) was(were) born in {youngest_user}")

            # Looking for the most common birth of year among the users.
            common_yob = df['Birth Year'].mode()[0]
            print(f"\tThe most common year of birth: {common_yob}")
        except KeyError:
            pass
    else:
        print("No data available")
    
    print(f"\n\t*This took {time.time() - start_time} seconds\n")

def main():
    """
    Call functions.

    This function calls custom functions which are specified for Udacity Python
    Project.

    Parameters
    ----------
    restart : input str
        It takes every possible user's entries to restart the program or Q or q
        to indicate quit.
    Returns
    -------
    None
    -------
    None
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        info_prompt(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_preview(df)

        restart = input("\nPress anything to restart or Q/q to quit? ").lower()
        if restart == 'q':
            print("\nBye!")
            break

if __name__ == '__main__':
    print("\nHello! Let's explore some US bikeshare data!")
    main()