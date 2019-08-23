import wx
import FileMenu
import time
import codecs

class MyWindows(FileMenu.MyFrame1):
	p = None
	def NewClick(self,event):
		self.m_textCtrl2.SetValue("")

	def OnopenFile(self,event):
		FileName=wx.FileSelector(
		"NotePad",
		wildcard="文字檔 (*.txt)|*.txt",
		flags=wx.FD_OPEN
		)
		self.p=codecs.open(FileName,"r","utf8")
		self.m_textCtrl2.SetValue(self.p.read())
		self.p.close()

	def OnsaveFile(self,event):
		FileName=wx.FileSelector(
		"NotePad",
		wildcard="文字檔 (*.txt)|*.txt",
		flags=wx.FD_SAVE
		)
		self.p=codecs.open(FileName,"w","utf8")
		self.p.write(self.m_textCtrl2.GetValue())
		self.p.close()

	def CloseClick(self,event):
		exit()		

app=wx.App()
win=MyWindows(None)
win.Show()
app.MainLoop()