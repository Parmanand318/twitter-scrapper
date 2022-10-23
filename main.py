import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import datetime as dt



# Creating list to append tweet data
# Setting variables to be used below
maxTweets = 10

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:dmmixra4').get_items()):
    if i > maxTweets:
        break
    tweets_list1.append(
        [tweet.date, tweet.id, tweet.content, tweet.user.username])  # declare the attributes to be returned

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
tweets_df1.head()

# Export dataframe into a CSV
tweets_df1.to_csv('user-tweets.csv', sep=',', index=False)


st.title("twitter scrapper")
today = dt.date.today()
tomorrow = today + dt.timedelta(days=1)
start_date = st.date_input("Start Date",today)
end_date = st.date_input("End Date",tomorrow)
if start_date < end_date:
    st.success("Start Date: '%s'\n\nEnd Date: '%s'" % (start_date , end_date))
else :
    st.error('Error: End Date must fall after Start Date.')

tweeter_trending = st.text_input("Enter Your text", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if (st.button('Submit')):
    result = tweeter_trending.title()
    st.success(result)
    

