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

class FrameBarang1 (gui.FrameBarangMgr):
    def __init__(self,parent):
        gui.FrameBarangMgr.__init__(self,parent)
<<<<<<< HEAD
        self.showData()
=======
        self.initData()
        self.AddButtonEditDelete()

    def AddButtonEditDelete(self):
        # imgEdit = wx.Bitmap("edit.PNG", wx.BITMAP_TYPE_PNG)
        # imgDelete = wx.Bitmap("delete.PNG", wx.BITMAP_TYPE_PNG)
        jmlKolom = self.tabel_barang.GetNumberCols()
        self.tabel_barang.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1
        # self.rdEdit = renderer.MyImageRenderer(imgEdit)
        # self.rdDelete = renderer.MyImageRenderer(imgDelete)

        self.tabel_barang.SetColLabelValue(colEdit, '')
        self.tabel_barang.SetColLabelValue(colDelete, '')

        for row in range(self.data_barang.GetNumberRows()):
            self.tabel_barang.SetCellValue(row, colEdit, 'Edit')
            self.tabel_barang.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.tabel_barang.SetCellTextColour(row, colEdit, wx.WHITE)

            self.tabel_barang.SetCellValue(row, colDelete, 'Delete')
            self.tabel_barang.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.tabel_barang.SetCellTextColour(row, colDelete, wx.WHITE)
            # self.tabelSiswa.SetCellRenderer(row, colEdit, rdEdit)
            # self.tabelSiswa.SetRowSize(row, imgEdit.GetHeight() + 4)
            # self.tabelSiswa.SetColSize(colEdit, imgEdit.GetWidth() + 4)

            # self.tabelSiswa.SetCellRenderer(row, colDelete, rdEdit)
            # self.tabelSiswa.SetRowSize(row, imgDelete.GetHeight() + 4)
            # self.tabelSiswa.SetColSize(colDelete, imgDelete.GetWidth() + 4)
        self.tabel_barang.Fit()
        self.panelGrid.Layout()

    def initData(self):
        # self.tabelSiswa.DeleteRows(0, 1, True)
        # tmpTabel = self.tabelSiswa
        # self.tabelSiswa.Destroy()

        # self.tabelSiswa = wx.grid.Grid( self.panelGrid, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        # self.tabelSiswa.CreateGrid( 5, 5 )
        n_cols = self.tabel_barang.GetNumberCols()
        n_rows = self.tabel_barang.GetNumberRows()
        if n_cols > 0:
            self.tabel_barang.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_barang.DeleteRows(0, n_rows, True)

        # t2.nama, t2.email, t1.nim, t1.tahun_masuk
        koloms = ['id_barang', 'nama_barang', 'jenis_barang', 'harga_barang', 'stok_barang']
        self.tabel_barang.AppendCols(len(koloms))

        self.brg = Data.Barang()
        daftarBrg = self.brg.getDataBarang(nama_barang)
        baris = 0
        # lstData = []
        self.lstIdPerson = []
        for col in range(len(koloms)):
            self.tabel_barang.SetColLabelValue(
                col, koloms[col])  # mengubah nama kolom
        for brg_row in daftarBrg:
            self.tabel_barang.AppendRows(1)
            # tmp_data_baris = []
            print(baris, '. ', brg_row)
            id_barang, nama_barang, jenis_barang, harga_barang, stok_barang = brg_row
            self.tabel_barang.SetCellValue(baris, 0, id_barang)
            self.tabel_barang.SetCellValue(baris, 1, nama_barang)
            self.tabel_barang.SetCellValue(baris, 2, jenis_barang)
            self.tabel_barang.SetCellValue(baris, 3, harga_barang)
            self.tabel_barang.SetCellValue(baris, 4, stok_barang)
            self.lstIdPerson.append(id)
            baris += 1
>>>>>>> 377f74f8689d5d54785908dac7c21d6dcadfae41

    def btn_back( self, event ):
        FrameMgr.Show()
        FrameBarang1.Hide()
    def btn_tambah(self, event):
