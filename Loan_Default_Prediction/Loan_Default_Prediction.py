#Loan Default Prediction

import dltk_ai
from dltk_ai.dataset_types import Dataset

#DLTK SDK requires Python 3.5 + . Go to https://dev.dltk.ai/ and create an app. On creation of an app, you will get an API Key.
c = dltk_ai.DltkAiClient('API Key')

#It stores Train and Test Files remotely. File upload API will return file storage locations from Cloud Storage in response.
train_file_store_response = c.store("path/to/train/file",Dataset.TRAIN_DATA)
train_data = train_file_store_response["fileUrl"]
 
#train_data file url
#'/spotflock-studio-prod/xxxxx@xxxxxxxx.com/1551936734455-loan_train.csv'
#Upload Test File
test_file_store_response = c.store("path/to/test/file", Dataset.TEST_DATA)
test_data = test_file_store_response["fileUrl"]

#test_data file url
#'/spotflock-studio-prod/xxxxx@xxxxxxx.com/1551936725437-loan_test.csv'

#build model using NaiveBayesMultinomial algorithm.
train_response_NBM = c.train("classification", "NaiveBayesMultinomial", train_data, "Loan_Status", 
["CurrentLoanAmount","CreditScore","MonthlyDebt","Yr_Credit_His"],
"Loan Model - NaiveBayesMultinomial","weka", 80, True)

#The train/predict jobs take some amount of time to be completed and so their status can be checked with this API.
train_job_status_response_NBM = c.job_status(train_response_NBM["data"]["jobId"])

#Once the job status is completed, the job output can be retrieved from this API.
train_job_output_response_NBM = c.job_output(train_response_NBM["data"]["jobId"])

#After Train job is finished, you can get the model url.
model = train_job_output_response_NBM["output"]["modelUrl"]

#Printing model
#'/spotflock-studio-prod/22/1552024436737-Loan_Data_Model_6647825745227784853.mdl'

#The below code is to predict on test data by passing the model url that was obtained from previous response.
predict_response = c.predict("classification", test_data, model,"weka")

#The train/predict jobs take some amount of time to be completed and so their status can be checked with this API.
predict_job_status_response = c.job_status(predict_response["data"]["jobId"])

#Once the job status is completed, the job output can be retrieved from this API.
predict_job_output_response = c.job_output(predict_response["data"]["jobId"])

#Once the Predict job is completed, get the prediction file url.
pred_file = predict_job_output_response['output']['predFileUrl']

#You can download the predicted file as csv by using below code.
prediction_response = c.download(pred_file)
import io
import pandas as pd
df = pd.read_csv(io.StringIO(prediction_response.text))
df.to_csv('pred_file.csv')

