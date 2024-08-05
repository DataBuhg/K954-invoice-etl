import pandas as pd

def clean_pii(filepath, num):
    df = pd.read_csv(filepath)

    ['Invitee Name','Invitee First Name','Invitee Last Name','Invitee Email','Invitee Time Zone','Invitee accepted marketing emails','Text Reminder Number']

    df['Invitee Name'] = ['Client {}'.format(i+1) for i in range(len(df))]
    df['Invitee First Name'] = ['Patient {}'.format(i+1) for i in range(len(df))]
    df['Invitee Last Name'] = ['Patient {}'.format(i+1) for i in range(len(df))]
    df['Invitee Email'] = 'anonymized@k954dogtraining.com'
    df['Text Reminder Number'] = 'xxx-xxx-xxxx'
    df['Response 1'] = 'anonymized'
    df['Response 2'] = 'anonymized'
    df['Guest Email(s)'] = 'anonymized'

    df.to_csv(f'cvdata_{num}.csv', index=False)

filepath = ['/Users/leonupshaw/Desktop/ev_data/evdata_apr2024.csv',
            '/Users/leonupshaw/Desktop/ev_data/evdata_feb2024.csv',
            '/Users/leonupshaw/Desktop/ev_data/evdata_jan2024.csv',
            '/Users/leonupshaw/Desktop/ev_data/evdata_jun2024.csv',
            '/Users/leonupshaw/Desktop/ev_data/evdata_mar2024.csv',
            '/Users/leonupshaw/Desktop/ev_data/evdata_may2024.csv']


num = 0
for file in filepath:
    clean_pii(file,num)
    num += 1
