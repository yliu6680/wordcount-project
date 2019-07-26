# HttpResponse function could return the content as html format
from django.http import HttpResponse
#  
from django.shortcuts import render
from operator import itemgetter

def home(request):
	return render(request, 'home.html')

def count(request):
	# get the information (input)
	fulltext = request.GET['fulltext']
	sortted_list, num = count_method(fulltext)
	return render(request, 'count.html', {'fulltext':fulltext, 'count': num, 'sortted_list': sortted_list})

def about(request):
	return render(request, 'about.html')

def count_method(fulltext):
	worddict = {}
	wordlist = fulltext.split()
	for word in wordlist:
		worddict[word] = worddict.get(word, 0) + 1
	# itemgetter is a function that could decide the index that will be used to sorted in this case.
	# in this case, the dict.items() is a list of tuple, the itemgetter will use the value in the position 1.
	# same with lambda kv: kv[1] 
	sortted_list = sorted(worddict.items(), key=itemgetter(1), reverse=True)
	#sortted_list = sorted(worddict.items(), key=lambda kv: kv[1])
	return sortted_list, len(wordlist)
