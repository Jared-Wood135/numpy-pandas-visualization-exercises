# =======================================================================================================
# Exercises Part I (10) START
# =======================================================================================================

import pandas as pd
# Use pandas to create a Series named fruits from the following list:
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", 
"watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", 
"gooseberry", "papaya"])
fruits_list = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", 
"watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", 
"gooseberry", "papaya"]

# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.
print('Length of fruits:\n',fruits.size)

# 2. Output only the index from fruits.
print('Index of fruits:\n',fruits.index)

# 3. Output only the values from fruits.
print('Values of fruits:\n',fruits.values)

# 4. Confirm the data type of the values in fruits.
print('Type of values in fruits:\n',fruits.dtype)

# 5. Output only the first five values from fruits. Output the last three values. 
#    Output two random values from fruits.
print(
  'First 5 values:\n',fruits.head(5),
  '\nLast 3 values:\n',fruits.tail(3),
  '\nRandom 2 values:\n',fruits.sample(2)
)

# 6. Run the .describe() on fruits to see what information it returns when called on a 
#    Series with string values.
fruits.describe()

# 7. Run the code necessary to produce only the unique string values from fruits.
fruits.unique()

# 8. Determine how many times each unique string value occurs in fruits.
fruits.unique().size

# 9. Determine the string value that occurs most frequently in fruits.
fruits.value_counts()

# 10. Determine the string value that occurs least frequently in fruits.
fruits.value_counts()[fruits.value_counts() == 1]

# =======================================================================================================
# Exercises Part I (10) END
# Exercises Part I (10) TO Exercises Part II (9)
# Exercises Part II (9) START
# =======================================================================================================

# Explore more attributes and methods while you continue to work with the fruits Series.

# 1. Capitalize all the string values in fruits.
fruits.str.capitalize()

# 2. Count the letter "a" in all the string values (use string vectorization).
sum(fruits.apply(lambda x: x.count('a')))

# 3. Output the number of vowels in each and every string value.
vowels = '[aeiouAEIOU]'
fruits.str.count(vowels)

# 4. Write the code to get the longest string value from fruits.
maxlen = max(fruits.str.len())
fruits[maxlen]

max(fruits_list)

# 5. Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() == 5]

lenof5 = ([str for str in fruits_list if len(str) == 5])
lenof5

# 6. Find the fruit(s) containing the letter "o" two or more times.
fruits.str.count('o')
fruits[fruits.str.count('o') >= 2]

# 7. Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]

hasberry = ([str for str in fruits_list if 'berry' in str])
hasberry

# 8. Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

hasapple = ([str for str in fruits_list if 'apple' in str])
hasapple

# 9. Which string value contains the most vowels?
fruits.str.count(vowels)
fruits[max(fruits.str.count(vowels))]

# =======================================================================================================
# Exercises Part II (9) END
# Exercises Part II (9) TO Exercises Part III (Set 1 - 6)
# Exercises Part III (Set 1 - 6) START
# =======================================================================================================

# Use pandas to create a Series named letters from the following string. The easiest way 
# to make this string into a Pandas series is to use list to convert each individual letter 
# into a single string on a basic Python list.
letters_list = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters = pd.Series(letters_list)

# 1. Which letter occurs the most frequently in the letters Series?
letters.value_counts(ascending=False)

# 2. Which letter occurs the Least frequently?
letters.value_counts(ascending=True)

# 3. How many vowels are in the Series?
letters.str.count(vowels).sum()

# 4. How many consonants are in the Series?
vowels2 = ['a', 'e', 'i', 'o', 'u']
letters[~letters.isin(vowels2)]

# 5. Create a Series that has all of the same letters but uppercased.
letters.str.capitalize()

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
import matplotlib.pyplot as plt
top6letters = letters.value_counts().head(6)
top6letters.plot.bar()
plt.xlabel('Letter')
plt.xticks(rotation=0)
plt.ylabel('Frequency')
plt.title('6 Most Commonly Occuring Letters')
plt.show()

# =======================================================================================================
# Exercises Part III (Set 1 - 6) END
# Exercises Part III (Set 1 - 6) TO Exercises Part III (Set 2 - 8)
# Exercises Part III (Set 2 - 8) START
# =======================================================================================================

# Use pandas to create a Series named numbers from the following list:
numbers_list = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', 
'$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', 
'$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', 
'$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
numbers = pd.Series(numbers_list)

# 1. What is the data type of the numbers Series?
numbers.dtype

# 2. How many elements are in the number Series?
numbers.describe()

# 3. Perform the necessary manipulations by accessing Series attributes and methods to 
#    convert the numbers Series to a numeric data type.
test = numbers.str.strip('$')
test2 = test.str.replace(',', '')
numbers_float = test2.astype(float)
numbers_float

# 4. Run the code to discover the maximum value from the Series.
numbers_float.max()

# 5. Run the code to discover the minimum value from the Series.
numbers_float.min()

# 6. What is the range of the values in the Series?
(numbers_float.max() - numbers_float.min())

# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(numbers_float,4).value_counts()

# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
import matplotlib.pyplot as plt
numbers_float.value_counts(bins=4).plot.barh(color='thistle', width=1, ec='black')
plt.title('Net Worth Bins')
plt.xlabel('Occurances')
plt.ylabel('US $')
plt.show()

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

'''
Revisit the exercises from https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a.

After you complete each set of Series exercises, use any extra time you have to pursue the 
challenge below. You can work on these in the same notebook or file as the Series exercises 
or create a new practice notebook you can work in a little every day to keep your python and 
pandas skills sharp by trying to solve problems in multiple ways. These are not a part of 
the Series exercises grade, so don't worry if it takes you days or weeks to meet the challenge.

Challenge yourself to be able to...
    - solve each using vanilla python.
    - solve each using list comprehensions.
    - solve each by using a pandas Series for the data structure instead of lists and 
      using vectorized operations instead of loops and list comprehensions.
'''

# =======================================================================================================
# More Practice END
# =======================================================================================================