import wx
import noname as gui
import Data
from wx.core import MessageBox


class dlgAddKaryawan(gui.FrameInputKry):
    def __init__(self, parent, id=-1):
        gui.FrameInputKry.__init__(self, parent)
        self.parent=parent
        self.id = id

    def btn_simpan( self, event ):
        dlg= wx.MessageDialog(self, 'simpan data', 'Informasi', style=wx.YES_NO)
        retval= dlg.ShowModal()

        if self.id == -1:
            self.parent.insertDataKry(self.input_user.GetValue(), self.input_pass.GetValue(),
            self.input_nama.GetValue(), self.input_gender.GetValue(), self.input_ttl.GetValue(),
            self.input_alamat.GetValue(), self.input_telp.GetValue())
        else:
            self.parent.updateDataKry(self.id, self.input_user.GetValue(), self.input_pass.GetValue(),
            self.input_nama.GetValue(), self.input_gender.GetValue(), self.input_ttl.GetValue(),
            self.input_alamat.GetValue(), self.input_telp.GetValue())
        self.Destroy()

    def fillDataKaryawan (self, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
        self.input_user.SetValue(username)
        self.input_pass.SetValue(password)
        self.input_nama.SetValue(nama_karyawan)
        self.input_gender.SetValue(jenis_kelamin)
        self.input_ttl.SetValue(tanggal_lahir)
        self.input_alamat.SetValue(alamat)
        self.input_telp.SetValue(no_telepon)

class FrameKaryawan(gui.FrameKaryawanMgr):
    def __init__(self,parent):
        gui.FrameKaryawanMgr.__init__(self,parent)
        self.showDataKaryawan()
        self.AddBtnKaryawan()

    def showDataKaryawan(self):
        n_cols = self.tabel_karyawan.GetNumberCols()
        n_rows = self.tabel_karyawan.GetNumberRows()
        if n_cols > 0:
            self.tabel_karyawan.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_karyawan.DeleteRows(0, n_rows, True)

        kolom = ['Username', 'Password', 'Nama', 'Gender', 'Tanggal Lahir', 'Alamat', 'No Telepon']
        self.tabel_karyawan.AppendCols(len(kolom))

        self.kry = Data.Karyawan()
        listKry = self.kry.getDataKaryawan()
        row = 0

        self.listIdKry = []
        for col in range(len(kolom)):
            self.tabel_karyawan.SetColLabelValue(col, kolom[col]) 
        for row_kry in listKry:
            self.tabel_karyawan.AppendRows(1)
            print(row, '. ', row_kry)
            id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon = row_kry
            self.tabel_karyawan.SetCellValue(row, 0, username)
            self.tabel_karyawan.SetCellValue(row, 1, password)
            self.tabel_karyawan.SetCellValue(row, 2, nama_karyawan)
            self.tabel_karyawan.SetCellValue(row, 3, jenis_kelamin)
            self.tabel_karyawan.SetCellValue(row, 4, tanggal_lahir)
            self.tabel_karyawan.SetCellValue(row, 5, alamat)
            self.tabel_karyawan.SetCellValue(row, 6, no_telepon)
            self.listIdKry.append(id)
            row += 1

    # def btn_back( self, event ):
    #     FrameMgr.Show()
    #     FrameBarang1.Hide()

    def btn_tambah( self, event ):
        dlg = dlgAddKaryawan(self)
        dlg.ShowModal()

    def insertDataKry(self, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
        self.kry.addDataKaryawan(username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon)
        self.showDataKaryawan()
        self.AddBtnKaryawan()
    
    def updateDataKry(self, id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
        self.kry.updateDataKaryawan(id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon)
        self.showDataKaryawan()
        self.AddBtnKaryawan()

    def AddBtnKaryawan (self):
        jmlKolom = self.tabel_karyawan.GetNumberCols()
        self.tabel_karyawan.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.tabel_karyawan.SetColLabelValue(colEdit, '')
        self.tabel_karyawan.SetColLabelValue(colDelete, '')

        for row in range(self.tabel_karyawan.GetNumberRows()):
            self.tabel_karyawan.SetCellValue(row, colEdit, 'Edit')
            self.tabel_karyawan.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.tabel_karyawan.SetCellTextColour(row, colEdit, wx.WHITE)

            self.tabel_karyawan.SetCellValue(row, colDelete, 'Delete')
            self.tabel_karyawan.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.tabel_karyawan.SetCellTextColour(row, colDelete, wx.WHITE)

        self.tabel_karyawan.Fit()

    def tabel_karyawanOnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()
        if kolom == 7:
            id = self.listIdKry[baris]
            dlg = dlgAddKaryawan(self, id)
            un = self.tabel_karyawan.GetCellValue(baris, 0)
            pasw = self.tabel_karyawan.GetCellValue(baris, 1)
            nama = self.tabel_karyawan.GetCellValue(baris, 2)
            gender = self.tabel_karyawan.GetCellValue(baris, 3)
            ttl = self.tabel_karyawan.GetCellValue(baris, 4)
            alamat = self.tabel_karyawan.GetCellValue(baris, 5)
            telp = self.tabel_karyawan.GetCellValue(baris, 6)
            dlg.fillDataKaryawan(un, pasw, nama, gender, ttl, alamat, telp)
            dlg.ShowModal()
        elif kolom == 8:
            dlg = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.kry.deleteDataKaryawan(self.listIdKry[baris])
                self.showDataKaryawan()
                self.AddBtnKaryawan()