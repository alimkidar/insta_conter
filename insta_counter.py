print ("Memulai")
import pandas as pd
import requests
import json
import re


#Untuk ambil jumlah followers dan following di instagram
def insta(user_name):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	ff = []
	situs = 'https://www.instagram.com/' + user_name + '/'
	try: 
		response = requests.get(url=situs, headers=headers)
	except: 
		print ("Koneksi Internet Error!")
	try:
		json_match = re.search(r'window\._sharedData = (.*);</script>', response.text)
		profile_json = json.loads(json_match.group(1))['entry_data']['ProfilePage'][0]['graphql']['user']


		follower_temp = profile_json['edge_followed_by']['count']
		following_temp = profile_json['edge_follow']['count']
		status_username = True #User ditemukan
	except:
		follower_temp = "-"
		following_temp = "-"
		status_username = False #User tidak ada

	ff.append(follower_temp)
	ff.append(following_temp)
	ff.append(status_username) 
	return ff

hit = 1

#Seting Output
output_name = "username_statistics.csv"
f = open(output_name, "w")
label = "No,Username,Following,Followers\n"
f.write(label)

dfdict = pd.read_csv('username.csv')
for index, row in dfdict.iterrows():
	username = row['username']
	response = insta(username)
	follower = response[0]
	following = response[1]
	f.write(str(hit) + "," + username  + "," + str(following) + "," +  str(follower) + "\n")
	print (str(hit) + ". Username: " + username  + " Followers: " + str(follower) + ". Following: " + str(following) + ".")
	hit += 1


f.close()
print ("Selesai")