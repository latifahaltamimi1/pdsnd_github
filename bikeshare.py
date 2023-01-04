import time
import pandas as pd
import numpy as np
import calendar


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    while True:
        
      city = input('\nPlease Choose a City Name :- chicago, new york city , washington : '). lower ()
      if city not in CITY_DATA.keys ():
        print("Invalid City!/n Please Enter a Valid City")
        continue
      else:
        break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january', 'february','march','april','may','june']

    while True:
      month = input(" \nPlease choose a month? january, february, march, april, may, june or type 'all' if you do not have any preference: ")
      if month not in months:
        print("Sorry, invalid input Try again.")
        continue
      else:
        break
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
       
        

    while True:
        weekDays =['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
        day =input('\nPlease choose a day of the week or if you want to display all days type "all": '). lower() 
        if day not in weekDays:
           print('Invalid input')
        else:
            break   
    print('-'*40)
    return city,month,day

 

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
       # loads data file
    df=pd.read_csv(CITY_DATA[city])
       #convert start time to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
       
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

       # filter by month if applicable
    if month != 'all':
        #use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week
    if day != 'all':
        #create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nThe most common month is:")
    print(calendar.month_name[df['month'].value_counts().idxmax()])
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print ('The most common day is:',common_day)
                                  

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_time = df['hour'].mode()[0]
    print ('The most common start time is:',start_time)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    start = df['Start Station'].value_counts().idxmax()
    end = df['End Station'].value_counts().idxmax()
    
    # TO DO: display most commonly used start station
    
    print('The most common start station is {}.'.format(start))

    # TO DO: display most commonly used end station

    print('The most common end station is {}.'.format(end))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station is: ')
    print(df.groupby(['Start Station','End Station']).size().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Time = df['Trip Duration'].sum().round()
    print('Total travel time:',Total_Time)

    # TO DO: display mean travel time
    Mean_Time = df['Trip Duration'].mean().round()
    print('Mean travel time:', Mean_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user Types are:\n', user_types)
    # TO DO: Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth

     # earliest birth year:-
        print('The Most recent year: {}'.format(int(df['Birth Year'].max())))
      # the most reasnt birthyear:-
        print('The Earliest year: {}'.format(int(df['Birth Year'].min())))
      # the most common birth year:-
        print('The Most common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display(df):
    data = 0
    while True:
        choose = str(input("would you like to see more 5 row data? Please choose yes or no \n")).lower()
        if choose not in {'yes','no'}:
            choose = str(input("your input is wrong , Please Enter only yes or no \n")).lower()
        elif choose == 'yes':
            data += 5
            print(df.iloc[data : data + 5])
        elif choose == 'no':        
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display(df)
         
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you ;)')
            break


if __name__ == "__main__":
    main()