# March 2, 2019
# Virus to mess with friends, opens web pages randomly and doesnt stop

import webbrowser
import time
import random

while True:
	sites = random.choice('google.com')
	visit = "http://{}".format(sites)
	webbrowser.open(visit)
	seconds = random.randrange(5,10)
	time.sleep(seconds)
