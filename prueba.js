const {readFileSync, promises: fsPromises} = require('fs');

artists = []
songs = []

async function asyncReadFile(filename) {
    try {
      const contents = await fsPromises.readFile(filename, 'utf-8');
  
      const arr = contents.split(/\r?\n/);
      artists = arr;
      console.log(arr); // 👉️ ['One', 'Two', 'Three', 'Four']
        
      return arr;
    } catch (err) {
      console.log(err);
    }
  }


  function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');
  
    const arr = contents.split(/\r?\n/);
    artists = arr;
    console.log(arr); // 👉️ ['One', 'Two', 'Three', 'Four']
  
    return arr;
  }


  function getArtistTopTracks(id,token){
    curl -X "GET" `https://api.spotify.com/v1/artists/${id}/top-tracks?market=CO` -H "Accept: application/json" -H "Content-Type: application/json" -H `Authorization: Bearer ${token}`
  }


  
    syncReadFile('utils/artists.txt');

function createSongsList(token){
    artists.forEach(artist => {
        let topTracks = getArtistTopTracks(artist,token);
        for(let i = 0; i < topTracks.length; i++) {
            let obj = topTracks[i];
            songs.push(obj.uri);
        }

    });
}

function addSongsToPlayList(playlistId,token){
    curl -X "PUT" `https://api.spotify.com/v1/playlists/${playlistId}/tracks?uris=${songs}` --data "{\"range_start\":0,\"insert_before\":99,\"range_length\":100}" -H "Accept: application/json" -H "Content-Type: application/json" -H `Authorization: Bearer ${playlistId}`
}
 

  console.log("Prueba:"+artists)
  