import pyaudio

p = pyaudio.PyAudio()

info = p.get_host_api_info_by_index(0)
num = info.get('deviceCount')

for i in range(0, num):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')):
        print("Input Device id = ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))