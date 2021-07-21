# Import urllib for downloading url's and sys for errors
import urllib.request
import sys

# Add a dummy url to start the while loop
url_link = 'http://www.google.com'

# Add empty dictionary to store search findings as key-pair values.
url_dict = {}

'''
Add while loop to start the url search. Enclose the try excpet block 
inside the while that way if and error occurs the programg can continue
to run.
'''

while url_link != '':
	try:
		url_link = input('Please enter a url? ')
		if url_link == '':
			print ('Ok, exiting the loop')
			break
		short_name = input('Please enter a short name for that url ' + url_link + '. ')
		# Download, open,and read the url being searched in HTML format 
		# and returned as a string then stored as key-value pair in the
		# empty dictoinary.
		web_page = urllib.request.urlopen(url_link).read()
		url_dict[short_name] = web_page
	except:
		print('Unexpected error', sys.exc_info()[0])
		stop_or_proceed = input('An error has occured to proceed enter 1 and to stop enter anything else.')
		if stop_or_proceed == '1':
			print('Stopping!\n')
			break
		else:
			print('Proceeding!\n')
			continue
	print('This line is inside the while loop, but not inside the try block')
print('This line is completely outside the while loop.')
print(url_dict.keys())
