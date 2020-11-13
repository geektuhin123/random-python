#!/usr/bin/env python
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import copy
# import yaml
import json

'''
  Instructions

  -> Works with both Python 2x and 3x.
  -> Install bs4 and requests package( pip install bs4 requests pyyaml ).
     For python 3 (pip3 install bs4 requests pyyaml)
  -> Run this file ( python scripts/scrapper.py ).
  -> Run scripts/aws-regions-check.coffee.
  -> Happy coding..!!

'''
req = Request('https://visualbi.com/about-us/our-team')
webpage = urlopen(req).read()
# url = "https://visualbi.com/about-us/our-team/"

# data  = requests.get(url)

# soup = BeautifulSoup(data.content, 'html.parser')

# print(webpage)

# pool = soup.findAll("div", attrs={"class": "aws-table", "data-is-sticky-header": "true"})

# americas = pool[0].find("tbody")
# europe = pool[1].find("tbody")
# asia = pool[2].find("tbody")

# regions = {} # regions dictionary

# us_regions = ['us-east-1', 'us-east-2', 'us-west-2', 'us-west-1', 'ca-central-1', 'sa-east-1', 'us-gov-west-1']
# eu_regions = ['eu-west-1', 'eu-central-1', 'eu-west-2', 'eu-west-3']
# asia_regions = ['ap-southeast-1', 'ap-northeast-1', 'ap-northeast-3', 'ap-southeast-2', 'ap-northeast-2', 'ap-south-1', 'cn-north-1', 'cn-northwest-1']
# unwanted_list = ['cn-north-1', 'cn-northwest-1', 'us-gov-west-1']

# region_names = us_regions + eu_regions + asia_regions


# for continent in [americas,europe,asia]:
#   for tr in continent:
#     if tr.find("a") != -1 and tr.find("a") != None:
#       # print tr.find("a").get_text()
#       key = str(tr.find("a").get_text()).rstrip()  # rstrip() to match "Lex" and "Lex "

#       # Handling Deformities Manually
#       if key == "AWS 1-Click":
#         key = "AWS IoT 1-Click"

#       if key not in regions.keys():
#         regions[key] = []

#       for td in tr:
#         if td.find("a") != -1 and td.find("a") == None:
#           if td.get_text() == u'\u2713':
#             regions[key].append(True)
#           else:
#             regions[key].append(False)

# # Handling the missing <td> </td> for some services
# if regions["AWS Device Farm"] and len(regions["AWS Device Farm"]) == 18:
#   regions["AWS Device Farm"].append(False)
# if regions["AWS Sumerian"] and len(regions["AWS Sumerian"]) == 20:
#   regions["AWS Sumerian"].pop()
# if regions["AWS Firewall Manager"] and len(regions["AWS Firewall Manager"]) == 7:
#   regions["AWS Firewall Manager"].extend([False] * 12)
# if regions["AWS Single Sign-On"] and len(regions["AWS Single Sign-On"]) == 7:
#   regions["AWS Single Sign-On"].extend([False] * 12)

# # Get list of supported regions for complete fetch
# perfect_list = {}
# for item in regions:
#   if len(regions[item]) == 19:	# If the service is in all tables and has 19 values
#     perfect_list[item] = []
#     for x in range(0, 19):
#       if regions[item][x] == True:
#         perfect_list[item].append(region_names[x])
#     perfect_list[item].sort()


# for item in perfect_list:			# sorted(perfect_list, key=lambda s: s.lower())
# 	print item , ": ", perfect_list[item]

# print "\n\nDeformities\n\n"

# for item in regions:
# 	if len(regions[item]) < 19:
# 		print item,": ", regions[item]


# Writing into a yml file

# yml_list = copy.deepcopy(perfect_list)
# for item in yml_list:
#   str = ""
#   for element in yml_list[item]:
#     if element not in unwanted_list:
#       str += "- " + element + "\\n"
#   yml_list[item] = [str[:-2]]

# with open('regions.yml', 'w') as outfile:
#     yaml.dump(yml_list, outfile, default_flow_style=False)


# # Writing into a JSON file
# json_list = copy.deepcopy(perfect_list)
# for item in json_list:
#   str = ""
#   for element in json_list[item]:
#     if element not in unwanted_list:
#       str += "- " + element + "\n"
#   json_list[item] = str[:-1]

# with open('../regions.json', 'w') as outfile:
#     json.dump(json_list, outfile, indent=2, sort_keys=True)
