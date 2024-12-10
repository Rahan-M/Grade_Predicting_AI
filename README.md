# Grade_Predicting_AI
Beginners Task for GDSC inductions

We are using the student performance dataset suggested in the problem statement
We shall be predicting G3

We are using a decision tree regressor model
Order of feature importance as calculated in feature_importance.ipynb

       Feature  Importance
12          G2    0.836842
10    absences    0.029313
6        goout    0.029130
5     freetime    0.022505
13       sex_n    0.017483
8         Walc    0.014459
11          G1    0.012548
0          age    0.008446
4       famrel    0.008310
7         Dalc    0.006362
9       health    0.005463
3     failures    0.004473
1   traveltime    0.002363
2    studytime    0.002302

Let's use the top 5 of these to predict the student's final grade. i.e
i G2 - second period grade (numeric: from 0 to 20)
ii absences - number of school absences (numeric: from 0 to 93)
iii G1 - first period grade (numeric: from 0 to 20)
iv freetime - free time after school (numeric: from 1 - very low to 5 - very high)
v age - student's age (numeric: from 15 to 22)


From the 649 rows in the dataset