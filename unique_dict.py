# Write a python program to convert a list of dictionaries which may contain duplicate dictonaries into a list 
# containing unique dictionaries.

#   Example - Input
#   dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, 
#              {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

#   output=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, 
#           {'name': 'inform', 'confidence': 0.9842240810394287}]



dict_list = [{'name': 'affirm', 'confidence': 0.9448149204254}, 
             {'name': 'affirm', 'confidence': 0.944814920425415}, 
             {'name': 'inform', 'confidence': 0.9842240810394287}, 
             {'name': 'inform', 'confidence': 0.9842240810394287}]

op = list({temp['confidence']:temp for temp in dict_list}.values())

print(op)