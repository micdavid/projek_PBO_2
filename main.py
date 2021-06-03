import wx
import noname

class Toko1(noname.MyFrame8):
    def __init__(self,parent):
        noname.MyFrame8.__init__(self,parent)

app=wx.App()
frame=Toko1(None)
frame.Show()
app.MainLoop()