# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 00:56:55 2017

@author: Akshay
"""

import os
import pandas as pd
import missingno as msno
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import linear_kernel
import pymysql
import itertools
from collections import Counter


os.chdir("C:\\Users\\Akshay\\Desktop\\Designation wise mapping")
os.getcwd()
df = pd.read_csv("user_skills_raw.csv")
df1 = df.dropna()

z = list(df1["mapped_skills"].unique())
b = list(df1["mapped_skills"].unique()).copy()

z.append("id")
feature_list = z

ids = list(df1["candidate_id"].unique())

columnz = ["candidate_id","mapped_skills"]
df3 = df1[columnz].copy()
df3["val"] = 1

df4 = df3.pivot(index='candidate_id', columns='mapped_skills', values='val').reset_index()
df4.fillna(0, inplace=True)

df5 = df4.set_index("candidate_id")

#Initialize dataframe as placeholder
data=df5.values.T
ibcf=pd.DataFrame(linear_kernel(data),index=df5.columns,columns=df5.columns)

#len(ibcf.columns)

#Neighbours based on descending order of cosine similarity
neighbours=pd.DataFrame({"skills":list(df5.columns)})
neighbours["associated_skills"]=neighbours["skills"].apply(lambda x: sorted(dict(ibcf.loc[x]).items(),key=lambda x:x[1],reverse=True)[0:5])

type(dict(ibcf.loc['2g']).items())

data=df5.values.T

a=linear_kernel(data)

dbconnect=pymysql.connect(host="54.254.219.225",user="shivankhome",passwd="password",database="consumer",charset="utf8mb4")


skill_data=pd.read_sql("select A.user_id,B.skill_name from user_skill A, master_skill B where A.skill_id=B.skill_id and user_id=3",con=dbconnect)


extracted_data=neighbours[neighbours["skills"].isin(list(map(lambda x: x.lower(),skill_data["skill_name"])))]
extracted_list=extracted_data["associated_skills"].tolist()
extracted_list=list(itertools.chain.from_iterable(extracted_list))
unique_list=list(set(list(map(lambda x: x[0],extracted_list))))



xe=neighbours["associated_skills"].apply(lambda x: list(map(lambda y:y[0],x))).tolist()
xe=list(itertools.chain.from_iterable(xe))
xe=dict(Counter(xe))

s=pd.DataFrame(xe,index=["counts"]).T
s.to_csv("count_data.csv")
p=pd.read_sql("select A.user_id,A.skill_id,B.skill_name from user_skill A,master_skill B  where A.skill_id=B.skill_id and user_id  in(select user_id from user_skill where skill_id=18077)",con=dbconnect)



