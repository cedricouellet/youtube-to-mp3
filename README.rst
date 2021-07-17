**************
youtube-to-mp3
**************

Download YouTube videos or playlists as MP3 audio files from a url.
###################################################################

::

 usage: youtube-to-mp3 [-h] [-o DIR] [-t S] [-r N] URL
 
 Youtube To MP3 Download Tool
 
 positional arguments:
   URL                The YouTube URL to download. Playlist or single video.
 
 optional arguments:
   -h, --help         show this help message and exit
   -o DIR, --out DIR  The directory in which to store the downloaded MP3 files.
   -t S, --timeout S  Request timeout length in seconds
   -r N, --retry N    Number of retries on failed download
 