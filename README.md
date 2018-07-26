## Music recommendation
### Music recommendation using Lyrics

According to easy access to the media, the music market has grown fast and the digital music industry is growing rapidly. Music recommendation also became important field.

Important information to make up the music includes the title of the song, There are the name of the singer, the speed, etc. But this time I just use only lyrics, because of the limitations of collecting attribute variables.

>> "Semantic analysis of song lyrics." Logan, Beth, Andrew Kositsky, and Pedro Moreno.
Multimedia and Expo, 2004

We can classify artists by their lyrics. Therefore, we can judge that the lyrics of a song can have a big impact on selection of music.


#### Data
* 'MELON' website (http://www.melon.com/)
Collect in order of popular rankings for POP music (Title, Singer)
* Use POP, Rock/Metal, R&B/Soul, Folk/Blues/Country genre
* Collect lyrics from 'AZLyrics' website (https://www.azlyrics.com/)
* Use 'Emolex' sentiment vocab

#### Framework
* Collect data from website
* Keyword extraction and data pre-processing
* Similarity analysis
