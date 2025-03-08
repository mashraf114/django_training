from django.shortcuts import render
from django.http import HttpResponse

def monthly_challenge(respnse,month):
  challenge_text = None
  if month == "january":
    challenge_text = "Eat no meat for the entire month!"
  elif month == "february":
    challenge_text = "Walk for at least 20 minutes every day!"
  elif month == "march":
    challenge_text = "Learn Django for at least 20 minutes every day!"
  else:
    return HttpResponse("This month is not supported!")
  return HttpResponse(challenge_text)