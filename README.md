# How to CSS
Build a Random Forest, Today!

Hello! This is a simple python command line thing to build/update the random forest model.

### 2 Commands
- update-d: updates the default random forest model with the prefined settings
- new: creates a new random forest model

#### 2.1 update-d


#### 2.2 new
- runs build_forest_proto(model_path)
  - model_path: .joblib file (e.g. model.joblib)
 - Prompts:
  - Partition Size (float): 0.25 - 0.75
  - Random Seed (partition) (int): 1 - max(int)
  - Number of trees: 1 - max(int) <- don't go max int because it'll be super slow and create a giant file (100,000 trees ~= 2.5gb)
  - Criteria (gini or entropy): 
    - gini: info gain good for continuous data
    - entropy: info gain good for attributes which occur in classes
  - Random Seed (classifier): 1 - max(int)



### 3 Default Random Forest Classifier Settings:
- Partition Settings:
  - Split Size: 0.5 (50%)
- Classifier Settings:
  - n_estimators: 100
  - oob_score: True
  
 
  
