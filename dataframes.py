# =======================================================================================================
# INITIAL DATAFRAMES ORIENTATION START
# =======================================================================================================

# For several of the following exercises, you'll need to load several datasets using the 
# pydataset library. (If you get an error when trying to run the import below, use pip to 
# install the pydataset package.)
from pydataset import data

# When the instructions say to load a dataset, you can pass the name of the dataset as a 
# string to the data function to load the dataset. You can also view the documentation for 
# the data set by passing the show_doc keyword argument.

data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable

# All the datasets loaded from the pydataset library will be pandas dataframes

# =======================================================================================================
# INITIAL DATAFRAMES ORIENTATION END
# INITIAL DATAFRAMES ORIENTATION TO Exercises Set 1 (5)
# Exercises Set 1 (5) START
# =======================================================================================================

# 1. Copy the code from the lesson to create a dataframe full of student grades.
#   a. Create a column named passing_english that indicates whether each student has a 
#      passing grade in english.
# vvv INITIAL CODE vvv
import pandas as pd
import numpy as np
from pydataset import data
np.random.seed(123)
students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas', 'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))
df_dict = {'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades}
df = pd.DataFrame(df_dict)
# vvv CODING vvv
df['passing_english'] = df.english >= 70
df

#   b. Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values('passing_english')

#   c. Sort the english grades first by passing_english and then by student name. All the 
#      students that are failing english should be first, and within the students that are 
#      failing english they should be ordered alphabetically. The same should be true for 
#      the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing_english', 'name'])

#   d. Sort the english grades first by passing_english, and then by the actual english grade, 
#      similar to how we did in the last step.
df.sort_values(by=['passing_english', 'english'])

#   e. Calculate each students overall grade and add it as a column on the dataframe. The 
#      overall grade is the average of the math, english, and reading grades.
del df['avg_grade']
df['avg_grade'] = df[['math', 'english', 'reading']].sum(axis=1) / 3
df['avg_grade'] = df['avg_grade'].round(2)
df

# =======================================================================================================
# Exercises Set 1 (5) END
# Exercises Set 1 (5) TO Exercises Set 2 (11)
# Exercises Set 2 (11) START
# =======================================================================================================

# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following 
#    questions:
#   a. How many rows and columns are there?
#      234 Rows
#      11 Columns
mpg
mpg.shape

#   b. What are the data types of each column?
#      object, float, int, bool
mpg.info()

#   c. Summarize the dataframe with .info and .describe
mpg.info()
mpg.describe()

#   d. Rename the cty column to city.
mpg.rename(columns = {'cty' : 'city'})

#   e. Rename the hwy column to highway.
mpg.columns
mpg.rename(columns = {'hwy' : 'highway'})

#   f. Do any cars have better city mileage than highway mileage?
#      Hell naw brah
mpg
mpg['citympg > highway'] = mpg['cty'] > mpg['hwy']
mpg.sort_values(by = 'citympg > highway', ascending = True)
mpg.sort_values(by = 'citympg > highway', ascending = False)

#   g. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg['mileage_difference'] = mpg['hwy'] - mpg['cty']
mpg.sort_values(by = 'mileage_difference')

#   h. Which car (or cars) has the highest mileage difference?
mpg.sort_values(by = 'mileage_difference', ascending = False)

#   i. Which compact class car has the lowest highway mileage? The best?
mpg.sort_values(by = 'hwy')
mpg.sort_values(by = 'hwy', ascending = False)

#   j. Create a column named average_mileage that is the mean of the city and highway mileage.
mpg['average_mileage'] = mpg[['cty', 'hwy']].sum(axis=1) / 2
mpg['average_mileage'] = mpg['average_mileage'].round(2)
mpg

#   k. Which dodge car has the best average mileage? The worst?
mpg.sort_values(by = 'average_mileage', ascending = False)
mpg.sort_values(by = 'average_mileage')

# =======================================================================================================
# Exercises Set 2 (11) END
# Exercises Set 2 (11) TO Exercises Set 3 (6)
# Exercises Set 3 (6) START
# =======================================================================================================

# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer 
#    these questions:
#   a. How many rows and columns are there?
mammals = data('Mammals')
mammals

#   b. What are the data types?
#      Float & Bool
mammals.info()

#   c. Summarize the dataframe with .info and .describe
mammals.info()
mammals.describe()

#   d. What is the the weight of the fastest animal?
mammals.sort_values(by = 'speed', ascending = False).head(1)

#   e. What is the overal percentage of specials?
mammals.shape  # =====> 107 rows
mammals.sample(1)
percent_of_specials = len(mammals[mammals.specials == True]) / 107
percent_of_specials

#   f. How many animals are hoppers that are above the median speed? What percentage is this?
mammals.speed.median()
mammals[(mammals.speed > mammals.speed.median()) == True].shape # =====> 53 / 107
percent_above_median_speed = len(mammals[(mammals.speed > mammals.speed.median())] == True) / len(mammals)
percent_above_median_speed

# =======================================================================================================
# Exercises Set 3 (6) END
# Exercises Set 3 (6) TO Awesome Bonus
# Awesome Bonus START
# =======================================================================================================

'''
For much more practice with pandas, Go to https://github.com/guipsamora/pandas_exercises and 
clone the repo down to your laptop. To clone a repository: - Copy the SSH address of the 
repository - cd ~/codeup-data-science - Then type git clone git@github.com:guipsamora/pandas_exercises.git - 
Now do cd pandas_exercises on your terminal. - Type git remote remove origin, so you won't 
accidentally try to push your work to guipsamora's repo.

Congratulations! You have cloned guipsamora's pandas exercises to your computer. 
Now you need to make a new, blank, repository on GitHub.

    - Go to https://github.com/new to make a new repo. Name it pandas_exercises.
    - DO NOT check any check boxes. We need a blank, empty repo.
    - Finally, follow the directions to "push an existing repository from the command line" 
      so that you can push up your changes to your own account.
    - Now do your own work, add it, commit it, and push it!
'''

# =======================================================================================================
# Awesome Bonus END
# =======================================================================================================