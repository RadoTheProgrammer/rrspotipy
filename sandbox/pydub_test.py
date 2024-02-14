

from pydub import AudioSegment

#FILE="/Users/alain/RRS/Rpy/rrytapi/rrytapi_downloads/Ed Sheeran - Shape of You (Official Music Video) audio#140.mp4"
# Replace 'input_file.wav' with your input file and 'output_file.mp3' with your desired output file
input_file = 'audio/sou/sou'
output_file = 'audio/sou/soug2.mp3'

audio = AudioSegment.from_file(input_file)
#file_extension = audio.format

#print(f"The file extension is: {file_extension}")
# Load the audio file
#audio = AudioSegment.from_file(input_file)

# Export the audio to MP3 format
#audio.export(output_file, format='mp3')

