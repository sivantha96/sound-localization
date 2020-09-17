import audioop
import numpy as np
import time

# function to get the threshold value from an audio stream
def get_threshold(stream, should_stop):
    threshold_array = np.zeros((120,), dtype=int)
    for i in range(300):
        data = stream.read(4096, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        if rms < 10:
            threshold_array[0] = threshold_array[0] + 1
        elif rms < 20:
            threshold_array[1] = threshold_array[1] + 1
        elif rms < 30:
            threshold_array[2] = threshold_array[2] + 1
        elif rms < 40:
            threshold_array[3] = threshold_array[3] + 1
        elif rms < 50:
            threshold_array[4] = threshold_array[4] + 1
        elif rms < 60:
            threshold_array[5] = threshold_array[5] + 1
        elif rms < 70:
            threshold_array[6] = threshold_array[6] + 1
        elif rms < 80:
            threshold_array[7] = threshold_array[7] + 1
        elif rms < 90:
            threshold_array[8] = threshold_array[8] + 1
        elif rms < 100:
            threshold_array[9] = threshold_array[9] + 1
        elif rms < 110:
            threshold_array[10] = threshold_array[10] + 1
        elif rms < 120:
            threshold_array[11] = threshold_array[11] + 1
        elif rms < 130:
            threshold_array[12] = threshold_array[12] + 1
        elif rms < 140:
            threshold_array[13] = threshold_array[13] + 1
        elif rms < 150:
            threshold_array[14] = threshold_array[14] + 1
        elif rms < 160:
            threshold_array[15] = threshold_array[15] + 1
        elif rms < 170:
            threshold_array[16] = threshold_array[16] + 1
        elif rms < 180:
            threshold_array[17] = threshold_array[17] + 1
        elif rms < 190:
            threshold_array[18] = threshold_array[18] + 1
        elif rms < 200:
            threshold_array[19] = threshold_array[19] + 1
        elif rms < 210:
            threshold_array[20] = threshold_array[20] + 1
        elif rms < 220:
            threshold_array[21] = threshold_array[21] + 1
        elif rms < 230:
            threshold_array[22] = threshold_array[22] + 1
        elif rms < 240:
            threshold_array[23] = threshold_array[23] + 1
        elif rms < 250:
            threshold_array[24] = threshold_array[24] + 1
        elif rms < 260:
            threshold_array[25] = threshold_array[25] + 1
        elif rms < 270:
            threshold_array[26] = threshold_array[26] + 1
        elif rms < 280:
            threshold_array[27] = threshold_array[27] + 1
        elif rms < 290:
            threshold_array[28] = threshold_array[28] + 1
        elif rms < 300:
            threshold_array[29] = threshold_array[29] + 1
        elif rms < 310:
            threshold_array[30] = threshold_array[30] + 1
        elif rms < 320:
            threshold_array[31] = threshold_array[31] + 1
        elif rms < 330:
            threshold_array[32] = threshold_array[32] + 1
        elif rms < 340:
            threshold_array[33] = threshold_array[33] + 1
        elif rms < 350:
            threshold_array[34] = threshold_array[34] + 1
        elif rms < 360:
            threshold_array[35] = threshold_array[35] + 1
        elif rms < 370:
            threshold_array[36] = threshold_array[36] + 1
        elif rms < 380:
            threshold_array[37] = threshold_array[37] + 1
        elif rms < 390:
            threshold_array[38] = threshold_array[38] + 1
        elif rms < 400:
            threshold_array[39] = threshold_array[39] + 1
        elif rms < 410:
            threshold_array[40] = threshold_array[40] + 1
        elif rms < 420:
            threshold_array[41] = threshold_array[41] + 1
        elif rms < 430:
            threshold_array[42] = threshold_array[42] + 1
        elif rms < 440:
            threshold_array[43] = threshold_array[43] + 1
        elif rms < 450:
            threshold_array[44] = threshold_array[44] + 1
        elif rms < 460:
            threshold_array[45] = threshold_array[45] + 1
        elif rms < 470:
            threshold_array[46] = threshold_array[46] + 1
        elif rms < 480:
            threshold_array[47] = threshold_array[47] + 1
        elif rms < 490:
            threshold_array[48] = threshold_array[48] + 1
        elif rms < 500:
            threshold_array[49] = threshold_array[49] + 1
        elif rms < 510:
            threshold_array[50] = threshold_array[50] + 1
        elif rms < 520:
            threshold_array[51] = threshold_array[51] + 1
        elif rms < 530:
            threshold_array[52] = threshold_array[52] + 1
        elif rms < 540:
            threshold_array[53] = threshold_array[53] + 1
        elif rms < 550:
            threshold_array[54] = threshold_array[54] + 1
        elif rms < 560:
            threshold_array[55] = threshold_array[55] + 1
        elif rms < 570:
            threshold_array[56] = threshold_array[56] + 1
        elif rms < 580:
            threshold_array[57] = threshold_array[57] + 1
        elif rms < 590:
            threshold_array[58] = threshold_array[58] + 1
        elif rms < 600:
            threshold_array[59] = threshold_array[59] + 1
        elif rms < 610:
            threshold_array[60] = threshold_array[60] + 1
        elif rms < 620:
            threshold_array[61] = threshold_array[61] + 1
        elif rms < 630:
            threshold_array[62] = threshold_array[62] + 1
        elif rms < 640:
            threshold_array[63] = threshold_array[63] + 1
        elif rms < 650:
            threshold_array[64] = threshold_array[64] + 1
        elif rms < 660:
            threshold_array[65] = threshold_array[65] + 1
        elif rms < 670:
            threshold_array[66] = threshold_array[66] + 1
        elif rms < 680:
            threshold_array[67] = threshold_array[67] + 1
        elif rms < 690:
            threshold_array[68] = threshold_array[68] + 1
        elif rms < 700:
            threshold_array[69] = threshold_array[69] + 1
        elif rms < 710:
            threshold_array[70] = threshold_array[70] + 1
        elif rms < 720:
            threshold_array[71] = threshold_array[71] + 1
        elif rms < 730:
            threshold_array[72] = threshold_array[72] + 1
        elif rms < 740:
            threshold_array[73] = threshold_array[73] + 1
        elif rms < 750:
            threshold_array[74] = threshold_array[74] + 1
        elif rms < 760:
            threshold_array[75] = threshold_array[75] + 1
        elif rms < 770:
            threshold_array[76] = threshold_array[76] + 1
        elif rms < 780:
            threshold_array[77] = threshold_array[77] + 1
        elif rms < 790:
            threshold_array[78] = threshold_array[78] + 1
        elif rms < 800:
            threshold_array[79] = threshold_array[79] + 1
        elif rms < 810:
            threshold_array[80] = threshold_array[80] + 1
        elif rms < 820:
            threshold_array[81] = threshold_array[81] + 1
        elif rms < 830:
            threshold_array[82] = threshold_array[82] + 1
        elif rms < 840:
            threshold_array[83] = threshold_array[83] + 1
        elif rms < 850:
            threshold_array[84] = threshold_array[84] + 1
        elif rms < 860:
            threshold_array[85] = threshold_array[85] + 1
        elif rms < 870:
            threshold_array[86] = threshold_array[86] + 1
        elif rms < 880:
            threshold_array[87] = threshold_array[87] + 1
        elif rms < 890:
            threshold_array[88] = threshold_array[88] + 1
        elif rms < 900:
            threshold_array[89] = threshold_array[89] + 1
        elif rms < 910:
            threshold_array[90] = threshold_array[90] + 1
        elif rms < 920:
            threshold_array[91] = threshold_array[91] + 1
        elif rms < 930:
            threshold_array[92] = threshold_array[92] + 1
        elif rms < 940:
            threshold_array[93] = threshold_array[93] + 1
        elif rms < 950:
            threshold_array[94] = threshold_array[94] + 1
        elif rms < 960:
            threshold_array[95] = threshold_array[95] + 1
        elif rms < 970:
            threshold_array[96] = threshold_array[96] + 1
        elif rms < 980:
            threshold_array[97] = threshold_array[97] + 1    
        elif rms < 990:
            threshold_array[98] = threshold_array[98] + 1
        elif rms < 1000:
            threshold_array[99] = threshold_array[99] + 1
        elif rms < 1010:
            threshold_array[100] = threshold_array[100] + 1
        elif rms < 1020:
            threshold_array[101] = threshold_array[101] + 1
        elif rms < 1030:
            threshold_array[102] = threshold_array[102] + 1
        elif rms < 1040:
            threshold_array[103] = threshold_array[103] + 1
        elif rms < 1050:
            threshold_array[104] = threshold_array[104] + 1
        elif rms < 1060:
            threshold_array[105] = threshold_array[105] + 1
        elif rms < 1070:
            threshold_array[106] = threshold_array[106] + 1
        elif rms < 1080:
            threshold_array[107] = threshold_array[107] + 1
        elif rms < 1090:
            threshold_array[108] = threshold_array[108] + 1
        elif rms < 1100:
            threshold_array[109] = threshold_array[109] + 1
        elif rms < 1110:
            threshold_array[110] = threshold_array[110] + 1
        elif rms < 1120:
            threshold_array[111] = threshold_array[111] + 1
        elif rms < 1130:
            threshold_array[112] = threshold_array[112] + 1
        elif rms < 1140:
            threshold_array[113] = threshold_array[113] + 1
        elif rms < 1150:
            threshold_array[114] = threshold_array[114] + 1
        elif rms < 1160:
            threshold_array[115] = threshold_array[115] + 1
        elif rms < 1170:
            threshold_array[116] = threshold_array[116] + 1
        elif rms < 1180:
            threshold_array[117] = threshold_array[117] + 1
        elif rms < 1190:
            threshold_array[118] = threshold_array[118] + 1
        else:
            threshold_array[119] = threshold_array[119] + 1
        if should_stop.value == 1:
            break
    threshold = (np.argmax(threshold_array) + 3)*10
    return int(threshold)
