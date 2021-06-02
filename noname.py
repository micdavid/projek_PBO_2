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

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Di Toko \"Selalu Makjos\" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 34, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer1.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Login Sek Lurr", wx.DefaultPosition, wx.Size( 175,40 ), 0 )
		self.m_button18.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer1.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
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

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"LOGIN DULU BOSSS!!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer2.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer2.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
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

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Menu Pilihan :" ), wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Menu Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		sbSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Barang >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn1.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer1.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Menu Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		sbSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_toggleBtn2 = wx.ToggleButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Karyawan >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn2.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer1.Add( self.m_toggleBtn2, 0, wx.ALL, 5 )


		sbSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button7 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		sbSizer1.Add( self.m_button7, 0, wx.ALL, 5 )


		self.SetSizer( sbSizer1 )
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

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		sbSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_radioBtn1 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Lihat Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tambah Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Ubah Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

		self.m_radioBtn31 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Hapus Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_radioBtn31, 0, wx.ALL, 5 )

		self.m_radioBtn32 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Lihat Laporan Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_radioBtn32, 0, wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button3 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer1.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer1.Add( self.m_button4, 0, wx.ALL, 5 )


		sbSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer2 )
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

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Karyawan" ), wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		sbSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_radioBtn4 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Lihat Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

		self.m_radioBtn5 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Tambah Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

		self.m_radioBtn6 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Ubah Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Hapus Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer2.Add( self.m_button6, 0, wx.ALL, 5 )


		sbSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer3 )
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

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Menu Pilihan" ), wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Menu Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		sbSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Profil >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		sbSizer5.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Menu Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		sbSizer5.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Barang >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		sbSizer5.Add( self.m_button10, 0, wx.ALL, 5 )


		sbSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button11 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button11.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		sbSizer5.Add( self.m_button11, 0, wx.ALL, 5 )


		self.SetSizer( sbSizer5 )
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

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Profil" ), wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		sbSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_radioBtn4 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Lihat Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

		self.m_radioBtn5 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Ubah Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

		self.m_radioBtn6 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Menu Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer2.Add( self.m_button6, 0, wx.ALL, 5 )


		sbSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer3 )
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
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Silahkan Pilih Daftar Menu Berikut :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		sbSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_radioBtn4 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Lihat Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

		self.m_radioBtn5 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cek Stok Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

		self.m_radioBtn6 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Laporan Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"OK >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		fgSizer2.Add( self.m_button6, 0, wx.ALL, 5 )


		sbSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


