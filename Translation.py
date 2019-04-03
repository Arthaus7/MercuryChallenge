#Import the google translate package
from google.cloud import traslate
#Phrase-Based Machine Translation Model. 
#For English = en
#For Arabic = ar

def ArTranslation():
	traslate_client = translate.Clint()
	text = u"Translated Text"
	target = 'ar'

	# Translate in to Arabic
	translation = translate_clinet.translate(text, target_language=target)

	#Not sure we need a loop to store the data
	for record in data:
		#fulltext = length of the arabic language

return translation