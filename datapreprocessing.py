#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:49:47 2018

@author: shannon
"""
import pandas as pd
#data = pd.read_csv('/home/shannon/Pictures/Data analysis 5525/Project stuff/survey_results_public.csv')
import warnings
data= pd.read_csv('/home/shannon/Pictures/Data analysis 5525/Project stuff/survey_results_stackoverflow_only.csv')
data.describe
data.shape
data['StackOverflowDescribes'].replace(
    to_replace="I have a login for Stack Overflow, but haven\'t created a CV or Developer Story",
    value="2",
    inplace=True
)
data['StackOverflowDescribes'].replace(
    to_replace="I\'ve visited Stack Overflow, but haven\'t logged in/created an account",
    value='1',
    inplace=True
)
data['StackOverflowDescribes'].replace(
    to_replace='I have created a CV or Developer Story on Stack Overflow',
    value='3',
    inplace=True
)
data['StackOverflowDescribes'].replace(
    to_replace='I\'d never heard of Stack Overflow before today',
    value='0',
    inplace=True
)
data['StackOverflowDescribes'].replace(
    to_replace='I\'ve heard of Stack Overflow, but have never visited',
    value='0',
    inplace=True
)
data.StackOverflowDescribes.unique()
data.StackOverflowFoundAnswer.unique()
data['StackOverflowFoundAnswer'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)
data.StackOverflowCopiedCode.unique()
data['StackOverflowCopiedCode'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)


data.StackOverflowJobListing.unique()
data['StackOverflowJobListing'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)

data['StackOverflowJobListing'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)
data.StackOverflowJobListing.unique()
#StackOverflowCompanyPage
data['StackOverflowCompanyPage'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)
data.StackOverflowCompanyPage.unique()

#StackOverflowJobSearch
data['StackOverflowJobSearch'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)
data.StackOverflowJobSearch.unique()
#StackOverflowNewQuestion
data['StackOverflowNewQuestion'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)
data.StackOverflowNewQuestion.unique()
#StackOverflowAnswer
#StackOverflowMetaChat
data['StackOverflowAnswer'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)
data.StackOverflowMetaChat.unique()
data['StackOverflowMetaChat'].replace(
    to_replace='Haven\'t done at all',
    value='0',
    inplace=True
)
data.StackOverflowAnswer.unique()
data.to_csv('SOformat.csv', sep=',', encoding='utf-8')
data.to_csv('SOformat1.csv', sep=',')
data.to_csv('SOformattab.csv', sep='\t',  encoding='utf-8')

data.StackOverflowAdsDistracting.unique()
data.StackOverflowMakeMoney.unique()
