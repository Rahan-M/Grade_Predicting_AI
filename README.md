# Grade_Predicting_AI
Beginners Task for GDSC inductions

We are using the student performance dataset suggested in the problem statement
We shall be predicting G3

We are using a decision tree regressor model

Order of feature importance as calculated in feature_importance.ipynb
The order of importance kept varying to a large degree depending upon the random_state with which we split the dataset into training and 
       Feature  Importance
12          G2    4.160429
10    absences    0.200501
0          age    0.128889
5     freetime    0.082194
4       famrel    0.064010
11          G1    0.061622
7         Dalc    0.056877
13       sex_n    0.052912
6        goout    0.049504
8         Walc    0.042614
1   traveltime    0.031435
9       health    0.030941
3     failures    0.021323
2    studytime    0.016749


Using grid search we found the best values for the hyperparameters of the decisiontreeregressor
{'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': None, 'max_depth': 4, 'criterion': 'squared_error'}

Let's use the top 5 of these to predict the student's final grade. i.e
i G2 - second period grade (numeric: from 0 to 20)
ii absences - number of school absences (numeric: from 0 to 93)
iii G1 - first period grade (numeric: from 0 to 20)
iv freetime - free time after school (numeric: from 1 - very low to 5 - very high)
v age - student's age (numeric: from 15 to 22)

Values of RMSE and r^2 (Coefficient of determination)

RMSE : 1.31270982349436 
 r^2 : 0.8523551944849997