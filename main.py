from utils.user_favorite_genres import get_user_favorite_genres,remove_duplicates,get_user_favorite_genres_list
from utils.user_favorite_artist import get_user_favorite_artists, get_artist_genres
from utils.group_artists_recommendation import get_group_artists_recommendation
import os
import pandas as pd



listofartists = []
listofgenres = []
usersCount = pd.DataFrame()

path_of_the_directory= 'C:/Users/USER/OneDrive/Documentos/STI/Spotify_Party/users'
print("Files and directories in a specified path:")
for filename in os.listdir(path_of_the_directory):
    print(filename)
    #get_user_favorite_genres(filename)
    usersCount = usersCount.append(get_user_favorite_genres(filename), ignore_index=True)
    listofartists.extend(get_user_favorite_artists(filename))
    listofgenres.extend(get_user_favorite_genres_list(filename))
    
    

remove_duplicates(listofartists)
remove_duplicates(listofgenres)

usersCount = usersCount.fillna(0)
df2 = usersCount.mean()
df2 = df2.sort_values(ascending=False)
mostListenedGenres = df2.head(20)
for filename in os.listdir(path_of_the_directory):
    ls = get_artist_genres(filename,listofartists)
    
df3 = pd.DataFrame()

df3 = get_group_artists_recommendation(ls,mostListenedGenres)




print("_____________________________________")
print(df3)
print("----------------------------------------------------")