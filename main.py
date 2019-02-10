# Domain Availability Check

from nltk import FreqDist
from nltk.corpus import brown
import requests
import json
import re

words = []
frequency_list = FreqDist(i.lower() for i in brown.words())
for pair in frequency_list.most_common():
    # Simple regex match to avoid special characters
    if len(pair[0]) >= 7 and re.fullmatch('[a-z]+', pair[0]) is not None:
        words.append(pair[0])
    if len(words)==500:
        break


def get_availability(words):
    """
    Returns a dictionary with word as key and availability as value.
    Input:
        works - Iterable of words
    """
    result = {}
    for i in range(len(words)):
        try:
            domain = words[i] + '.com'
            response = requests.get("https://jsonwhois.com/api/v1/whois",headers={
                                "Accept": "application/json",
                                "Authorization": "Token token=<your token>"},  # Replace your token key here
                        params={"domain": domain})
            content = response.content
            content = content.decode('utf-8')
            json_content = json.loads(content)
            result[domain] = json_content['available?']
        except:
            print(domain)
    return result
    
    
    
availabilities = get_availability(words)

# Print the available domains
for domain in availabilities:
    if availabilities[domain]:
        print(domain)

