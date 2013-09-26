#This program is designed to turn ppm files into ASCII art
#   Written by Charles Camp
#   Year 2011

import sys

def main():

   f = open('tux.ppm', 'r+')
   newimg = open('tux1.ppm', 'w')
   asciifile = open('tuxtascii.txt', 'w')
   a = ppm(f, newimg, asciifile)
   a.getvals()
   a.grayscale()
   a.closefiles()


class ppm:
   def __init__(self, img, newimg, asciifile):
      self.asciifile = asciifile
      self.thefile = img
      self.newimg = newimg
      self.width = 0
      self.height = 0
      self.maxcolor = 0
      self.r = 0
      self.g = 0
      self.b = 0
      self.chars = [" ", ".",",",":",";","+","=","o","a","e","0","$","@","A","#", "M"]
      self.graycolor = 0
      self.grays = []
      self.fifty = 0

   def getvals(self):
      v = self.thefile.readline()
      while(v == "#"):
         v = self.thefile.readline()
      if(v == "P3\n" or v == "P3" or "P6" or "P6\n"):
         v == "P3"
      else:
         print "problem"
      self.newimg.write('P3\n')
      w = self._getparams()
      x = self._getmaxcolor()
      


   def grayscale(self):
      count = 0
      br = 0
      self.newimg.write('\n')
      f = self.thefile.read().split()
      for j in range(0, (self.width * self.height) * 3):
         if(count == 0):
            self.r = int(f[j])
            count += 1
            if br < self.width:
               br += 1
            else:
               br = 0
               self.newimg.write('\n')
         elif(count == 1):
            self.g = int(f[j])
            count += 1
            if br < self.width:
               br += 1
            else:
               br = 0
               self.newimg.write('\n')
         elif(count == 2):
            self.b = int(f[j])
            newpix = int((0.3*self.r) + (0.59*self.g) + (0.11*self.b))
            self.graycolor = newpix
            character = self._getchar()
            #print character
            if(self.fifty < self.width):
               self.grays.append(character)
               self.fifty += 1
            else:
               self.asciifile.write(' '.join(self.grays) + '\n')
               self.grays = []
               self.grays.append(character)
               self.fifty = 1
            count = 0
            prntcount = 0
            if br < self.width:
               br += 1
               self.newimg.write(str(newpix) + ' ' + str(newpix) + ' ' + str(newpix) + ' ')
            else:
               br = 0
               self.newimg.write('\n')
               self.newimg.write(str(newpix) + ' ' + str(newpix) + ' ' + str(newpix) + ' ')
               
   #def _printascii(self):
         
      
   def _getparams(self):
      w = ''
      h = ''
      f = self.thefile.readline()
      w = f.split()[0]
      while(w == "#"):
         f = self.thefile.readline()
         w = f.split()[0]
      h = f.split()[1]

      self.newimg.write(w + ' ' + h + '\n')
      self.height = int(h)
      self.width = int(w)


   def _getmaxcolor(self):
      f = self.thefile.readline()
      c = f.split()[0]
      while(c == "#"):
         f = self.thefile.readline()
         c = f.split()[0]
      self.newimg.write(c)
      self.maxcolor = int(c) 
      print self.maxcolor

   def closefiles(self):
      self.newimg.close()
      self.thefile.close()
      self.asciifile.close()

   def _getchar(self):
      #print self.graycolor
      convert = 15
      colorscale = int((self.maxcolor*1) / 15)
      runningnum = 0
      for j in range(len(self.chars)):
         if(self.graycolor >= runningnum and self.graycolor < runningnum + colorscale):
            return self.chars[convert]
            runningnum = 0
            break
         else:
            runningnum += colorscale
            convert = convert - 1


main()
