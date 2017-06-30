import urllib

def read_text():
	quotes = open("/home/nrohankar/Desktop/Python/PythonPractice/movie_quotes.txt")
	conents_of_file = quotes.read()
	print(conents_of_file)
	quotes.close()
	check_profanity2(conents_of_file)

def check_profanity2(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")

read_text()