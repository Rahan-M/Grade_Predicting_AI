# Grade_Predicting_AI
Beginners Task for GDSC inductions

We are using the student performance dataset suggested in the problem statement
We shall be predicting G3

Order of feature importance as calculated in feature_importance.ipynb

       Feature  Importance
12          G2    0.317957
10    absences    0.093695
11          G1    0.085076
5     freetime    0.080451
0          age    0.060107
2    studytime    0.058146
9       health    0.055575
4       famrel    0.051255
8         Walc    0.048176
6        goout    0.044748
1   traveltime    0.031638
13       sex_n    0.028319
3     failures    0.022597
7         Dalc    0.022262

Let's use the top 5 of these to predict the student's final grade. i.e
i G2 - second period grade (numeric: from 0 to 20)
ii absences - number of school absences (numeric: from 0 to 93)
iii G1 - first period grade (numeric: from 0 to 20)
iv freetime - free time after school (numeric: from 1 - very low to 5 - very high)
v age - student's age (numeric: from 15 to 22)


From the 649 rows in the dataset