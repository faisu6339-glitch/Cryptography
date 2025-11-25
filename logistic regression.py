from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score

product_dic = {
    'product_name':['acer 1','lenovo 1','acer 2.0','dell 1','dell 2', 'dell 3','dell 4', 'hp 1','hp 2', 'hp 3','hp 4'],
    'feedback_rate':[3,3.5,4.5,5,3.5,2.5,3.0,2.5,4.0,4.5,3.8],
    'state':[0,0,1,1,1,0,0,0,0,1,1]
    }

product = pd.DataFrame(product_dic)
X = product[['feedback_rate']]
y = product['state']

X_train,x_test,y_train,y_test = train_test_split(X, y, test_size=0.3,random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
#pred=model.predict([3.6])
#print('Prediction :',pred[0])