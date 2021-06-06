import wx
import noname as gui
import Data

# class InputBarang(gui.panel_input_data_brg):
#     def __init__(self,parent):
#         self.parent = parent

#     def input_brg(self, id_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
#         self.input_id_barang.SetValue(id_barang)
#         self.input_nama_barang.SetValue(id_barang)
#         self.input_jenis_barang.SetValue(id_barang)
#         self.input_harga_barang.SetValue(id_barang)
#         self.input_stok_barang.SetValue(id_barang)

class Login(gui.FrameLogin):
    def __init__(self,parent):
        gui.FrameLogin.__init__(self,parent)

    def btn_login( self, event ):
        self.manager = Data.Manager()
        mgrlist = self.manager.getDataManager()
        self.karyawan = Data.Karyawan()
        krylist = self.karyawan.getDataKaryawan()
        username = self.input_username.GetValue()
        password = self.input_pw.GetValue()

        array_user = []
        array_pw = []
        array_nama = []

        for i in mgrlist:
            array_user.append(i[0])
            array_pw.append(i[1])

        for j in krylist:
            array_user.append(j[0])
            array_pw.append(j[1])
            array_nama.append(j[2])

        # print(array_user)
        # print(array_pw)
        # print(array_nama)

        for x in range (len(array_nama)):
            print(x)
            if username == array_user[x] and password == array_pw[x]:
                if array_nama[x]== "":
                    FrameMgr.Show()
                    FrameLogin.Hide()
                else :
                    FrameKry.Show()
                    FrameLogin.Hide()
            else :
                print("Error mas")
                    
class FrameMgr(gui.FrameMenuMgr):
    def __init__(self,parent):
        gui.FrameMenuMgr.__init__(self,parent)
    def btn_barang( self, event ):
        FrameBarang.Show()
        FrameMgr.Hide()
    def btn_karyawan( self, event ):
        FrameKryawan.Show()
        FrameMgr.Hide()

        
class FrameKry(gui.FrameMenuKry):
    def __init__(self,parent):
        gui.FrameMenuKry.__init__(self,parent)

class Welcome(gui.WelcomeFrame):
    def __init__(self,parent):
        gui.WelcomeFrame.__init__(self,parent)

class FrameKryawan(gui.FrameKaryawanMgr):
    def __init__(self,parent):
        gui.FrameKaryawanMgr.__init__(self,parent)

class FrameBarang(gui.FrameBarangKry):
    def __init__(self,parent):
        gui.FrameBarangKry.__init__(self,parent)

# class Toko(gui.panel_barang_mgr):
#     def __init__(self,parent):
#         gui.panel_barang_mgr.__init__(self,parent)
        # self.initData()

    # def insertDataBrg(self, id_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
    #     self.mhs.setDataMahasiswa(nama, email, nim, tahunMasuk)
    #     self.initData()
    #     self.AddButtonEditDelete()

    # def updateDataBrg(self, id_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
    #     self.mhs.updateMahasiswa(id_person, nama, email, nim, tahunMasuk)
    #     self.initData()
    #     self.AddButtonEditDelete()

app=wx.App()
framewelcome=Welcome(None)
FrameLogin=Login(None)
FrameMgr=FrameMgr(None)
FrameKry=FrameKry(None)
FrameKryawan=FrameKryawan(None)
FrameBarang=FrameBarang(None)

FrameLogin.Show()
# FrameMgr.Show()
# FrameKryawan.Show()
# FrameBarang.Show()
app.MainLoop()