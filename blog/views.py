from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Tweet
from .forms import TweetForm
from datetime import datetime
from cloudinary.forms import cl_init_js_callbacks


# Create your views here.


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, show error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all the posts, limit = 20
    tweet = Tweet.objects.all().order_by('id').reverse().all()[:20]

    # show
    return render(request, 'tweets.html',
                  {'tweets': tweet})

# //// EDIT

def edit(request, id):
    tweet = Tweet.objects.get(id=id)
    print(tweet)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    else:
        # Show editting screen
        form = TweetForm
        return render(request, 'edit.html',
              {'tweet': tweet, 'form': form})


# /// DELETE

def delete(request, id):
    # Find post
    tweet = Tweet.objects.get(id=id)
    tweet.delete()
    return HttpResponseRedirect('/')



# LIKE COUNT ///////

def tweetLikeAdd(request, id):
  # Get requested tweet
    tweet = Tweet.objects.get(id=id)
  # Add count
    new_like_count = tweet.like_count + 1
    tweet.like_count = new_like_count
  # Save
    print(tweet.like_count)
    tweet.save()
    return HttpResponseRedirect('/')


def tweetLikeSubtract(request, id):
  # Get requested tweet
    tweet = Tweet.objects.get(id=id)
  # Subtract count
    new_like_count = tweet.like_count - 1
    tweet.like_count = new_like_count
  # Save
    tweet.save()
    return JsonResponse({'result': 'successful'})

# //////

