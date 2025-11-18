from gtts import gTTS  #google  text  to speech
import os
text='ചേലക്കര പോളിടെക്‌നിക് കോളേജിൽ കഴിഞ്ഞ വർഷം പരാജയം ഏറ്റുവാങ്ങുന്ന ഒരു സാഹചര്യം ആയിരുന്നു'
output =gTTS(text=text,lang='ml',slow=False)
output.save('output.mp3')
os.system('start output.mp3')