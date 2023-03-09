'''
 @decription: Forming a chatbot for Wechat
 @author: Yueya
 @version:0.0.1
 @date:20230310
'''
#%% lib
from wxauto import *


#%%
def Monitor_Mesaage(to=False, monitorone=False):
    wx, ind = WeChat(), 1
    if to:
        wx.Search(keyword=to)
    else:
        wx.GetSessionList()
    msg = wx.GetLastMessage
    if monitorone:
        if msg[0] == monitorone:
            return msg
    return msg
