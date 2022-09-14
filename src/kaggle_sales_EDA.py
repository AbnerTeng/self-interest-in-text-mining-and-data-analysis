import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import requests
from statistics import mode
import warnings

class data_analyze():
    def load_data(self):
        self.fwd_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        self.data_path = "/datas/train.csv"
        self.full_path = self.fwd_path + self.data_path
        self.df = pd.read_csv(self.full_path)

        
        


    def deal_nan(self):
        self.df.rename(columns = {"City_Category": "City", "Stay_In_Current_City_Years": "Years_in_city"}, inplace = True)
        print(self.df.Age.unique)
        self.df['Age'] = self.df['Age'].map({'0-17': 'Child', '18-25': 'Teenage', '26-35': 'Adult', '36-45': 'Adult', '46-50': 'Adult', '51-55': 'Old', '55+': 'Old'})

        self.pc2 = self.df.groupby(['Age'])['Product_Category_2'].agg(pd.Series.mode)
        self.pc3 = self.df.groupby(['Age'])['Product_Category_3'].agg(pd.Series.mode)

        self.child2 = self.df.loc[self.df['Age'] == 'Child', 'Product_Category_2'].fillna(self.pc2['Child'])
        self.df.loc[self.df['Age'] == 'Child', 'Product_Category_2'] = self.child2
        self.child3 = self.df.loc[self.df['Age'] == 'Child', 'Product_Category_3'].fillna(self.pc3['Child'])
        self.df.loc[self.df['Age'] == 'Child', 'Product_Category_3'] = self.child3
        

        self.teenage2 = self.df.loc[self.df['Age'] == 'Teenage', 'Product_Category_2'].fillna(self.pc2['Teenage'])
        self.df.loc[self.df['Age'] == 'Teenage', 'Product_Category_2'] = self.teenage2
        self.teenage3 = self.df.loc[self.df['Age'] == 'Teenage', 'Product_Category_3'].fillna(self.pc3['Teenage'])
        self.df.loc[self.df['Age'] == 'Teenage', 'Product_Category_3'] = self.teenage3

        self.adult2 = self.df.loc[self.df['Age'] == 'Adult', 'Product_Category_2'].fillna(self.pc2['Adult'])
        self.df.loc[self.df['Age'] == 'Adult', 'Product_Category_2'] = self.adult2
        self.adult3 = self.df.loc[self.df['Age'] == 'Adult', 'Product_Category_3'].fillna(self.pc3['Adult'])
        self.df.loc[self.df['Age'] == 'Adult', 'Product_Category_3'] = self.adult3

        self.old2 = self.df.loc[self.df['Age'] == 'Old', 'Product_Category_2'].fillna(self.pc2['Old'])
        self.df.loc[self.df['Age'] == 'Old', 'Product_Category_2'] = self.old2
        self.old3 = self.df.loc[self.df['Age'] == 'Old', 'Product_Category_3'].fillna(self.pc3['Old'])
        self.df.loc[self.df['Age'] == 'Old', 'Product_Category_3'] = self.old3

        print(self.df['Product_Category_2'].isnull().value_counts())
        print(self.df['Product_Category_3'].isnull().value_counts())


    def convert_data(self):
        self.df['Gender'] = self.df['Gender'].map({'M': 1, 'F': 0})
        print(self.df.head())

    def save_file(self):
        self.df.to_csv('/Users/abnerteng/GitHub/self-interest-in-text-mining-and-data-analysis/datas/customer_data.csv', index = False)


    def data_visulaize(self):
        '''
        heatmap
        '''
        sns.heatmap(self.df.corr(), annot = True)
        plt.show()
        '''
        gender column
        '''
        sns.countplot(x = 'Gender', data = self.df)
        plt.show()
        '''
        City column
        '''
        sns.countplot(x = 'City', data = self.df)
        plt.show()
        '''
        Age column
        '''
        sns.countplot(x = 'Age', data = self.df)
        plt.show()
        '''
        purchase graph
        '''
        sns.displot(self.df['Purchase'])
        plt.show()
        '''
        Age & purchase
        '''
        sns.boxplot(x = 'Age', y = 'Purchase', data = self.df)
        plt.show()



if __name__ == "__main__":
    EDA = data_analyze()
    EDA.read_file()
    EDA.deal_nan()
    EDA.convert_data()
    EDA.save_file()
    EDA.data_visulaize()






