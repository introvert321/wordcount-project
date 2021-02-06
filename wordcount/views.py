from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] +=1
        else:
	        word_dictionary[word] = 1
    Sortedwords = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=False)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'Sortedwords':Sortedwords})

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'count.html')

def info(request):
    return render(request, 'info.html')
