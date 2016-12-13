import requests as req
import ast
import json

#stati=""""{"stats": ["total_vectors",0],["attempt_number",0],["classify_data_ratio",0],["avg_accuracy",0],["avg_false_positive_ratio",0],["avg_spent_time",0],["avg_user_level",0],["total_results",0],["avg_false_negative_ratio",0]}"""
s = req.get('https://slot-ml.ptsecurity.com/api/v1/users/d81bf0a5e623df798a99e9059056f0f36726f72c/stats')

str_1 = s.json()
str_2 = str_1['stats']
str_3 = str_2[0]
str = dict(str_3)

