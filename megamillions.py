import sys
from csv import DictReader


'''
from csv import DictReader
# open file in read mode
with open('students.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    dict_reader = DictReader(read_obj)
    # get a list of dictionaries from dct_reader
    list_of_dict = list(dict_reader)
    # print list of dict i.e. rows
    print(list_of_dict)
'''

filename = '/mnt/c/Users/a0323/Downloads/Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv'
'''
with open(filename, newline='') as f:
    dict_reader = DictReader(f)
    list_of_dict = list(dict_reader)
    print(list_of_dict[1910])
    print(len(list_of_dict))
   '''
lotteryNumbers = [
 
        {
                "numbers": [1,2,3,4,5]             #  <- index 0
                "mega": [30]
        },
        {
                "numbers": [1,2,3,4,5]                 #  <- index 1
                "mega": 30
                "average":
                "median":
        }
 ] 
lotteryNumbers[1]["numbers"] = row[0].split(" ")
   
   
    '''
    try:d
        for row in reader:
            print(row)
    except Exception as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    '''