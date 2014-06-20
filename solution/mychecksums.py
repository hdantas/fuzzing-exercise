from Peach.fixup import Fixup
import hashlib

class CheckSums(Fixup):

	def __init__(self, arg1, arg2):
		Fixup.__init__(self)
		self.text = arg1
		self.timestamp = arg2

	def fixup(self):
		# Locate and get the value of the element we are interested in
		text = self.context.findDataElementByName(self.text)
		timestamp = self.context.findDataElementByName(self.timestamp)
		shasum = hashlib.sha1(text.getValue() + timestamp.getValue()).hexdigest()

		return shasum
