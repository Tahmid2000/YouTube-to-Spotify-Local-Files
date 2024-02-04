
# YouTube to Spotify Local Files

There is a lot of unreleased music on YouTube and I wish I could listen to directly on the Spotify app. I can manually download these files and then move them my Spotify playlists using Spotify's Local Files feature. 

Unfortunately, the Spotify API currently doesn't allow much configuration with local files, so I had to figure out a roundabout way of adding my local files to my liked songs.

This short CLI app downloads a YouTube video as a mp3 file and then navigates the macOS Spotify GUI to add the newly downloaded audio file to my liked songs.

***

**NOTE: Naviagting the Spotify GUI using pyautogui is very glitchy and is heavily dependent on how the Spotify GUI layout. Please update the coordinates with the appropriate values.**

