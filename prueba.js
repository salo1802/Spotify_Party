const {readFileSync, promises: fsPromises} = require('fs');
const fs = require( 'fs' );
const path = require( 'path' );



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



  
    syncReadFile('utils/artists.txt');

function createSongsList(token){
    artists.forEach(artist => {
        let topTracks = getArtistTopTracks(artist,token);
        for(let i = 0; i <= 5; i++) {
            let obj = topTracks[i];
            songs.push(obj.uri);
        }

    });
}



 

  

  

const toptracksfolder = "artistTopTracks";


// Make an async function that gets executed immediately
(async ()=>{
    // Our starting point
    try {
        // Get the files as an array
        const files = await fs.promises.readdir( toptracksfolder );

        // Loop them all with the new for...of
        for( const file of files ) {
            const fromPath = path.join( toptracksfolder, file );
            const contents = readFileSync(fromPath, 'utf-8');
            let topTracks = JSON.parse(contents)
           
            

        
            
            //let obj = JSON.parse(topTracks[i]);
            //console.log("Preuba: "+obj.name)
           
           
        

        topTracks.tracks.forEach(element => {
                
            //console.log(element.name)
            songs.push(element.uri);
        });

        //console.log("-----------------")
            // Log because we're crazy
            //console.log(file);
        } // End for...of

        console.log(songs)
        var file = fs.createWriteStream('songs.txt');
        file.on('error', function(err) { /* error handling */ });
        songs.forEach(song => {
            file.write(`"${song}\",`);
        });
        
        file.end();
    }
    catch( e ) {
        // Catch anything bad that happens
        console.error( "We've thrown! Whoops!", e );
    }

})(); // Wrap in parenthesis and call now
  