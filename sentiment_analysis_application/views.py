from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SentimentAnalysisSerializer

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Load the sentiment analysis model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ["Negative", "Neutral", "Positive"]


@csrf_exempt
@api_view(["POST"])
def analyze(request):
    # Deserializing the request data using the SentimentAnalysisSerializer
    serializer = SentimentAnalysisSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Retrieving the text from the deserialized data
    text = serializer.validated_data["text"]

    # Preprocessing the text
    tweet_words = []
    for word in text.split(" "):
        if word.startswith("@") and len(word) > 1:
            word = "@user"
        elif word.startswith("http"):
            word = "http"
        tweet_words.append(word)
    processed_text = " ".join(tweet_words)

    # Performing sentiment analysis
    encoded_text = tokenizer(processed_text, return_tensors="pt")
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Determine the sentiment
    sentiment_index = scores.argmax()
    sentiment = labels[sentiment_index]

    # Create the response JSON
    response_data = {"sentiment": sentiment}

    # Return the response
    return Response(response_data)


def homepage(request):
    return render(request, "homepage.html")
