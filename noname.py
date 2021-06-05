# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"LOGIN DULU BOSSS!!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )

		bSizer21.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer21.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_textCtrl21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer21.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_textCtrl22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer21.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

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
		self.m_toggleBtn32.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer31.Add( self.m_toggleBtn32, 0, wx.ALL, 5 )


		sbSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button31 = wx.Button( sbSizer31.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button31.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		sbSizer31.Add( self.m_button31, 0, wx.ALL, 5 )


		self.SetSizer( sbSizer31 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		self.m_staticText41 = wx.StaticText( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		sbSizer41.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_radioBtn41 = wx.RadioButton( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Lihat Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_radioBtn41, 0, wx.ALL, 5 )

		self.m_radioBtn42 = wx.RadioButton( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Tambah Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_radioBtn42, 0, wx.ALL, 5 )

		self.m_radioBtn43 = wx.RadioButton( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Ubah Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_radioBtn43, 0, wx.ALL, 5 )

		self.m_radioBtn44 = wx.RadioButton( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Hapus Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_radioBtn44, 0, wx.ALL, 5 )

		self.m_radioBtn45 = wx.RadioButton( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Lihat Laporan Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_radioBtn45, 0, wx.ALL, 5 )

		fgSizer41 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button41 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button41.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer41.Add( self.m_button41, 0, wx.ALL, 5 )

		self.m_button42 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button42.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer41.Add( self.m_button42, 0, wx.ALL, 5 )


		sbSizer41.Add( fgSizer41, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Karyawan" ), wx.VERTICAL )

		self.m_staticText51 = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		sbSizer51.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_radioBtn51 = wx.RadioButton( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Lihat Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.m_radioBtn51, 0, wx.ALL, 5 )

		self.m_radioBtn52 = wx.RadioButton( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Tambah Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.m_radioBtn52, 0, wx.ALL, 5 )

		self.m_radioBtn53 = wx.RadioButton( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Ubah Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.m_radioBtn53, 0, wx.ALL, 5 )

		self.m_radioBtn54 = wx.RadioButton( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Hapus Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.m_radioBtn54, 0, wx.ALL, 5 )

		fgSizer51 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button51 = wx.Button( sbSizer51.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button51.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer51.Add( self.m_button51, 0, wx.ALL, 5 )

		self.m_button52 = wx.Button( sbSizer51.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button52.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer51.Add( self.m_button52, 0, wx.ALL, 5 )


		sbSizer51.Add( fgSizer51, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer51 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Menu Pilihan" ), wx.VERTICAL )

		self.m_staticText61 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Menu Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		sbSizer61.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.m_button61 = wx.Button( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Profil >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button61.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		sbSizer61.Add( self.m_button61, 0, wx.ALL, 5 )

		self.m_staticText62 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Menu Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		sbSizer61.Add( self.m_staticText62, 0, wx.ALL, 5 )

		self.m_button62 = wx.Button( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Barang >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button62.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		sbSizer61.Add( self.m_button62, 0, wx.ALL, 5 )


		sbSizer61.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button63 = wx.Button( sbSizer61.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button63.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		sbSizer61.Add( self.m_button63, 0, wx.ALL, 5 )


		self.SetSizer( sbSizer61 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame7
###########################################################################

class MyFrame7 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Profil" ), wx.VERTICAL )

		self.m_staticText71 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		sbSizer71.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_radioBtn71 = wx.RadioButton( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Lihat Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer71.Add( self.m_radioBtn71, 0, wx.ALL, 5 )

		self.m_radioBtn72 = wx.RadioButton( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Ubah Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer71.Add( self.m_radioBtn72, 0, wx.ALL, 5 )

		fgSizer71 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button71 = wx.Button( sbSizer71.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button71.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer71.Add( self.m_button71, 0, wx.ALL, 5 )

		self.m_button72 = wx.Button( sbSizer71.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button72.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer71.Add( self.m_button72, 0, wx.ALL, 5 )


		sbSizer71.Add( fgSizer71, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer71 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame8
###########################################################################

class MyFrame8 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		self.m_staticText81 = wx.StaticText( sbSizer81.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		sbSizer81.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_radioBtn81 = wx.RadioButton( sbSizer81.GetStaticBox(), wx.ID_ANY, u"Lihat Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer81.Add( self.m_radioBtn81, 0, wx.ALL, 5 )

		self.m_radioBtn82 = wx.RadioButton( sbSizer81.GetStaticBox(), wx.ID_ANY, u"Cek Stok Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer81.Add( self.m_radioBtn82, 0, wx.ALL, 5 )

		self.m_radioBtn83 = wx.RadioButton( sbSizer81.GetStaticBox(), wx.ID_ANY, u"Laporan Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer81.Add( self.m_radioBtn83, 0, wx.ALL, 5 )

		fgSizer81 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button81 = wx.Button( sbSizer81.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button81.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer81.Add( self.m_button81, 0, wx.ALL, 5 )

		self.m_button82 = wx.Button( sbSizer81.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button82.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer81.Add( self.m_button82, 0, wx.ALL, 5 )


		sbSizer81.Add( fgSizer81, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer81 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


