import json
import codecs
types_of_encoding = ["utf8", "utf-8"]



def get_user_favorite_genres(username):

    jsonFile = "./users/" + username 
    firstList = []
    genres_list = []
    genres_count = {}
    
    firstList = create_genresList(jsonFile)
    genres_list = remove_duplicates(firstList)
    genres_count = count_genres(firstList,genres_list)

    
        
    return genres_count   

def get_user_favorite_genres_list(username):

    jsonFile = "./users/" + username 
    firstList = []
    genres_list = []
    
    
    firstList = create_genresList(jsonFile)
    genres_list = remove_duplicates(firstList)

    return genres_list




# organize the genre list in only one list
def createList(genres_array):
    list = []
    for x in genres_array:
        list.append(x)  
   
    return list   

# create list with all the genres from the top artists 
def create_genresList(jsonFileName):
    # Opening JSON file
    for encoding_type in types_of_encoding:
        with codecs.open(jsonFileName, encoding = encoding_type, errors ='replace') as json_file:
            data = json.load(json_file)
            
            #add the genres that each artist have
            genres_list = []
            for x in data['items']:
                listAllItem = createList(x['genres'])
                for y in listAllItem:
                    genres_list.append(y) 
    return genres_list



#create a list of the genres without dulicates
def remove_duplicates(genres_list):
    nonDuplicates = []
    nonDuplicates = list( dict.fromkeys(genres_list) )
    return nonDuplicates
    
#Count how many artists does the user have per genre
def count_genres(genres_list,nonDuplicates):

    genres_count = {}

    for i in range(len(nonDuplicates)):
        genres_count[nonDuplicates[i]] = 0

    for i in range(len(genres_list)):
        genres_count[genres_list[i]] +=1

    return genres_count 
    


        





