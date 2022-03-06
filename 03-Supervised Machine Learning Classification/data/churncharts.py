"""
This script generates charts for the Course 1 Deck using the churndata files

"""

import pandas as pd, matplotlib.pyplot as plt, os, sys, seaborn as sns
os.getcwd()
# IBM colors
from colorsetup import coloribm, colors, palette
sns.set_palette(palette)
from datasetup import labels, churndata

# Start with subset of phone customers
df_phone = churndata[churndata.phone=='Yes']

# Look at churn value assigned by payment type
sns.barplot(y='churn_value', x='payment', data=df_phone, ci=None)
plt.ylabel('Churn Rate')
plt.xlabel('Payment Type')
plt.title('Churn Rate by Payment Type, Phone Customers')
plt.savefig('churn_pay_type.png')

sns.barplot(y='churn_value', x='contract', data=df_phone, ci=None)
plt.ylabel('Churn Rate')
plt.xlabel('Contract Type')
plt.title('Churn Rate by Contract Type, Phone Customers')
plt.savefig('churn_contract_type.png')

sns.barplot(y='churn_value', x=pd.cut(df_phone.months, bins=5), data=df_phone, ci=None)
plt.ylabel('Churn Rate')
plt.xlabel('Tenure Range in Months')
plt.title('Churn Rate by Tenure, Phone Customers')
plt.savefig('churn_tenure.png')

dfr = df_phone.rename(columns=labels)

#df_phone.info()
sns.jointplot(x=dfr[labels['months']], y=dfr[labels['monthly']], kind='hex')
#plt.xlabel('Tenure in Months')
#plt.ylabel('Average Monthly Payment')
#plt.title('Hexbin Plot of Tenure and Payment')
plt.savefig('hexbin_tenure_pmt.png')

df_phone_pairplot = df_phone[['months', 'gb_mon', 'total_revenue', 'cltv', 'churn_value']].rename(columns=labels)
sns.pairplot(df_phone_pairplot, vars=list(df_phone_pairplot.columns[:4]), hue=labels['churn_value'])


#df_phone_pairplot = df_phone[['months', 'gb_mon', 'total_revenue', 'cltv', 'churn_value']]
#sns.pairplot(df_phone_pairplot.rename(columns=labels), vars=['months', 'gb_mon', 'total_revenue', 'cltv'], hue=labels['churn_value'])
plt.savefig('phone_pairplot.png')
df_phone.groupby('churn_value')['total_revenue'].hist()
df_phone.groupby('churn_value')['cltv'].hist()

#######
#breakpoint()