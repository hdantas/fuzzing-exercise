from Peach.publisher import Publisher
import hashlib

class FileWriter(Publisher):
	'''
	Publishes generated data to a file.  No concept of receaving data
	yet.
	'''
	
	def __init__(self, filename):
		'''
		@type	filename: string
		@param	filename: Filename to write to
		'''
		Publisher.__init__(self)
		self._filename = None
		self._fd = None
		self._state = 0	# 0 -stoped; 1 -started
		self.setFilename(filename)
	
	def getFilename(self):
		'''
		Get current filename.
		
		@rtype: string
		@return: current filename
		'''
		return self._filename
	def setFilename(self, filename):
		'''
		Set new filename.
		
		@type filename: string
		@param filename: Filename to set
		'''
		self._filename = filename
	
	def start(self):
		pass
	
	def connect(self):
		if self._state == 1:
			raise Exception('File::start(): Already started!')
		
		if self._fd != None:
			self._fd.close()
		
		self.mkdir()
		
		self._fd = open(self._filename, "a")
		self._state = 1
	
	def stop(self):
		self.close()
	
	def mkdir(self):
		# lets try and create the folder this file lives in
		delim = ""
		
		if self._filename.find("\\") != -1:
			delim = '\\'
		elif self._filename.find("/") != -1:
			delim = '/'
		else:
			return
		
		# strip filename
		try:
			path = self._filename[: self._filename.rfind(delim) ]
			os.mkdir(path)
		except:
			pass
		
	def close(self):
		if self._state == 0:
			return
		
		self._fd.close()
		self._fd = None
		self._state = 0
	
	def send(self, data):
		if type(data) != str:
			data = data.encode('iso-8859-1')
		self._fd.write(data)
	
	def receive(self, size = None):
		if size != None:
			return self._fd.read(size)
		
		return self._fd.read()