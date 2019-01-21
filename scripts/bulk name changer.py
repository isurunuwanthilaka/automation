import os
count=0
for afile in os.listdir('.'):
    filename, file_extension = os.path.splitext(afile)
    a=filename[:2]
    b=filename[14:]
    if a.isdigit():
        t=a
    elif b.isdigit():
        t=b
    try:
        os.rename(afile, t+".Niwanmaga- Ven Ududumbara Kashshapa Thero.mp3")
        print(t+".Niwanmaga- Ven Ududumbara Kashshapa Thero.mp3")
        count+=1
    except Exception:
        print(t+".Niwanmaga- Ven Ududumbara Kashshapa Thero.mp3")

print(count)
