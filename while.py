import sounddevice
from scipy.io.wavfile import write
fs = 44100


second = int(input("Enter the recording time in second: "))
print("recording....\n")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs,channels=2)
sounddevice.wait()
write("Myrecording.wav" , fs, record_voice)
print("recording is done Please check your folderto listen recording")
input()