import pandas as pd

# value became row, key became column
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)
print(grades.T)

print(grades['Eva'])
print(grades.Sam)

# using loc and iloc method
print(grades.loc['Test2'])
print(grades.iloc[1])

# for consecutive rows
print(grades.loc['Test1':'Test3'])
print(grades.iloc[0:3])

# for non-consecutive rows
print(grades.loc[['Test1', 'Test3']])
print(grades.iloc[[0, 2]])

# view only Eva's and Katies's grades for Test1 and Test2
print(grades.loc[:'Test2', ['Eva', 'Katie']])
# test 1 is first one so dont need before:

# view only Sam's and Bob's grades for Test1 and Test3
print(grades.loc[['Test1', 'Test3'], 'Sam':'Bob'])

grades_A = grades[grades >= 90]
print(grades_A)

# create a dataframe for everyone with B grade
grade_B = [(grades >= 80) & (grades < 90)]
print(grade_B)

# create a dataframe for everyone with A or B garde
grades_A_or_B = [(grades >= 90) | (grades >= 80)]
print(grades_A_or_B)

pd.set_option('precision', 2)

print(grades.describe())
print(grades.T.describe())

print(grades.sort_index(ascending=False))
print(grades.sort_index(axis=1))
print(grades.sort_index(axis=1, ascending=False))

print(grades.sort_values(by='Test1', axis=1, ascending=False))
print(grades.T.sort_values(by='Test1', ascending=False))

print(grades.loc['Test1'].sort_values(ascending=False))
