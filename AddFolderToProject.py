import sublime, sublime_plugin
import os


folderList = []

class AddFolder():

   def add(self, dirPath):
      d = self.window.project_data()
      d['folders'].append({'path': dirPath, 'follow_symlinks': True})
      self.window.set_project_data(d)

class AddCustomFolderToProject( sublime_plugin.WindowCommand ):

   def run(self):
      filePath = self.window.active_view().file_name();
      dirName  = os.path.dirname(filePath)
      self.window.show_input_panel("Add Folder:", dirName, AddFolder.add, None, None) # onDone, onChange, onCancel
        
class AddActualFolderToProject( sublime_plugin.WindowCommand ):

   def run(self):
      filePath = self.window.active_view().file_name();
      dirName  = os.path.dirname(filePath)
      if (dirName):
         AddFolder.add(self, dirName)

class ListFolderToAdd( sublime_plugin.WindowCommand ):

   def run(self):
      del folderList[:]
      filePath = self.window.active_view().file_name();
      dirName = os.path.dirname(filePath)
      while (os.path.isdir(dirName) ):
         folderList.append(dirName)
         nPos = dirName.rfind("\\")
         dirName = dirName[:nPos]

      if (folderList == 0):
         return

      folderList.append("-- Add manually a directory --")

      self.window.show_quick_panel(folderList, self.onDone, sublime.MONOSPACE_FONT, 0, None)

   def onDone(self, nIndex):
      if (nIndex == len(folderList)-1):
         AddCustomFolderToProject.run(self)
      elif (nIndex != -1):
         dirPath = folderList[nIndex]
         AddFolder.add(self, dirPath)
      
      del folderList[:]

class CopyFilePath( sublime_plugin.WindowCommand ):

   def run(self):
      filePath = self.window.active_view().file_name();
      sublime.set_clipboard(filePath)

class CopyDirPath( sublime_plugin.WindowCommand ):

   def run(self):
      filePath = self.window.active_view().file_name();
      dirName  = os.path.dirname(filePath)
      if (dirName):
         sublime.set_clipboard(dirName)