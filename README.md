# Grade_Predicting_AI
Beginners Task for GDSC inductions

We are using the student performance dataset suggested in the problem statement
We shall be predicting G3

We are using a decision tree regressor model

Order of feature importance as calculated in feature_importance.ipynb
The order of importance kept varying to a large degree depending upon the random_state with which we split the dataset into training and 
testing set, so I used the sum of the importances of 5 different random states
         Feature  Importance
12            G2    4.138190
10      absences    0.200482
4         famrel    0.090337
0            age    0.059401
11            G1    0.059242
14      school_n    0.042391
21        Fjob_n    0.037051
27  activities_n    0.035550
7           Dalc    0.032036
19        Fedu_n    0.030840
18        Medu_n    0.028207
8           Walc    0.027873
6          goout    0.026650
20        Mjob_n    0.024284
22      reason_n    0.022088
3       failures    0.020814
23    guardian_n    0.017889
13         sex_n    0.016680
9         health    0.014823
5       freetime    0.014097
1     traveltime    0.011163
2      studytime    0.010229
25      famsup_n    0.007695
16     famsize_n    0.005819
15     address_n    0.005546
31    romantic_n    0.004853
24   schoolsup_n    0.004756
26        paid_n    0.003204
17     Pstatus_n    0.002616
28     nursery_n    0.002353
30    internet_n    0.002335
29      higher_n    0.000507


Using grid search we found the best values for the hyperparameters of the decisiontreeregressor
min_samples_split= 5, min_samples_leaf= 5, max_features= None, max_depth= 4, criterion= 'squared_error'

Let's use the top 5 of these to predict the student's final grade. i.e
i G2 - second period grade (numeric: from 0 to 20)
ii G1 - first period grade (numeric: from 0 to 20)
iii absences - number of school absences (numeric: from 0 to 93)
iv famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
v age - student's age (numeric: from 15 to 22)

Values of RMSE and r^2 (Coefficient of determination) 
RMSE : 1.1754037010163108 
 r^2 : 0.8568457689399083

 Cross Validation:
 rmse_scores:
[1.47087101 1.34311317 1.74755629 1.87816684 1.79955646]
Average RMSE = 1.6478527554973303