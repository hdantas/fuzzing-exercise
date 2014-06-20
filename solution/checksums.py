from Peach.fixup import Fixup
from fcs import cosem_fcs

class CheckSums(Fixup):

	def __init__(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7="", arg8=""):
		Fixup.__init__(self)
		self.frametype1 = arg1
		self.framelength = arg2
		self.destupper = arg3
		self.destlower = arg4
		self.source = arg5
		self.frametype2 = arg6
		self.headercheckseq = arg7
		self.payload = arg8

	def fixup(self):
		# Locate and get the value of the element we are interested in
		frametype1 = self.context.findDataElementByName(self.frametype1)
		framelength = self.context.findDataElementByName(self.framelength)
		destupper = self.context.findDataElementByName(self.destupper)
		destlower = self.context.findDataElementByName(self.destlower)
		source = self.context.findDataElementByName(self.source)
		frametype2 = self.context.findDataElementByName(self.frametype2)
		headercheckseq = self.context.findDataElementByName(self.headercheckseq)
		payload = self.context.findDataElementByName(self.payload)

		if frametype1 == None or framelength == None or destupper == None or destlower == None or source == None or frametype2 == None :
			raise Exception("Error: FrameCheckSequenceFixup was unable to locate [%s]" % self.ref)

		if headercheckseq == None or payload == None:
			headercheckseq = ""
			payload = ""
		else:
			headercheckseq = headercheckseq.getValue()
			payload = payload.getValue()

		stuff = frametype1.getValue() + framelength.getValue() + destupper.getValue() + destlower.getValue() + source.getValue() + frametype2.getValue() + headercheckseq + payload
		fcs = cosem_fcs(stuff).get_fcs()
		return fcs
