import wx
import noname

class Toko(noname.MyFrame1):
    def __init__(self,parent):
        noname.MyFrame1.__init__(self,parent)

app=wx.App()
frame=Toko(None)
frame.Show()
app.MainLoop()