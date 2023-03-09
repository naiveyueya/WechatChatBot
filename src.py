'''
 @decription: Forming a chatbot for Wechat
 @author: Yueya
 @version:0.0.1
 @date:20230310
'''
#%% lib
from wxauto import *


#%%
def Monitor_Mesaage(to=False):
    '''
    Monitor message
    :param to: the one who u want to spy
    :return:
    '''
    wx, ind = WeChat(), 1
    if to:
        wx.Search(keyword=to)
    else:
        wx.GetSessionList()
    msg = wx.GetLastMessage
    try:
        if msg[0] == to:
            return msg
    except:
        return msg
