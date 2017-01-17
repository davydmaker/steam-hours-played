#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = "Davyd Maker"
__version__ = "1.0"

import requests

headers = {
    'User-Agent': 'Mozilla/5.0'
}

username = input('Steam Username: ')

r = requests.get('http://steamcommunity.com/id/'+username,headers=headers)
c = r.text

if '<div class="persona_name" style="font-size: 24px;">' not in c:
	print('\nUser does not exist.')
elif '<div class="profile_private_info">' in c:
	print('\nPrivate profile.')
elif '<div class="recentgame_quicklinks recentgame_recentplaytime">' not in c:
	print('\nUser did not play recently.')
else:
	time = c.split('<div class="recentgame_quicklinks recentgame_recentplaytime">')
	time = time[1].strip()
	time = time.split('</div>')
	time = time[0].replace('<h2>','').replace('</h2>','').strip()
	print('\nUser '+username+' played '+time+'.')