# DomainAvailability
# My first attempt to mine domain names.

Just a simple script to check if a particular domain is available. The script checks for domain names using common words from the nltk brown corpus dataset. 

I found [JsonWhois](https://jsonwhois.com/) to be the most simple free api to use for this purpose. It allows you to make 500 calls without any charge. 

However, for some domain names it returns a status code of 500. For these domains, the domain names are printed. 
