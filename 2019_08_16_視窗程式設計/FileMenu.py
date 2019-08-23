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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"記事本", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,500 ), wx.TE_MULTILINE )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu6 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"New File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Open File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem4 )

		self.m_menubar2.Append( self.m_menu6, u"File" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.NewClick, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.OnopenFile, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.OnsaveFile, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.CloseClick, id = self.m_menuItem4.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def NewClick( self, event ):
		event.Skip()

	def OnopenFile( self, event ):
		event.Skip()

	def OnsaveFile( self, event ):
		event.Skip()

	def CloseClick( self, event ):
		event.Skip()


