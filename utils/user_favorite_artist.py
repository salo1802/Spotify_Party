import json
import codecs
types_of_encoding = ["utf8", "utf-8"]

def get_user_favorite_artists(username):
    print("debug" + username)
    jsonfile = "./users/" + username 

    # Opening JSON file
    with open(jsonfile) as json_file:
        data = json.load(json_file)
    
 #add the genres that each artist have
    artits_list = []
    for x in data['items']:
        artits_list.append(x['name']) 
    return artits_list

#create a list of the artists without dulicates
def get_artist_genres(username, artistsList):

    jsonfile = "./users/" + username 

    # Opening JSON file
    for encoding_type in types_of_encoding:
        with codecs.open(jsonfile, encoding = encoding_type, errors ='replace') as json_file:
            data = json.load(json_file)
        
            
        
    #add the genres that each artist have
        artits_genres_list = artistsList
        for x in data['items']:
            for y in artistsList:
                if y == x['name']:
                    artits_genres_list.append([x['name'],x['genres'],x['id']]) 
    return artits_genres_list


