# 5.29 

音频切割的时候，考虑所有音频等分切割

目前为按照固定slot大小切割，此种方法的弊端是被切割的最后一个音频与其他音频时间长度不一样

# 6.1

考虑加速的位置是有音素的还是空隙

# 6.2

This 25ms width is large enough for us to capture enough information and yet the features inside this frame should remain relatively stationary. If we speak 3 words per second with 4 phones and each phone will be sub-divided into 3 stages, then there are 36 states per second or 28 ms per state. So the 25ms window is about right.

Each slid window is about 10ms apart so we can capture the dynamics among frames to capture the proper context.

Starting from an audio clip, we slide windows of 25 ms width and 10 ms apart to extract MFCC features. 

![image-20200602170219251](C:\Users\qinhong\AppData\Roaming\Typora\typora-user-images\image-20200602170219251.png)