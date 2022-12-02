import pandas as pd

def get_group_artists_recommendation(groupArtistsList,mostListenedGenres):
    artistsRatings = []
    df = pd.DataFrame()
   
    for artist in groupArtistsList:
        
        artistPopularity = 0
        for genres in artist[1]:
            
            for x in mostListenedGenres.index:               
                if genres == x:
                    artistPopularity+=1

        artistsRatings.append([artist[0],artistPopularity,artist[2]])
        
        df = pd.DataFrame(artistsRatings,
                  columns = ['Name' , 'Popularity', 'id' ])
        df2 = df.drop_duplicates()          
        df2 = df2.sort_values('Popularity',ascending=False)

    return df2.head(10)

