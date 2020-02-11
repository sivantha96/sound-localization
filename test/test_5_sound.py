import pyaudio
import wave
import audioop

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
#device index found by p.get_device_info_by_index(ii)
dev_1 = 2
# dev_2 = 3
# dev_3 = 4

audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
# stream_1 = audio.open(format = form_1,rate = samp_rate,channels = chans, \
#                     input_device_index = dev_1,input = True, \
#                     frames_per_buffer=chunk)
# 
stream_1 = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_1,input = True, \
                    frames_per_buffer=chunk)

# stream_3 = audio.open(format = form_1,rate = samp_rate,channels = chans, \
#                     input_device_index = dev_1,input = True, \
#                     frames_per_buffer=chunk)
print("recording")

count = 0;
sum = 0;
# loop through stream and append audio chunks to frame array
while True:
    data_1 = stream_1.read(chunk, exception_on_overflow = False)
#     data_2 = stream_2.read(chunk, exception_on_overflow = False)
#     data_3 = stream_3.read(chunk, exception_on_overflow = False)
    
    rms_1 = audioop.rms(data_1, 2)
#     rms_2 = audioop.rms(data_2, 2)
#     rms_3 = audioop.rms(data_3, 2)
    
    print(rms_1)
#     print(rms_2)
#     print(rms_3)
    
    

print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream_1.stop_stream()
stream_1.close()
# stream_2.stop_stream()
# stream_2.close()
# stream_3.stop_stream()
# stream_3.close()
audio.terminate()
