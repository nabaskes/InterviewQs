# Time for a response on a messaging application

# Below is a table schema for a P2P messaging application. The table contains send/receive message data for the application's users.

# Column Name 	Data Type 	Description
# date 	string 	date of the message sent/received, format is 'YYYY-mm-dd'
# timestamp 	integer 	timestamp of the message sent/received, epoch seconds
# sender_id 	integer 	id of the message sender
# receiver_id 	integer 	id of the message receiver

# Question: Using Python and the Pandas library, how would you find the fraction of messages that get a response within 5 minutes?
# For simplicity, let's limit data to March 1, 2018.

# Upgrade to premium to receive in-depth solutions to each problem.

import pandas as pd


def quick_response(df: pd.DataFrame) -> float:
    for row in df.iterrows():
        row['has_quick_response'] = 1 if len(df[df['sender_id'] == row['receiver_id']][df['timestamp'] - row['timestamp'] < 360][df['timestamp'] - row['timestamp'] > 0]) > 0 else 0
    return float(df['has_quick_response'].sum())/float(df)

# more efficient to sort and then only search the next five minutes?
