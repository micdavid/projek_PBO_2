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
        self.karyawan = Data.Karyawan()
        mgrlist = self.manager.getDataManager()
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

        for x in array_user:
            print(x)
            if username == array_user and password == array_pw:
                if array_nama[x]== "":
                    FrameMgr.Show()
                    FrameLogin.Hide()
                else :
                    FrameKry.Show()
                    FrameLogin.Hide()
            else :
                print("Error mas")
                    

        

class Welcome(gui.WelcomeFrame):
    def __init__(self,parent):
        gui.WelcomeFrame.__init__(self,parent)

class FrameBarang1 (gui.FrameBarangMgr):
    def __init__(self,parent):
        gui.FrameBarangMgr.__init__(self,parent)
    def btn_back( self, event ):
        FrameMgr.Show()
        FrameBarang1.Hide()
    def btn_tambah(self, event):
        FrameInput.Show()
        FrameBarang1.Hide()

class FrameBarang2 (gui.FrameBarang):
    def __init__(self,parent):
        gui.FrameBarang.__init__(self,parent)
        
        
class FrameInput(gui.FrameInputBarang):
    def __init__(self,parent):
        gui.FrameInputBarang.__init__(self,parent)

class FrameKaryawan(gui.FrameKaryawanMgr):
    def __init__(self,parent):
        gui.FrameKaryawanMgr.__init__(self,parent)
    def btn_back( self, event ):
        FrameMgr.Show()
        FrameKaryawan.Hide()

# class FrameProfil (gui.FrameProfilKry):
#     def __init__(self,parent):
#         gui.FrameKaryawanMgr.__init__(self,parent)

class FrameMgr(gui.FrameMenuMgr):
    def __init__(self,parent):
        gui.FrameMenuMgr.__init__(self,parent)
    def btn_barang( self, event ):
        FrameBarang1.Show()
        FrameMgr.Hide()
    def btn_karyawan( self, event ):
        FrameKaryawan.Show()
        FrameMgr.Hide()

class FrameKry(gui.FrameMenuKry):
    def __init__(self,parent):
        gui.FrameMenuKry.__init__(self,parent)
    def btn_barang1(self, event):
        FrameBarang2.Show()
        FrameKry.Hide()





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
FrameKaryawan=FrameKaryawan(None)
FrameBarang1=FrameBarang1(None)
FrameBarang2=FrameBarang2(None)
FrameInput=FrameInput(None)
# FrameProfil=FrameProfil(None)

# framewelcome.Show()
# FrameLogin.Show()
# FrameMgr.Show()
# FrameKry.Show()
# FrameKaryawan.Show()
FrameBarang1.Show()
# FrameBarang2.Show()
# FrameInput.Show()
# FrameProfil.Show()

app.MainLoop()