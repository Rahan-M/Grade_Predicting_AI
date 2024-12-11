# Grade_Predicting_AI
Beginners Task for GDSC inductions
---

User Instructions:
To install the necessary libraries
pip install -r requirements.txt

to run the webapp type the command 
streamlit run app.py

I used the student performance dataset suggested in the problem statement.

## Problem Statement
Build a model to predict a student's final grade based on relevant features with minimal error

The model will predict the final grade of the student using previous grades, attendance, age and interestingly the quality of their family relationships
---

## Approach:

I have a decision tree regressor model.
Order of feature importance was calculated in feature_importance.ipynb
The order of importance kept varying to a large degree depending upon the random_state with which we split the dataset into training and 
testing sets, so I used the sum of the importances of 5 different random states to sort the features.

Feature - Importance   (Descending Order)  
G2 -   4.138190  
absences -  0.200482  
famrel -   0.090337  
age -   0.059401  
G1 -   0.059242  
school_n -   0.042391  
Fjob_n -   0.037051  
activities_n -   0.035550  
Dalc -   0.032036  
Fedu_n -   0.030840  
Medu_n -   0.028207  
Walc -   0.027873  
goout -   0.026650  
Mjob_n -   0.024284  
reason_n -   0.022088  
failures -   0.020814  
guardian_n -   0.017889  
sex_n -   0.016680  
health -   0.014823  
freetime -   0.014097  
traveltime -   0.011163  
studytime -   0.010229  
famsup_n -   0.007695  
famsize_n -   0.005819  
address_n -   0.005546  
romantic_n -   0.004853  
schoolsup_n -   0.004756  
paid_n -   0.003204  
Pstatus_n -   0.002616  
nursery_n -   0.002353  
internet_n -   0.002335  
higher_n -   0.000507  

* '_n' at the end of a feature means the orginal values for this feature were not integers or float, so it had to be converted to a number using label encoder*

I used the top 5 of these to predict the student's final grade. i.e  
i G2 - second period grade (numeric: from 0 to 20)  
ii G1 - first period grade (numeric: from 0 to 20)  
iii absences - number of school absences (numeric: from 0 to 93)   
iv famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)  
v age - student's age (numeric: from 15 to 22)  

---

The best values for the hyperparameters of the Decision Tree Regressor model was found using grid search. (Code available in project.ipynb)

The values were as follows:
min_samples_split= 5, min_samples_leaf= 5, max_features= None, max_depth= 4, criterion= 'squared_error'

---
The webapp was then created using streamlit,  (app.py)  
the model was saved in a pkl file and then loaded into app.py

---
## Results
The model was then trained on the above features and hyperparameters, and the here are its final performance metrics  

Values of RMSE and r^2 (Coefficient of determination) 
RMSE : 1.1754037010163108   
 r^2 : 0.8568457689399083  
  
 Cross Validation:  
 rmse_scores:  
[1.47087101 1.34311317 1.74755629 1.87816684 1.79955646]
Average RMSE = 1.6478527554973303

---

## Challenges

1) The order of feature importance kept changing depening upon how the dataset was split into training and testing set. i.r for different values of random_state given in the argument of train_test_split the feature importance was different.(G2 and absences however remained in the top 2 always).
I solved this by sorting the features by the sum of their importances over 5 random splits, which gave me a constant order for the top 5 features, independent of the split.

2) I first tried to use RandomizedSearchCV to find the best parameters for my models. But it did not give a consistent answer again showing big variations depending upon the value for random_state given in the argument.
I solved this by switching to GridSearchCV which looked over the range in which RandomizedSearchCV was giving me the best arguments most frequently. While it require a considerable amount of computational power, after the computation was complete, I obtained the best hyperparameters for optimizing my model

3) I first used a classification model, but the accuracy was very low. On furthur research I found that a regressor model would be better suited to handle this task.

---

## ScreenShots
Final Metrics:
![image](/ScreenShots/Final_Metrics.png)

Feature Importances Calculation

![image](/ScreenShots/Featuer_Importances_Code.png)
![image](/ScreenShots/Feature_Importance.png)