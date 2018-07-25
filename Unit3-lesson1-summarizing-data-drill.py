# Unit3-lesson1-summarizing-data-drill

import pandas as pd

#create empty data frame
df = pd.DataFrame()

#populate it with data
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Cousin Oliver']
df['age'] = [14, 12, 11, 10, 8, 6, 8]
df['age_cindy_bday'] = [14, 12, 11, 10, 8, 7, 8]
df['name_replace_with_jessica'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Jessica']
df['age_cindy_bday_with_jessica'] = [14, 12, 11, 10, 8, 7, 1]

#1: mean, median, mode of kids at the age they started the show?
print(df.age.mean())
print(df.age.median())
print(df.age.mode())

#1: variance, standard deviation, standard error
print(df.age.var())
print(df.age.std())
print(df.age.sem())


#2: choose one estimate of central tendency: mean - all of the numbers are grouped fairly close to each other
# no extreme high or low values

#2: choose one estimate of variance: variance between values since no extreme high or low values in list

#3: cindy had a birthday. updated estimates:
# changed: mean age increased, variance decreased, std decreased, standard error reduced
# didn't change: median age, mode
# mean, median, mode of kids at the age they started the show?
print(df.age_cindy_bday.mean())
print(df.age_cindy_bday.median())
print(df.age_cindy_bday.mode())

# variance, standard deviation, standard error
print(df.age_cindy_bday.var())
print(df.age_cindy_bday.std())
print(df.age_cindy_bday.sem())

# 4 replace with Jessica: replace central tendency estimate with median
# since extreme value of 1 for Jessica replaced Cousin Oliver at 8
# variance is high - tells you high spread out from the mean - but why is it 18??
# mean, median, mode of kids at the age they started the show with Jessica
print(df.age_cindy_bday_with_jessica.mean())
print(df.age_cindy_bday_with_jessica.median())
print(df.age_cindy_bday_with_jessica.mode())

# variance, standard deviation, standard error
print(df.age_cindy_bday_with_jessica.var())
print(df.age_cindy_bday_with_jessica.std())
print(df.age_cindy_bday_with_jessica.sem())

# 5: drop the outlier of .05, and average the rest
# to get a good estimate of readers of these mags who are fans of the Brady Bunch
print(((.20 + .23 + .17) / 3))
