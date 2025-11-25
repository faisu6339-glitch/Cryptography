product_dic = {
    'product_name':['acer 1','lenovo 1','acer 2.0','dell 1','dell 2', 'dell 3','dell 4', 'hp 1','hp 2', 'hp 3','hp 4'],
    'feedback_rate':[3,3.5,4.5,5,3.5,2.5,3.0,2.5,4.0,4.5,3.8],
    'state':[0,0,1,1,1,0,0,0,0,1,1]
    }
import pandas as pd
product = pd.DataFrame(product_dic)
product
   product_name  feedback_rate  state
0        acer 1            3.0      0
1      lenovo 1            3.5      0
2      acer 2.0            4.5      1
3        dell 1            5.0      1
4        dell 2            3.5      1
5        dell 3            2.5      0
6        dell 4            3.0      0
7          hp 1            2.5      0
8          hp 2            4.0      0
9          hp 3            4.5      1
10         hp 4            3.8      1
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
X = df[['feedback_rate']]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    X = df[['feedback_rate']]
NameError: name 'df' is not defined
X = product[['feedback_rate']]
X
    feedback_rate
0             3.0
1             3.5
2             4.5
3             5.0
4             3.5
5             2.5
6             3.0
7             2.5
8             4.0
9             4.5
10            3.8
y = product['state']
y
0     0
1     0
2     1
3     1
4     1
5     0
6     0
7     0
8     0
9     1
10    1
Name: state, dtype: int64
product['feedback_rate']
0     3.0
1     3.5
2     4.5
3     5.0
4     3.5
5     2.5
6     3.0
7     2.5
8     4.0
9     4.5
10    3.8
Name: feedback_rate, dtype: float64

X_train,x_test,y_train,y_test = train_test_split(X, y, test_size=0.3,random_state=42)
X_train
   feedback_rate
2            4.5
1            3.5
8            4.0
4            3.5
7            2.5
3            5.0
6            3.0
x_test
    feedback_rate
5             2.5
0             3.0
9             4.5
10            3.8
>>> y_train
2    1
1    0
8    0
4    1
7    0
3    1
6    0
Name: state, dtype: int64
>>> y_test
5     0
0     0
9     1
10    1
Name: state, dtype: int64
>>> model = LogisticRegression()
>>> model.fit(X_train, y_train)
LogisticRegression()
>>> X_train
   feedback_rate
2            4.5
1            3.5
8            4.0
4            3.5
7            2.5
3            5.0
6            3.0
>>> y_train
2    1
1    0
8    0
4    1
7    0
3    1
6    0
Name: state, dtype: int64
>>> X_train
   feedback_rate
2            4.5
1            3.5
8            4.0
4            3.5
7            2.5
3            5.0
6            3.0
>>> model.predict(3.6)

Warning (from warnings module):
  File "C:\Users\Md Faisal Sheikh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sklearn\utils\validation.py", line 2749
    warnings.warn(
UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    model.predict(3.6)
  File "C:\Users\Md Faisal Sheikh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sklearn\linear_model\_base.py", line 375, in predict
    scores = self.decision_function(X)
  File "C:\Users\Md Faisal Sheikh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sklearn\linear_model\_base.py", line 352, in decision_function
    X = validate_data(self, X, accept_sparse="csr", reset=False)
  File "C:\Users\Md Faisal Sheikh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sklearn\utils\validation.py", line 2954, in validate_data
    out = check_array(X, input_name="X", **check_params)
  File "C:\Users\Md Faisal Sheikh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sklearn\utils\validation.py", line 1068, in check_array
    raise ValueError(
ValueError: Expected 2D array, got scalar array instead:
array=3.6.
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
feedback = 3.6
model.predict([[feedback]])

Warning (from warnings module):
  File "C:\Users\Md Faisal Sheikh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sklearn\utils\validation.py", line 2749
    warnings.warn(
UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
array([0])
s = model.predict([[feedback]])

Warning (from warnings module):
  File "C:\Users\Md Faisal Sheikh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sklearn\utils\validation.py", line 2749
    warnings.warn(
UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
s
array([0])
s[0]
np.int64(0)
