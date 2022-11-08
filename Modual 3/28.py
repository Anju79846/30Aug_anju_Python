#   Write a Python script to sort (ascending and descending) a dictionary by value.


import operator
Student_Data={"Anju":4 ,"Pooja":10 ,"Bhumi":8 ,"Mukul":24}
print("original dictionary",Student_Data)

Acending = dict(sorted(Student_Data.items(),key=operator.itemgetter(1)))
print("Accending order",Acending)

Decending=dict(sorted(Student_Data.items(),key=operator.itemgetter(1), reverse=True))
print("Decending order",Decending)