import wx
import noname as gui
import Data
import mainBarang
import mainKaryawan
from wx.core import MessageBox

class FrameWelcome(gui.WelcomeFrame):
    def __init__(self,parent):
        gui.WelcomeFrame.__init__(self,parent)
    def btn_login( self, event ):
        FrameLogin.Show()
        FrameWelcome.Hide()

class Login(gui.FrameLogin):
    def __init__(self,parent):
        gui.FrameLogin.__init__(self,parent)

    def btn_login( self, event ):
        self.manager = Data.Manager()
        self.karyawan = Data.Karyawan()
        mgrlist = self.manager.getDataManager()
        krylist = self.karyawan.getDataKaryawan()
        username = self.input_username.GetValue()
        password = self.input_pw.GetValue()
        Uname = []
        Pass = []
        Nama = []
        Jabatan = []

        for x in mgrlist:
            Uname.append(x[1])
            Pass.append(x[2])
            Nama.append(x[3])
            Jabatan.append(x[4])

        for y in krylist:
            Uname.append(y[1])
            Pass.append(y[2])
            Nama.append(y[3])
            Jabatan.append(y[4])

        for i in range(len(Uname)):
            print(i)
            if username == Uname[i] and password == Pass[i]:
                if Jabatan[i] == "Manager":
                    FrameMgr.Show()
                    FrameLogin.Hide()
                elif Jabatan[i] != "Manager" :
                    FrameKry.Show()
                    FrameLogin.Hide()
            else :
                print("Username atau password salah!!")
                

class FrameBarang2 (gui.FrameBarang):
    def __init__(self,parent):
        gui.FrameBarang.__init__(self,parent)
    def btn_back( self, event ):
        FrameKry.Show()
        FrameBarang2.Hide()


class FrameMgr(gui.FrameMenuMgr):
    def __init__(self,parent):
        gui.FrameMenuMgr.__init__(self,parent)
    def btn_barang( self, event ):
        FrameBarang1.Show()
        FrameMgr.Hide()
    def btn_karyawan( self, event ):
        FrameKaryawan.Show()
        FrameMgr.Hide()
    def btn_back( self, event ):
        FrameLogin.Show()
        FrameMgr.Hide()

class FrameKry(gui.FrameMenuKry):
    def __init__(self,parent):
        gui.FrameMenuKry.__init__(self,parent)
    def btn_barang1(self, event):
        FrameBarang2.Show()
        FrameKry.Hide()
    def btn_profil( self, event ):
        FrameProfil.Show()
        FrameKry.Hide()
    def btn_back( self, event ):
        FrameLogin.Show()
        FrameKry.Hide()


class FrameInputKr(gui.FrameInputKry):
    def __init__(self,parent):
        gui.FrameInputKry.__init__(self,parent)


class FrameProfil(gui.FrameProfilKry):
    def __init__(self,parent):
        gui.FrameProfilKry.__init__(self,parent)
    def btn_back( self, event ):
        FrameKry.Show()
        FrameProfil.Hide()

class FrameLapor(gui.FrameLaporMgr):
    def __init__(self, parent):
        gui.FrameLaporMgr.__init__(self, parent)
        self.showDataLapor()
    
    def btn_back(self):
        FrameBarang1.Show()
        FrameLapor.Hide()    
    
    def showDataLapor(self):
        n_cols = self.tabel_lapor.GetNumberCols()
        n_rows = self.tabel_lapor.GetNumberRows()
        if n_cols > 0:
            self.tabel_lapor.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_lapor.DeleteRows(0, n_rows, True)

        kolom = ['ID Lapor', 'ID Barang', 'Username']
        self.tabel_lapor.AppendCols(len(kolom))

        self.lapor = Data.Lapor()
        listLaporan = self.lapor.getDataLapor()
        row = 0

        self.listIDLaporan = []
        for col in range(len(kolom)):
            self.tabel_lapor.SetColLabelValue(col, kolom[col]) 
        for row_lapor in listLaporan:
            self.tabel_lapor.AppendRows(1)
            print(row, '. ', row_lapor)
            id_laporan, no_barang, username= row_lapor
            lpr=str(no_barang)
            no_kry=str(username)
            self.tabel_lapor.SetCellValue(row, 0, lpr)
            self.tabel_lapor.SetCellValue(row, 1, no_kry)
            self.listIDLaporan.append(id_laporan)
            row += 1


app=wx.App()
FrameWelcome=FrameWelcome(None)
FrameLogin=Login(None)
FrameMgr=FrameMgr(None)
FrameKry=FrameKry(None)
FrameKaryawan=mainKaryawan.FrameKaryawan(None)
FrameBarang1=mainBarang.FrameBarang1(None)
FrameBarang2=FrameBarang2(None)
FrameProfil=FrameProfil(None)
FrameLapor=FrameLapor(None)

# FrameWelcome.Show()
# FrameLogin.Show()
# FrameMgr.Show()
# FrameKry.Show()
FrameKaryawan.Show()
# FrameBarang1.Show()
# FrameBarang2.Show()
# FrameInput.Show()
# FrameProfil.Show()
# FrameInputLp.Show()
# FrameInputKr.Show()

app.MainLoop()