'''

This piece of code merges two mp3 audio files.

This code needs the following dependencies:
 	- pydub
	- ffmpeg

Install dependencies by executing the following commands:
	$pip install pydub
	$brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora

Author: __Viki( vikiworks.io )

'''
import sys
from pydub import AudioSegment

def main():
    if len(sys.argv) < 3:
        print "USAGE: python audio_joiner.py <mp3 file1> <mp3 file2> <output file name>"
        exit(0)

    faudio1 = sys.argv[1]
    faudio2 = sys.argv[2]
    fmerged = sys.argv[3]
    if not faudio1.endswith('.mp3') and not faudio2.endswith('.mp3'):
        print "Unrecognized extension, This software only supports .mp3 extension"
        exit(0)

    audio1 = AudioSegment.from_mp3(faudio1)
    audio2 = AudioSegment.from_mp3(faudio2)
    merged_audio = audio1 + audio2
    merged_audio.export(fmerged, format="mp3")

if __name__ == "__main__":
    main()
