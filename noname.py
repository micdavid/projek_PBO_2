# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class WelcomeFrame
###########################################################################

class WelcomeFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 641,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Di Toko \"Selalu Makjos\" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 34, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Login Sek Lurr", wx.DefaultPosition, wx.Size( 175,40 ), 0 )
		self.m_button11.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.m_button11OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button11OnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class FrameBarangMgr
###########################################################################

class FrameBarangMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 652,331 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer5.Add( bSizer4, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer5.Add( fgSizer8, 1, wx.EXPAND, 5 )

		self.tabel_barang = wx.grid.Grid( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_barang.CreateGrid( 5, 5 )
		self.tabel_barang.EnableEditing( True )
		self.tabel_barang.EnableGridLines( True )
		self.tabel_barang.EnableDragGridSize( False )
		self.tabel_barang.SetMargins( 0, 0 )

		# Columns
		self.tabel_barang.EnableDragColMove( False )
		self.tabel_barang.EnableDragColSize( True )
		self.tabel_barang.SetColLabelSize( 30 )
		self.tabel_barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_barang.EnableDragRowSize( True )
		self.tabel_barang.SetRowLabelSize( 80 )
		self.tabel_barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.tabel_barang, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button33 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button33, 0, wx.ALL, 5 )

		self.m_button34 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Update Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button34, 0, wx.ALL, 5 )

		self.m_button35 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Hapus Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button35, 0, wx.ALL, 5 )

		self.m_button32 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Cek Laporan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button32, 0, wx.ALL, 5 )


		fgSizer5.Add( bSizer3, 1, wx.EXPAND, 5 )


		sbSizer41.Add( fgSizer5, 1, wx.EXPAND, 5 )


		sbSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button37 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"<< Back ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button37, 0, wx.ALL, 5 )


		sbSizer41.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button33.Bind( wx.EVT_BUTTON, self.btn_tambah )
		self.m_button37.Bind( wx.EVT_BUTTON, self.btn_back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambah( self, event ):
		event.Skip()

	def btn_back( self, event ):
		event.Skip()


###########################################################################
## Class FrameBarang
###########################################################################

class FrameBarang ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 627,252 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer5.Add( bSizer4, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer5.Add( fgSizer8, 1, wx.EXPAND, 5 )

		self.tabel_barang = wx.grid.Grid( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_barang.CreateGrid( 5, 5 )
		self.tabel_barang.EnableEditing( True )
		self.tabel_barang.EnableGridLines( True )
		self.tabel_barang.EnableDragGridSize( False )
		self.tabel_barang.SetMargins( 0, 0 )

		# Columns
		self.tabel_barang.EnableDragColMove( False )
		self.tabel_barang.EnableDragColSize( True )
		self.tabel_barang.SetColLabelSize( 30 )
		self.tabel_barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_barang.EnableDragRowSize( True )
		self.tabel_barang.SetRowLabelSize( 80 )
		self.tabel_barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.tabel_barang, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button21 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Laporkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button21, 0, wx.ALL, 5 )


		fgSizer5.Add( bSizer3, 1, wx.EXPAND, 5 )


		sbSizer41.Add( fgSizer5, 1, wx.EXPAND, 5 )


		sbSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button37 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"<< Back ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button37, 0, wx.ALL, 5 )


		sbSizer41.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FrameInputBrg
###########################################################################

class FrameInputBrg ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input Data Barang", pos = wx.DefaultPosition, size = wx.Size( 372,276 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Id Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer19.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer19.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Jenis Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer19.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Harga Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer19.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Stok Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer19.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_button24, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer19 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button24.Bind( wx.EVT_BUTTON, self.btn_simpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan( self, event ):
		event.Skip()


###########################################################################
## Class FrameInputKry
###########################################################################

class FrameInputKry ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Frame Input Karyawan", pos = wx.DefaultPosition, size = wx.Size( 465,339 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Id Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer20.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer20.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer20.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Nama Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer20.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer20.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_textCtrl191 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl191, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		fgSizer20.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		fgSizer20.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u"No Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )

		fgSizer20.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_button26, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FrameInputLaporan
###########################################################################

class FrameInputLaporan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input Data Laporan", pos = wx.DefaultPosition, size = wx.Size( 379,185 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Id Lapor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		fgSizer21.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_textCtrl25, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Id Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		fgSizer21.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_textCtrl26, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Id Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		fgSizer21.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_textCtrl27, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button29, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FrameKaryawanMgr
###########################################################################

class FrameKaryawanMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 843,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Karyawan" ), wx.VERTICAL )

		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow" ) )

		bSizer8.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer14.Add( bSizer8, 1, wx.EXPAND, 5 )

		fgSizer15 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer14.Add( fgSizer15, 1, wx.EXPAND, 5 )

		self.tabel_karyawan = wx.grid.Grid( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_karyawan.CreateGrid( 3, 8 )
		self.tabel_karyawan.EnableEditing( True )
		self.tabel_karyawan.EnableGridLines( True )
		self.tabel_karyawan.EnableDragGridSize( False )
		self.tabel_karyawan.SetMargins( 0, 0 )

		# Columns
		self.tabel_karyawan.EnableDragColMove( False )
		self.tabel_karyawan.EnableDragColSize( True )
		self.tabel_karyawan.SetColLabelSize( 30 )
		self.tabel_karyawan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_karyawan.EnableDragRowSize( True )
		self.tabel_karyawan.SetRowLabelSize( 80 )
		self.tabel_karyawan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_karyawan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer14.Add( self.tabel_karyawan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button24 = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button25 = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Update Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button25, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Hapus Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button26, 0, wx.ALL, 5 )


		fgSizer14.Add( bSizer9, 1, wx.EXPAND, 5 )


		sbSizer7.Add( fgSizer14, 1, wx.EXPAND, 5 )


		sbSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button27 = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_button27, 0, wx.ALL, 5 )


		sbSizer7.Add( fgSizer16, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FrameLaporMgr
###########################################################################

class FrameLaporMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 352,241 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Cek Laporan" ), wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText32 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Data Lapor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		bSizer12.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer22.Add( bSizer12, 1, wx.EXPAND, 5 )

		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer22.Add( fgSizer23, 1, wx.EXPAND, 5 )

		self.m_grid7 = wx.grid.Grid( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid7.CreateGrid( 1, 3 )
		self.m_grid7.EnableEditing( True )
		self.m_grid7.EnableGridLines( True )
		self.m_grid7.EnableDragGridSize( False )
		self.m_grid7.SetMargins( 0, 0 )

		# Columns
		self.m_grid7.EnableDragColMove( False )
		self.m_grid7.EnableDragColSize( True )
		self.m_grid7.SetColLabelSize( 30 )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 80 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer22.Add( self.m_grid7, 0, wx.ALL, 5 )


		sbSizer8.Add( fgSizer22, 1, wx.EXPAND, 5 )


		sbSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button34 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.m_button34, 0, wx.ALL, 5 )


		sbSizer8.Add( fgSizer24, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FrameProfilKry
###########################################################################

class FrameProfilKry ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 792,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Profil" ), wx.VERTICAL )

		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText25 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Profil Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer10.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer18.Add( bSizer10, 1, wx.EXPAND, 5 )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer18.Add( fgSizer19, 1, wx.EXPAND, 5 )

		self.m_grid4 = wx.grid.Grid( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid4.CreateGrid( 3, 8 )
		self.m_grid4.EnableEditing( True )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )

		# Columns
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelSize( 80 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer18.Add( self.m_grid4, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_button30 = wx.Button( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Update Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button30, 0, wx.ALL, 5 )


		fgSizer18.Add( bSizer11, 1, wx.EXPAND, 5 )


		sbSizer71.Add( fgSizer18, 1, wx.EXPAND, 5 )


		sbSizer71.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button31 = wx.Button( sbSizer71.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_button31, 0, wx.ALL, 5 )


		sbSizer71.Add( fgSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer71 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FrameLogin
###########################################################################

class FrameLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"LOGIN DULU BOSSS!!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )

		bSizer21.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer21.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.input_username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer21.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_pw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.input_pw, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tombol_login = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tombol_login.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer21.Add( self.tombol_login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tombol_login.Bind( wx.EVT_BUTTON, self.btn_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login( self, event ):
		event.Skip()


###########################################################################
## Class FrameMenuMgr
###########################################################################

class FrameMenuMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Menu Pilihan :" ), wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Menu Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		sbSizer31.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_toggleBtn31 = wx.ToggleButton( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Barang >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn31.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer31.Add( self.m_toggleBtn31, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Menu Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		sbSizer31.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_toggleBtn32 = wx.ToggleButton( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Karyawan >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn32.SetValue( True )
		self.m_toggleBtn32.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer31.Add( self.m_toggleBtn32, 0, wx.ALL, 5 )


		sbSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button31 = wx.Button( sbSizer31.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button31.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		sbSizer31.Add( self.m_button31, 0, wx.ALL, 5 )


		self.SetSizer( sbSizer31 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_toggleBtn31.Bind( wx.EVT_TOGGLEBUTTON, self.btn_barang )
		self.m_toggleBtn32.Bind( wx.EVT_TOGGLEBUTTON, self.btn_karyawan )
		self.m_button31.Bind( wx.EVT_BUTTON, self.btn_back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_barang( self, event ):
		event.Skip()

	def btn_karyawan( self, event ):
		event.Skip()

	def btn_back( self, event ):
		event.Skip()


###########################################################################
## Class FrameMenuKry
###########################################################################

class FrameMenuKry ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Menu Pilihan" ), wx.VERTICAL )

		self.m_staticText61 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Menu Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		sbSizer61.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.m_button61 = wx.Button( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Profil >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button61.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer61.Add( self.m_button61, 0, wx.ALL, 5 )

		self.m_staticText62 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Menu Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		sbSizer61.Add( self.m_staticText62, 0, wx.ALL, 5 )

		self.m_button62 = wx.Button( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Barang >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button62.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer61.Add( self.m_button62, 0, wx.ALL, 5 )


		sbSizer61.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button63 = wx.Button( sbSizer61.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button63.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		sbSizer61.Add( self.m_button63, 0, wx.ALL, 5 )


		self.SetSizer( sbSizer61 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button61.Bind( wx.EVT_BUTTON, self.btn_profil )
		self.m_button62.Bind( wx.EVT_BUTTON, self.btn_barang1 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_profil( self, event ):
		event.Skip()

	def btn_barang1( self, event ):
		event.Skip()


