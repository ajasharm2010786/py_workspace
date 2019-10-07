
import csv
import pandas as pd
import json

# https://medium.com/@yzhong.cs/serialize-and-deserialize-complex-json-in-python-205ecc636caa

class DataClass(object):
    invest_adv_name = ""
    invest_adv_number = 0
    question = ""
    data = ""

    def __init__(self, var1, var2, var3, var4):
        self.invest_adv_name = var1
        self.invest_adv_number = var2
        self.question = var3
        self.data = var4

    def getAdvName(self):
        return self.invest_adv_name

    def getAdvNumber(self):
        return self.invest_adv_number

    def getQuestion(self):
        return self.question

    def getData(self):
        return self.data


class OutputClass(object):
    final_invst_number =0
    final_ques_obj_lst = []

    def __init__(self, var1, var2):
        self.final_invst_number = var1
        self.final_ques_obj_lst = var2

    def getFinalQesLst(self):
        return self.final_ques_obj_lst

    def getFinalInvstNum(self):
        return self.final_invst_number


class QuestionData(object):
    final_question = ""
    final_data = dict()

    def __init__(self, var1, var2):
        self.final_question = var1
        self.final_data = var2

    def getFinalData(self):
        return self.final_data

    def getFinalQes(self):
        return self.final_question


my_list = []

with open('F:\\nasscom_hack\\csv_json.csv', 'r') as file:
    array = file.readlines()
    counter = 0
    for row in array:
        if counter ==0:
            counter = counter + 1
            continue
        counter = counter + 1
        new_array = []
        new_array = row.split('|')
        # print(new_array[3])
        my_list.append(DataClass(new_array[0], new_array[1], new_array[2], new_array[3].strip()))
#
qes_rec_lst = []
ques_array = "item8a.3.1, item8a.3.2"
context_array = ques_array.split(',')
for rec in my_list:
    for ctxt_arr in context_array:
        if ctxt_arr == rec.getQuestion():
            qesObj = QuestionData(rec.getQuestion(), rec.getData())
            # print(qesObj.__dict__)
            qes_rec_lst.append(qesObj)

    outObj = OutputClass(rec.getAdvNumber(), qes_rec_lst)
    # lst = outObj.getFinalQesLst()
    # for l in lst:
    #     print(l.getFinalData())
    print(json.dumps(outObj.__dict__))



