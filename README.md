## PYTHON SCRIPT TO JOIN TWO mp3 FILES

##### USAGE:

	$python audio_joiner.py <mp3 file 1> <mp3 file 2> <output file name>

##### Example:

	The following command will join two mp3 files 1.mp3, 2.mp3 and store the merged file in out.mp3
	$python audio_joiner.py 1.mp3 2.mp3 out.mp3

##### Dependencies:

	This code needs the following dependencies:
    	- pydub
    	- ffmpeg

##### Install dependencies by executing the following commands:
    	$pip install pydub
    	$brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora
