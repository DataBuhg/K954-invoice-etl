import pandas as pd


def main():

    def program_price(program):
        if program in ['Puppy Preschool', 'Basic Obedience', 'Advanced Obedience']:
            return 135
        elif program in ['Day Training', 'Behavior Modification', 'Service Animal']:
            return 150
        elif program == '2 Dog Session':
            return 215
        else:
            return 0
        
    def csv_cleanup(csv_filepath):
        df = pd.read_csv(csv_filepath)
        df = df[['Invitee Name', 'Invitee Email', 'Text Reminder Number', 'Event Type Name', 'Start Date & Time', 'End Date & Time', 'Canceled']]
        df.loc[:,'Start Date & Time'] = pd.to_datetime(df['Start Date & Time'], format='mixed').dt.strftime('%m-%d-%Y')
        df.loc[:,'End Date & Time'] = pd.to_datetime(df['End Date & Time'], format='mixed').dt.strftime('%m-%d-%Y')
        df = df[df['Canceled']== False]
        df.insert(7, "Price", pd.Series([], dtype='float'))
        df.loc[:, 'Price'] = df['Event Type Name'].apply(program_price)
        print('Cleaning data...')
        print('Data cleanup complete')
        return df
    

        
    def download(df):
        active = True
        while active:
            print("Would you like to download this as a csv or an excel file? ")
            answer1 = input("Please type Csv for Csv\nPlease type Excel for Excel\n(Csv :: Excel):  ").lower()
            file_name = input("input file name for download: ")

            if answer1 == 'csv':
                filename = f'{file_name}.csv'
                df.to_csv(filename, index=False)
                print("Downloading...")
                print('Downloaded :-)')
                active = False
            elif answer1 == 'excel':
                filename = f'{file_name}.xlsx'
                df.to_excel(filename, index=False)
                print("Downloading...")
                print('Downloaded :-)')
                active = False
    try:
        print("When entering the file you want to transform/ clean dont forget to add the ending. Ex: something.csv")            
        file = input("Enter the name of the file you would like to transform: ")
        df = csv_cleanup(file)
        download(df)
    except KeyError as ke:
        print(f"You're trying to access something that is non-existent.")
        print(f"Error: {ke}")
    except TypeError as te:
        print("Incorrect data type.")
        print(f"Error: {te}")
    except IOError as ie:
        print("File not found")
        print(f"Error: {ie}")
    except Exception as e:
        print(f"Something went wrong :-(\nError: {e}")


if __name__ == "__main__":
    main()