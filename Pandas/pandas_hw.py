import pandas as pd

data = pd.read_csv('adult.data.csv')

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


#   1. Сколько мужчин и женщин (признак sex) представлено в этом наборе данных?
print(data['sex'].value_counts(normalize=False))


#   2. Каков средний возраст (признак age) женщин?
print('\nAverage age of women: ', round(data[data.sex != 'Male']['age'].mean(), 2))


#   3. Какова доля граждан Германии (признак native-country)?
print('\nProportion of German citizens: ', round(data['native-country'].value_counts(normalize=True)['Germany'], 4))


#   4-5. Каковы средние значения и среднеквадратичные отклонения возраста тех,
#   кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год?
print('\n', data.groupby(['salary'])['age'].describe(percentiles=[0.5]))


#   6. Правда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование?
#   (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
print('\nIs it true that people who make more than 50k have at least a college degree?\n',
      len(data[((data.education == 'Bachelors') | (data.education == 'Prof-school') |
               (data.education == 'Assoc-acdm') | (data.education == 'Assoc-voc') |
               (data.education == 'Masters') | (data.education == 'Doctorate')) &
               (data.salary == '>50K')]) == len(data[data.salary == '>50K']))


#   7. Выведите статистику возраста для каждой расы (признак race) и каждого пола. Используйте groupby и describe.
#   Найдите таким образом максимальный возраст мужчин расы Amer-Indian-Eskimo.
print('\n', data.groupby(['race', 'sex'])['age'].describe(percentiles=[0.5]))


#   8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)?
#   Женатыми считаем тех, у кого marital-status начинается с Married (Married-civ-spouse,
#   Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.
print('\n', data[data.salary == '>50K']['marital-status'].value_counts(normalize=True))


#   9. Какое максимальное число часов человек работает в неделю (признак hours-per-week)? Сколько людей работают
#   такое количество часов и каков среди них процент зарабатывающих много?
print('\nMaximum number of hours a person works per week:', data['hours-per-week'].max(),
      '\nHow many people work this number of hours:',
      data['hours-per-week'].value_counts(normalize=False)[data['hours-per-week'].max()],
      '\nWhat is the percentage of them earning a lot',
      data[data['hours-per-week'] == data['hours-per-week'].max()]['salary'].value_counts(normalize=True)['>50K'],
      )

#   10. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary)
#   для каждой страны (native-country).
print('\n', data.groupby(['native-country', 'salary'])['hours-per-week'].mean())
