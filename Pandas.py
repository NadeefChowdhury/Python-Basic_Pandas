
#import pandas as pd
import pandas as pd


#read Salaries.csv as a dataframe called sal
sal = pd.read_csv('H:\Machine learning\Salaries.csv')

#check the head (first four rows)
sal.head(4)


#check info for details
sal.info()

#drop rows and columns containing null values
sal.dropna()

#check the average base pay
sal['BasePay'].mean()


#check the highest overtime pay
sal['OvertimePay'].max()


#check the job title of Christopher Chong
sal[sal['EmployeeName']=='Christopher Chong']['JobTitle']


#check the average total pay of all employees per year
sal.groupby('Year').mean()['TotalPay']

#check the number of unique job titles
sal['JobTitle'].nunique()



#check the top five most common job titles
sal['JobTitle'].value_counts().head(5)


#check how many job titles were represented by only one person in 2011
sum(sal[sal['Year']==2011]['JobTitle'].value_counts()==1)





