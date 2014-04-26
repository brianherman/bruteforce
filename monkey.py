# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
print "press the buttons"
zero_x = 380
zero_y = 1031

one_x = 249
one_y = 797

two_x = 400
two_y = 776

three_x= 504
three_y = 744

four_x = 234
four_y = 860

five_x = 363
five_y = 861

six_x = 540
six_y = 859

seven_x = 252
seven_y = 931

eight_x = 373
eight_y = 938

nine_x = 528
nine_y = 930


#print "(%d,%d) (%d,%d) (%d,%d)" % (str(b[first][0]),str(b[first][1]), str(b[second][0],b[second][1]), str(b[third][0],b[third][1]), str(b[forth][0],b[forth][1]))
b = [(zero_x,zero_y),(one_x, one_y), (two_x, two_y), (three_x, three_y,),(four_x,four_y),(five_x,five_y),(six_x,six_y),(seven_x,seven_y),(eight_x,eight_y),(nine_x, nine_y)]
for first in range(0,10):
    for second in range (0,10):
        for third in range(0,10):
            for forth in range(0,10):
                print "%d %d %d %d" % (first,second,third,forth)
                device.wake()
                device.touch(b[first][0], b[first][1], 'DOWN_AND_UP')
                MonkeyRunner.sleep(1)
                device.touch(b[second][0], b[second][1], 'DOWN_AND_UP')
                MonkeyRunner.sleep(1)
                device.touch(b[third][0], b[third][1], 'DOWN_AND_UP')
                MonkeyRunner.sleep(1)
                device.touch(b[forth][0], b[forth][1], 'DOWN_AND_UP')
                MonkeyRunner.sleep(1)
                device.touch(535,1015, 'DOWN_AND_UP')
                MonkeyRunner.sleep(1)
                #if (forth % 5)==0:
                #    MonkeyRunner.sleep(30)
#0001
