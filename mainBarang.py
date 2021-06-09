import wx
import noname as gui
import Data
from wx.core import MessageBox


class dlgAddBarang(gui.FrameInputBrg):
    def __init__(self, parent, id=-1):
        gui.FrameInputBrg.__init__(self, parent)
        self.parent=parent
        self.id = id

    def btn_simpan( self, event ):
        dlg= wx.MessageDialog(self, 'simpan data', 'Informasi', style=wx.YES_NO)
        retval= dlg.ShowModal()

        if self.id == -1:
            self.parent.insertDataBrg(self.input_no.GetValue(), self.input_nama.GetValue(
            ), self.input_jenis.GetValue(), self.input_harga.GetValue(), self.input_stok.GetValue())
        else:
            self.parent.updateDataBrg(self.id, self.input_no.GetValue(), self.input_nama.GetValue(
            ), self.input_jenis.GetValue(), self.input_harga.GetValue(), self.input_stok.GetValue())
        self.Destroy()

    def fillDataBarang(self, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.input_no.SetValue(no_barang)
        self.input_nama.SetValue(nama_barang)
        self.input_jenis.SetValue(jenis_barang)
        self.input_harga.SetValue(harga_barang)
        self.input_stok.SetValue(stok_barang)

class FrameBarang1 (gui.FrameBarangMgr):
    def __init__(self,parent):
        gui.FrameBarangMgr.__init__(self,parent)
        self.showDataBarang()
        self.AddBtnBarang()

    def showDataBarang(self):
        n_cols = self.tabel_barang.GetNumberCols()
        n_rows = self.tabel_barang.GetNumberRows()
        if n_cols > 0:
            self.tabel_barang.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_barang.DeleteRows(0, n_rows, True)

        kolom = ['No Barang', 'Nama Barang', 'Jenis Barang', 'Harga Barang', 'Stok Barang']
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

    # def btn_back( self, event ):
    #     FrameMgr.Show()
    #     FrameBarang1.Hide()

    def btn_tambah( self, event ):
        dlg = dlgAddBarang(self)
        dlg.ShowModal()

    def insertDataBrg(self, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.barang.addDataBarang(no_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
        self.showDataBarang()
        self.AddBtnBarang()
    
    def updateDataBrg(self, id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.barang.updateDataBarang(id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
        self.showDataBarang()
        self.AddBtnBarang()

    def AddBtnBarang (self):
        jmlKolom = self.tabel_barang.GetNumberCols()
        self.tabel_barang.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.tabel_barang.SetColLabelValue(colEdit, '')
        self.tabel_barang.SetColLabelValue(colDelete, '')

        for row in range(self.tabel_barang.GetNumberRows()):
            self.tabel_barang.SetCellValue(row, colEdit, 'Edit')
            self.tabel_barang.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.tabel_barang.SetCellTextColour(row, colEdit, wx.WHITE)

            self.tabel_barang.SetCellValue(row, colDelete, 'Delete')
            self.tabel_barang.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.tabel_barang.SetCellTextColour(row, colDelete, wx.WHITE)

        self.tabel_barang.Fit()

    def tabel_barangOnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()
        if kolom == 5:
            id = self.listIdBarang[baris]
            dlg = dlgAddBarang(self, id)
            no = self.tabel_barang.GetCellValue(baris, 0)
            nama = self.tabel_barang.GetCellValue(baris, 1)
            jenis = self.tabel_barang.GetCellValue(baris, 2)
            harga = self.tabel_barang.GetCellValue(baris, 3)
            stk = self.tabel_barang.GetCellValue(baris, 4)
            dlg.fillDataBarang(no, nama, jenis, harga, stk)
            dlg.ShowModal()
        elif kolom == 6:
            dlg = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.barang.deleteDataBarang(self.listIdBarang[baris])
                self.showDataBarang()
                self.AddBtnKaryawan()