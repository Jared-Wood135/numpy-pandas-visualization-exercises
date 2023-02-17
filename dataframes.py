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


#   b. What are the data types of each column?


#   c. Summarize the dataframe with .info and .describe


#   d. Rename the cty column to city.


#   e. Rename the hwy column to highway.


#   f. Do any cars have better city mileage than highway mileage?


#   g. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.


#   h. Which car (or cars) has the highest mileage difference?


#   i. Which compact class car has the lowest highway mileage? The best?


#   j. Create a column named average_mileage that is the mean of the city and highway mileage.


#   k. Which dodge car has the best average mileage? The worst?


# =======================================================================================================
# Exercises Set 2 (11) END
# Exercises Set 2 (11) TO Exercises Set 3 (6)
# Exercises Set 3 (6) START
# =======================================================================================================

# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer 
#    these questions:
#   a. How many rows and columns are there?


#   b. What are the data types?


#   c. Summarize the dataframe with .info and .describe


#   d. What is the the weight of the fastest animal?


#   e. What is the overal percentage of specials?


#   f. How many animals are hoppers that are above the median speed? What percentage is this?


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