import datetime
print("ffmpeg -i 1.mp4 -ss 00:00:00 -t 00:00:02 output1.ts")



a = datetime.datetime(100,1,1,00,00,00)
#b = a + datetime.timedelta(0,2)# add two seconds

#print (b.time())




b = a + datetime.timedelta(0,2)# add two seconds

print("ffmpeg -i 1.mp4 -ss",b.time(),"-t 00:00:02 output2.ts")



counter = 3
while counter < 301:
    
  b = b + datetime.timedelta(0,2)# add two seconds
  print("ffmpeg -i 1.mp4 -ss",b.time(),"-t 00:00:02 output{}.ts".format(counter))
  counter+=1
#print("ffmpeg -i 1.mp4 -ss 00:00:00 -t 00:00:02 output1.ts")


