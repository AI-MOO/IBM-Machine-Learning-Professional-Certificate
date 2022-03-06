import pandas as pd, matplotlib.pyplot as plt, os, sys, seaborn as sns
os.getcwd()

# Set up IBM colors
from colorsetup import colors, palette
sns.set_palette(palette)
#sns.palplot(sns.color_palette())

sourcefiles = ('Telco_customer_churn_demographics.xlsx', 'Telco_customer_churn_location.xlsx',
             'Telco_customer_churn_population.xlsx', 'Telco_customer_churn_services.xlsx',
             'Telco_customer_churn_status.xlsx')
datafiles = ('fulldata.pkl', 'churndata.pkl')

keep_vars = ['Customer ID', 'Tenure in Months', 'Offer', 'Phone Service', 'Multiple Lines',
             'Internet Type', 'Avg Monthly GB Download', 'Online Security', 'Online Backup',
             'Device Protection Plan', 'Premium Tech Support', 'Unlimited Data', 'Contract',
             'Paperless Billing', 'Payment Method', 'Monthly Charge', 'Total Revenue',
             'Satisfaction Score', 'Churn Value', 'Churn Score', 'CLTV']

keep_new = ['id', 'months', 'offer', 'phone', 'multiple', 'internet_type', 'gb_mon',
            'security', 'backup', 'protection', 'support', 'unlimited', 'contract',
            'paperless', 'payment', 'monthly', 'total_revenue', 'satisfaction',
            'churn_value', 'churn_score', 'cltv']

keep_rename = dict(zip(keep_vars, keep_new))
labels = {keep_rename[i] : i for i in keep_rename}

num_args, user_args = len(sys.argv), sys.argv[1:]
#print('\nWorking directory: {}'.format(os.getcwd()))
#breakpoint()
#if len(user_args) > 1: raise SyntaxError('Too many arguments.')
source = 's' in user_args
if source:
    (demo, loc, pop, services, status) = (pd.read_excel(i) for i in sourcefiles)
    locpop = loc.merge(pop)
    fulldata = demo.merge(locpop).merge(services).merge(status)
    fulldata.to_pickle(datafiles[0])
    churndata = fulldata[keep_vars].rename(columns=keep_rename)
    churndata.to_pickle(datafiles[1])

else:
    try:        
        fulldata = pd.read_pickle(datafiles[0])
        churndata = pd.read_pickle(datafiles[1])
    except FileNotFoundError:
        print(f'\nPickle datafile not found \nRun with argument "s" to read source files')
        sys.exit(1)

#breakpoint()


#colors = []
#colornum = 60
#for i in [f'Blue {colornum}', f'Teal {colornum}', f'Magenta {colornum}', f'Purple {colornum}', f'Gray {colornum}']:
#    colors.append(f'#{coloribm[i]}')

#colors = [f'#{coloribm["Blue 40"]}', f'#{coloribm["Purple 40"]}']
# Set your custom color palette
#sns.set_palette(sns.color_palette(colors))
#sns.palplot(sns.color_palette())



# Columns in original data
#demo_cols = ['Customer ID', 'Count', 'Gender', 'Age', 'Under 30', 'Senior Citizen',
#             'Married', 'Dependents', 'Number of Dependents']
#
#pop_cols = ['ID', 'Zip Code', 'Population']
#
#services_cols = ['Customer ID', 'Count', 'Quarter', 'Referred a Friend',
#                 'Number of Referrals', 'Tenure in Months', 'Offer', 'Phone Service',
#                 'Avg Monthly Long Distance Charges', 'Multiple Lines',
#                 'Internet Service', 'Internet Type', 'Avg Monthly GB Download',
#                 'Online Security', 'Online Backup', 'Device Protection Plan',
#                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies',
#                 'Streaming Music', 'Unlimited Data', 'Contract', 'Paperless Billing',
#                 'Payment Method', 'Monthly Charge', 'Total Charges', 'Total Refunds',
#                 'Total Extra Data Charges', 'Total Long Distance Charges', 'Total Revenue']

#status_cols = ['Customer ID', 'Count', 'Quarter', 'Satisfaction Score', 'Customer Status',
#               'Churn Label', 'Churn Value', 'Churn Score', 'CLTV', 'Churn Category',
#               'Churn Reason']