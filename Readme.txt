To fulfill the project requirements, I have used the Django web framework to build the backend service for sentiment analysis.
I have provided some extra features in the project. Such as, I have simply designed a Web page where Users can enter any text in
order to analyze the sentiment. I have called the API to perform such operation in that web page.


I am providing step by step process to run this project locally. 

1. First, you have to install the dependencies. To do so, Run the following command: "pip install -r requirements.txt".
2. You might need to install or upgrade numpy. To install it use: "pip install numpy".
   To upgrade the version use: "pip install --upgrade numpy".  
3. Now, to run the project use the following command: "python manage.py runserver". 
4. On the local host "http://127.0.0.1:8000/" (In my project "Homepage") Page, it opens a designed web page where Users can enter any text in
   order to analyze the sentiment.
5. Click or Open "http://127.0.0.1:8000/api/v1/analyze" to find the "Sentiment Analysis API". The api/v1 is indicating
   the version 1 of this "Sentiment Analysis API". There might be need of building some other versions of this API.

