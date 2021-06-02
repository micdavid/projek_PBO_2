import wx
import noname

class Toko1(noname.MyFrame1):
    def __init__(self,parent):
        noname.MyFrame1.__init__(self,parent)

app=wx.App()
frame=Toko1(None)
frame.Show()
app.MainLoop()