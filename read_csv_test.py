import csv
import unittest
import json

# file = r"C:\Users\Myo Thiha Kyaw\Downloads\business-operations-survey-2018-business-finance-csv.csv"

class Test(unittest.TestCase):

    def test_read_csv_file(self,file_name):
        file = r"C:\Users\Myo Thiha Kyaw\Downloads\{}.csv".format(file_name)

        csv_file = []
        with open(file) as csvDataFile:
           csv_data = csv.reader(csvDataFile)
           for row in csv_data:
            #    print(row)
               csv_file.append(row)
        return csv_file
if __name__ == "__main__":
    test = Test()
    csv_datas = test.test_read_csv_file(file_name="export")
    json_data  = json.dumps(csv_datas,sort_keys=True,indent=4)
    python_data = json.loads(json_data)
    # print(python_data)
    # print(json_data)
    # print(python_data)
    
    dic_data1 =[i for i in csv_datas[0]]
    lis1 = [i for i in csv_datas[1]]
    list2= [i for i in csv_datas[2]]
    list3= [i for i in csv_datas[3]]
    list4= [i for i in csv_datas[4]]
    data1 = dict(zip(dic_data1,lis1))
    data2 = dict(zip(dic_data1,list2))
    data3 = dict(zip(dic_data1,list3))
    data4 = dict(zip(dic_data1,list4))
    datas=[data1,data2,data3,data4]
    # print(data1)
    print(datas)
    json_datas = json.dumps(datas,indent=4)
    print(json_datas)
    # for i in dic_data1:
    #     dic_csv["Installation Order Id"]= i
    #     disc_csv["Created Date"] =
    