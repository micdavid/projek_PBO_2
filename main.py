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
                    

class FrameWelcome(gui.WelcomeFrame):
    def __init__(self,parent):
        gui.WelcomeFrame.__init__(self,parent)
    def btn_login( self, event ):
        FrameLogin.Show()
        FrameWelcome.Hide()

class dlgAddBarang(gui.FrameInputBrg):
    def __init__(self, parent, id=-1):
        gui.FrameInputBrg.__init__(self, parent)
        self.parent=parent
        self.id = id

    def btn_simpan( self, event ):
        dlg= wx.MessageDialog(self, 'simpan data', 'Informasi', style=wx.YES_NO)
        retval= dlg.ShowModal()

        if self.id == -1:
            self.parent.insertDataEmployee(self.ctrlUsername.GetValue(), self.ctrlPassword.GetValue(
            ), self.ctrlNama.GetValue(), self.ctrlGender.GetValue(), self.ctrlAlamat.GetValue(), self.ctrlTelepon.GetValue(), self.ctrlTahunMasuk.GetValue())
        else:
            self.parent.updateDataEmp(self.id, self.ctrlUsername.GetValue(), self.ctrlPassword.GetValue(
            ), self.ctrlNama.GetValue(), self.ctrlGender.GetValue(), self.ctrlAlamat.GetValue(), self.ctrlTelepon.GetValue(), self.ctrlTahunMasuk.GetValue())

        self.Destroy()

    def fillDataEmployee(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.ctrlUsername.SetValue(username)
        self.ctrlPassword.SetValue(password)
        self.ctrlNama.SetValue(nama)
        self.ctrlGender.SetValue(gender)
        self.ctrlAlamat.SetValue(alamat)
        self.ctrlTelepon.SetValue(telepon)
        self.ctrlTahunMasuk.SetValue(tanggalMasuk)

class FrameBarang1 (gui.FrameBarangMgr):
    def __init__(self,parent):
        gui.FrameBarangMgr.__init__(self,parent)
        self.showDataBarang()
        # self.initData()
        # self.AddButtonEditDelete()

    def btn_back( self, event ):
        FrameMgr.Show()
        FrameBarang1.Hide()
    def btn_tambah(self, event):
        # FrameInput.Show()
        FrameBarang1.Hide()

    def showDataBarang(self):
        n_cols = self.tabel_barang.GetNumberCols()
        n_rows = self.tabel_barang.GetNumberRows()
        if n_cols > 0:
            self.tabel_barang.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_barang.DeleteRows(0, n_rows, True)

        kolom = ['ID Barang', 'Nama Barang', 'Jenis Barang', 'Harga Barang', 'Stok Barang']
        self.tabel_barang.AppendCols(len(kolom))

        self.barang = Data.Barang()
        listBarang = self.barang.getDataBarang()
        row = 0

        self.listIdBarang = []
        for col in range(len(kolom)):
            self.tabel_barang.SetColLabelValue(col, kolom[col]) 
        for row_barang in listBarang:
            self.tabel_barang.AppendRows(1)
            print(row, '. ', row_barang)
            id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang = row_barang
            no_item=str(no_barang)
            hrg=str(harga_barang)
            stok=str(stok_barang)
            self.tabel_barang.SetCellValue(row, 0, no_item)
            self.tabel_barang.SetCellValue(row, 1, nama_barang)
            self.tabel_barang.SetCellValue(row, 2, jenis_barang)
            self.tabel_barang.SetCellValue(row, 3, hrg)
            self.tabel_barang.SetCellValue(row, 4, stok)
            self.listIdBarang.append(id)
            row += 1


    def btn_tambah( self, event ):
		dlg = dlgAddBarang(self)
        dlg.ShowModal()

    def insertDataBrg(self, id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.barang.addDataBarang()

    
    def updateDataBrg(self, id_person, nama, email, nim, tahunMasuk):
        self.brg.updateDataBarang(id_person, nama, email, nim, tahunMasuk)
        self.initData()
        self.AddButtonEditDelete()

    def AddBtnBarang (self):
        jmlKolom = self.Karyawan.GetNumberCols()
        self.Karyawan.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.Karyawan.SetColLabelValue(colEdit, '')
        self.Karyawan.SetColLabelValue(colDelete, '')

        for row in range(self.Karyawan.GetNumberRows()):
            self.Karyawan.SetCellValue(row, colEdit, 'Edit')
            self.Karyawan.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.Karyawan.SetCellTextColour(row, colEdit, wx.WHITE)

            self.Karyawan.SetCellValue(row, colDelete, 'Delete')
            self.Karyawan.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.Karyawan.SetCellTextColour(row, colDelete, wx.WHITE)

        self.Karyawan.Fit()
        self.infoAkun.Layout()


class FrameBarang2 (gui.FrameBarang):
    def __init__(self,parent):
        gui.FrameBarang.__init__(self,parent)
    def btn_back( self, event ):
        FrameKry.Show()
        FrameBarang2.Hide()
        

class FrameKaryawan(gui.FrameKaryawanMgr):
    def __init__(self,parent):
        gui.FrameKaryawanMgr.__init__(self,parent)
    def btn_back( self, event ):
        FrameMgr.Show()
        FrameKaryawan.Hide()

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


app=wx.App()
FrameWelcome=FrameWelcome(None)
FrameLogin=Login(None)
FrameMgr=FrameMgr(None)
FrameKry=FrameKry(None)
FrameKaryawan=FrameKaryawan(None)
FrameBarang1=FrameBarang1(None)
FrameBarang2=FrameBarang2(None)
FrameProfil=FrameProfil(None)

# FrameWelcome.Show()
# FrameLogin.Show()
# FrameMgr.Show()
# FrameKry.Show()
# FrameKaryawan.Show()
FrameBarang1.Show()
# FrameBarang2.Show()
# FrameInput.Show()
# FrameProfil.Show()
# FrameInputLp.Show()
# FrameInputKr.Show()

app.MainLoop()