<<<<<<< HEAD
        FrameInput.Show()
        FrameBarang1.Hide()
    def showData(self):
        jml_kolom = self.tabel_barang.GetNumberCols()
        jml_baris = self.tabel_barang.GetNumberRows()
        if jml_kolom > 0:
            self.tabel_barang.DeleteCols(0, jml_kolom, True)
        if jml_baris > 0:
            self.tabel_barang.DeleteRows(0, jml_baris, True)

        kolom = ['Id Barang', 'Nama Barang', 'Jenis Barang', 'Harga Barang', 'Stok Barang']
        self.tabel_barang.AppendCols(len(kolom))

        self.manager = Data.Manager()
        mgrlist = self.manager.getDataManager()
        row = 0

        self.listIdmgr = []
        for i in range(len(kolom)):
            self.tabel_barang.SetColLabelValue(
                i, kolom[i]) 
        for x in mgrlist:
            self.tabel_barang.AppendRows(1)

            print(row, '. ', x)
            id_barang, nama_barang, jenis_barang, harga_barang, stok_barang = x
            self.tabel_barang.SetCellValue(row, 0, id_barang)
            self.tabel_barang.SetCellValue(row, 1, nama_barang)
            self.tabel_barang.SetCellValue(row, 2, jenis_barang)
            self.tabel_barang.SetCellValue(row, 3, harga_barang)
            self.tabel_barang.SetCellValue(row, 4, stok_barang)
            self.listIdmgr.append(id_barang)
            row += 1
=======
        frg = gui.FrameInputBarang(self)
        frg.ShowModal()

    def insertDataBrg(self, id_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.brg.setDataBarang(id_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
        self.initData()
        self.AddButtonEditDelete()

    def updateDataBrg(self, id_person, nama, email, nim, tahunMasuk):
        self.brg.updateDataBarang(id_person, nama, email, nim, tahunMasuk)
        self.initData()
        self.AddButtonEditDelete()

        # wx.MessageBox('Tambah data', 'Informasi')
    def tabel_barangOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)
        if kolom == 5:
            # wx.MessageBox('Edit data', 'Informasi')
            id_person = self.lstIdPerson[baris]
            frg = gui.FrameInputBarang(self, id_person)
            id_barang = self.tabel_barang.GetCellValue(baris, 0)
            nama_barang = self.tabel_barang.GetCellValue(baris, 1)
            jenis_barang = self.tabel_barang.GetCellValue(baris, 2)
            harga_barang = self.tabel_barang.GetCellValue(baris, 3)
            stok_barang = self.tabel_barang.GetCellValue(baris, 4)
            frg.isiDataBarang(id_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
            frg.ShowModal()
        elif kolom == 6:
            frg = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = frg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.brg.deleteBarang(self.lstIdPerson[baris])
                self.initData()
                self.AddButtonEditDelete()
>>>>>>> 377f74f8689d5d54785908dac7c21d6dcadfae41

class FrameBarang2 (gui.FrameBarang):
    def __init__(self,parent):
        gui.FrameBarang.__init__(self,parent)
    def btn_back( self, event ):
        FrameKry.Show()
        FrameBarang2.Hide()
        
        
class FrameInput(gui.FrameInputBarang):
    def __init__(self,parent):
        gui.FrameInputBarang.__init__(self,parent)

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

class FrameInputLp(gui.FrameInputLapor):
    def __init__(self,parent):
        gui.FrameInputLapor.__init__(self,parent)

class FrameProfil(gui.FrameProfilKry):
    def __init__(self,parent):
        gui.FrameProfilKry.__init__(self,parent)
    def btn_back( self, event ):
        FrameKry.Show()
        FrameProfil.Hide()


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
FrameWelcome=FrameWelcome(None)
FrameLogin=Login(None)
FrameMgr=FrameMgr(None)
FrameKry=FrameKry(None)
FrameKaryawan=FrameKaryawan(None)
FrameBarang1=FrameBarang1(None)
FrameBarang2=FrameBarang2(None)
FrameInput=FrameInput(None)
FrameInputKr=FrameInputKr(None)
FrameInputLp=FrameInputLp(None)
FrameProfil=FrameProfil(None)

FrameWelcome.Show()
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