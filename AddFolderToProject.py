import sublime, sublime_plugin
import os

folderList = []

class AddFolder():

   def add(self, dirPath):
      d = self.window.project_data()

      # if no project present
      if not d: 
         d = {'folders': [{'follow_symlinks': True, 'path': dirPath}] }
         self.window.set_project_data(d)
         return 

      d['folders'].append({'path': dirPath, 'follow_symlinks': True})
      self.window.set_project_data(d)         

   def exists(self, dirPath):
      d = self.window.project_data()

      if d :
         for folder in d['folders']:
            if (folder['path']):
               if os.path.samefile( dirPath, folder['path']):
                  return True

      return False

   def remove(self, dirPath):
      d = self.window.project_data()

      nI = 0
      for folder in d['folders']:
         if (folder['path']):
            if os.path.samefile( dirPath, folder['path']):
               del (d['folders'][nI])
               self.window.set_project_data(d)
               return True
            nI = nI + 1;

class AddCustomFolderToProject( sublime_plugin.WindowCommand ):

   def run(self):
      filePath = self.window.active_view().file_name();

      if (not filePath):
         dirName = ""
      else:
         dirName  = os.path.dirname(filePath)

      global mySelf
      mySelf = self
      self.window.show_input_panel("Add Folder:", dirName, AddCustomFolderToProject.on_done, None, None) # onDone, onChange, onCancel

   def on_done(result):
      AddFolder.add(mySelf, result)

        
# Command "Add This Folder To Project"
class AddActualFolderToProject( sublime_plugin.WindowCommand ):

   def run(self):
      filePath = self.window.active_view().file_name();
      dirName  = os.path.dirname(filePath)
      if (dirName):
         global mySelf
         mySelf = self
         AddFolder.add(self, dirName)

   def is_visible(self):
      filePath = self.window.active_view().file_name();

      # if path exists AND doesn't exists in the project already, visibile
      if (filePath and not AddFolder.exists(self, os.path.dirname(filePath) ) ):
         return True
      else:
         return False

class RemoveActualFolderFromProject( sublime_plugin.WindowCommand ):

   def run(self):
      filePath = self.window.active_view().file_name();
      dirName  = os.path.dirname(filePath)
      if (dirName):
         AddFolder.remove(self, dirName)

   def is_visible(self):
      filePath = self.window.active_view().file_name();

      # if path exists AND doesn't exists in the project already, visibile
      if (filePath and AddFolder.exists(self, os.path.dirname(filePath) ) ):
         return True
      else:
         return False

class ListFolderToAdd( sublime_plugin.WindowCommand ):

   def run(self):
      del folderList[:]
      filePath = self.window.active_view().file_name();

      # if path dowesn't exist, asks for a custom folder
      if (not filePath):
         AddCustomFolderToProject.run(self)
         return

      dirName = os.path.dirname(filePath)
      while (os.path.isdir(dirName) ):
         folderList.append(dirName)
         nPos = dirName.rfind("\\")
         dirName = dirName[:nPos]

      if (folderList == 0):
         return

      for el in folderList:
         if AddFolder.exists(self, el):
            folderList.remove(el)

      if (folderList == 0):
         return

      folderList.append("-- Add manually a directory --")

      self.window.show_quick_panel(folderList, self.onDone, sublime.MONOSPACE_FONT, 0, None)

   def onDone(self, nIndex):
      if (nIndex == len(folderList)-1):
         AddCustomFolderToProject.run(self)
      elif (nIndex != -1):
         dirPath = folderList[nIndex]
         global mySelf
         mySelf = self
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


class CreateProjectFromFile(sublime_plugin.WindowCommand):
   
   def run(self, paths = []):
      import subprocess
      items = []

      executable_path = sublime.executable_path()

      if sublime.platform() == 'osx':
         app_path = executable_path[:executable_path.rfind(".app/")+5]
         executable_path = app_path+"Contents/SharedSupport/bin/subl"

      items.append(executable_path)

      filePath = self.window.active_view().file_name();
      dirName  = os.path.dirname(filePath)

      items.append(dirName)
      items.append(filePath)

      p = subprocess.Popen(items)