# %%
from moviepy.editor import *
import os

# %%
# load audios
audios_input = './lingjian/v5/'
li_temp = list(map(lambda x: audios_input + x, sorted(os.listdir(audios_input))))
li_input = list(filter(lambda audios_input: audios_input.endswith('.MP3'), li_temp))
num = len(li_input)
print(num)


# %%
li_input

# %%
### modify and combine
L = []

# start at half
# adstart = AudioFileClip(li_input[0])
# adstart_v = adstart.subclip(917,adstart.duration)
# L.append(adstart_v)

# # remove unified pre
for i in range(0, num-1): #note
    ad = AudioFileClip(li_input[i])
    ad_v = ad.subclip(29.6,ad.duration) # cut off the first 29.6s
    L.append(ad_v)
    #print(ad_v.start, ad_v.end, ad_v.duration)
    
# # end at half
adend = AudioFileClip(li_input[-1])
adend_v = adend.subclip(29.6, 524.5)
L.append(adend_v)

final_clip = concatenate_audioclips(L) 

# %%
# write out
audios_output = './lingjian/v5.mp3'
final_clip.write_audiofile(audios_output)

# %%
## add cover pic
audioclip = AudioFileClip("./result/vol.mp3")
imgclip = ImageClip("mountain.jpg")
vd = imgclip.set_duration(audioclip.duration).set_audio(audioclip)#.fx( vfx.speedx, 1.2)

# too big not work
vd.write_videofile('./result/vd.mp4', fps=30)

# %%
