# =======================================================================================================
# Exercises Part I (11) START
# =======================================================================================================

# 1. Run python -m pip install pymysql from your terminal to install the mysql client 
#    (any folder is fine)


# 2. cd into your exercises folder for this module and run echo env.py >> .gitignore


# 3. Create a function named get_db_url. It should accept a username, hostname, password, 
#    and database name and return a url connection string formatted like in the example at 
#    the start of this lesson.


# 4. Use your function to obtain a connection to the employees database.


# 5. Once you have successfully run a query:
#   a. Intentionally make a typo in the database url. What kind of error message do you see?


#   b. Intentionally make an error in your SQL query. What does the error message look like?


# 6. Read the employees and titles tables into two separate DataFrames.


# 7. How many rows and columns do you have in each DataFrame? Is that what you expected?


# 8. Display the summary statistics for each DataFrame.


# 9. How many unique titles are in the titles DataFrame?


# 10. What is the oldest date in the to_date column?


# 11. What is the most recent date in the to_date column?


# =======================================================================================================
# Exercises Part I (11) END
# Exercises Part I (11) TO Exercises Part II (16)
# Exercises Part II (16) START
# =======================================================================================================

# 1. Copy the users and roles DataFrames from the examples above.


# 2. What is the result of using a right join on the DataFrames?


# 3. What is the result of using an outer join on the DataFrames?


# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?


# 5. Load the mpg dataset from PyDataset.


# 6. Output and read the documentation for the mpg dataset.


# 7. How many rows and columns are in the dataset?


# 8. Check out your column names and perform any cleanup you may want on them.


# 9. Display the summary statistics for the dataset.


# 10. How many different manufacturers are there?


# 11. How many different models are there?


# 12. Create a column named mileage_difference like you did in the DataFrames exercises; 
#     this column should contain the difference between highway and city mileage for each car.


# 13. Create a column named average_mileage like you did in the DataFrames exercises; 
#     this is the mean of the city and highway mileage.


# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values 
#     denoting whether the car has an automatic transmission.


# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon 
#     on average?


# 16. Do automatic or manual cars have better miles per gallon?


# =======================================================================================================
# Exercises Part II (16) END
# Exercises Part II (16) TO Exercises Part III (7)
# Exercises Part III (7) START
# =======================================================================================================

# 1. Use your get_db_url function to help you explore the data from the chipotle database.


# 2. What is the total price for each order?


# 3. What are the most popular 3 items?


# 4. Which item has produced the most revenue?


# 5. Join the employees and titles DataFrames together.


# 6. For each title, find the hire date of the employee that was hired most recently 
#    with that title.


# 7. Write the code necessary to create a cross tabulation of the number of titles by 
#    department. (Hint: this will involve a combination of SQL code to pull the necessary 
#    data and python/pandas code to perform the manipulations.)


# =======================================================================================================
# Exercises Part III (7) END
# Exercises Part III (7) TO Extra Pandas Exercises and Resources
# Extra Pandas Exercises and Resources START
# =======================================================================================================

'''
    - https://www.w3resource.com/python-exercises/pandas/index.php
    - https://towardsdatascience.com/20-pandas-functions-that-will-boost-your-data-analysis-process-f5dfdb2f9e05
    - https://github.com/guipsamora/pandas_exercises
    - https://github.com/ajcr/100-pandas-puzzles
'''

# =======================================================================================================
# Extra Pandas Exercises and Resources END
# Extra Pandas Exercises and Resources TO More Practice!
# More Practice! START
# =======================================================================================================

'''
For even more practice with pandas, you can do the exercises from the SQL module, but 
instead of using SQL to do the aggregation, sorting, joining, etc, use pandas. That is, 
read the data from all of the tables into pandas dataframes and manipulate the dataframes.
'''

# =======================================================================================================
# More Practice! END
# =======================================================================================================