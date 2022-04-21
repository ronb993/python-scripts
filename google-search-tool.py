#### 'pip install google' before running ####

from googlesearch import search
 
# to search
query = "infosec tools"
 
for j in search(query, tld="com", num=10, stop=None, pause=2):
    print(j)
