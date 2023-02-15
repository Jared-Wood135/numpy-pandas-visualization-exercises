# =======================================================================================================
# Exercises Part I (10) START
# =======================================================================================================

# Use pandas to create a Series named fruits from the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", 
"watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", 
"gooseberry", "papaya"]

# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.


# 2. Output only the index from fruits.


# 3. Output only the values from fruits.


# 4. Confirm the data type of the values in fruits.


# 5. Output only the first five values from fruits. Output the last three values. 
#    Output two random values from fruits.


# 6. Run the .describe() on fruits to see what information it returns when called on a 
#    Series with string values.


# 7. Run the code necessary to produce only the unique string values from fruits.


# 8. Determine how many times each unique string value occurs in fruits.


# 9. Determine the string value that occurs most frequently in fruits.


# 10. Determine the string value that occurs least frequently in fruits.


# =======================================================================================================
# Exercises Part I (10) END
# Exercises Part I (10) TO Exercises Part II (9)
# Exercises Part II (9) START
# =======================================================================================================

# Explore more attributes and methods while you continue to work with the fruits Series.

# 1. Capitalize all the string values in fruits.


# 2. Count the letter "a" in all the string values (use string vectorization).


# 3. Output the number of vowels in each and every string value.


# 4. Write the code to get the longest string value from fruits.


# 5. Write the code to get the string values with 5 or more letters in the name.


# 6. Find the fruit(s) containing the letter "o" two or more times.


# 7. Write the code to get only the string values containing the substring "berry".


# 8. Write the code to get only the string values containing the substring "apple".


# 9. Which string value contains the most vowels?


# =======================================================================================================
# Exercises Part II (9) END
# Exercises Part II (9) TO Exercises Part III (Set 1 - 6)
# Exercises Part III (Set 1 - 6) START
# =======================================================================================================

# Use pandas to create a Series named letters from the following string. The easiest way 
# to make this string into a Pandas series is to use list to convert each individual letter 
# into a single string on a basic Python list.
'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

# 1. Which letter occurs the most frequently in the letters Series?


# 2. Which letter occurs the Least frequently?


# 3. How many vowels are in the Series?


# 4. How many consonants are in the Series?


# 5. Create a Series that has all of the same letters but uppercased.


# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.


# =======================================================================================================
# Exercises Part III (Set 1 - 6) END
# Exercises Part III (Set 1 - 6) TO Exercises Part III (Set 2 - 8)
# Exercises Part III (Set 2 - 8) START
# =======================================================================================================

# Use pandas to create a Series named numbers from the following list:
['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', 
'$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', 
'$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', 
'$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

# 1. What is the data type of the numbers Series?


# 2. How many elements are in the number Series?


# 3. Perform the necessary manipulations by accessing Series attributes and methods to 
#    convert the numbers Series to a numeric data type.


# 4. Run the code to discover the maximum value from the Series.


# 5. Run the code to discover the minimum value from the Series.


# 6. What is the range of the values in the Series?


# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.


# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.


# ======================================================================================================
# Exercises Part III (Set 2 - 8) END
# Exercises Part III (Set 2 - 8) TO Exercises Part III (Set 3 - 6)
# Exercises Part III (Set 3 - 6) START
# =======================================================================================================

# Use pandas to create a Series named exam_scores from the following list:
[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

# 1. How many elements are in the exam_scores Series?


# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores 
#    for the exam_scores Series.


# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.


# 4. Write the code necessary to implement a curve for your exam_grades Series and save this 
#    as curved_grades. Add the necessary points to the highest grade to make it 100, and add 
#    the same number of points to every other score in the Series as well.


# 5. Use a method to convert each of the numeric values in the curved_grades Series into a 
#    categorical value of letter grades. For example, 86 should be a 'B' and 95 should be 
#    an 'A'. Save this as a Series named letter_grades.


# 6. Plot your new categorical letter_grades Series in a meaninful way and include a title 
#    and axis labels.


# =======================================================================================================
# Exercises Part III (Set 3 - 6) END
# Exercises Part III (Set 3 - 6) TO More Practice
# More Practice START
# =======================================================================================================

# Revisit the exercises from https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a.

# After you complete each set of Series exercises, use any extra time you have to pursue the 
# challenge below. You can work on these in the same notebook or file as the Series exercises 
# or create a new practice notebook you can work in a little every day to keep your python and 
# pandas skills sharp by trying to solve problems in multiple ways. These are not a part of 
# the Series exercises grade, so don't worry if it takes you days or weeks to meet the challenge.

# Challenge yourself to be able to...
#       - solve each using vanilla python.


#       - solve each using list comprehensions.


#       - solve each by using a pandas Series for the data structure instead of lists and 
#         using vectorized operations instead of loops and list comprehensions.


# =======================================================================================================
# More Practice END
# =======================================================================================================