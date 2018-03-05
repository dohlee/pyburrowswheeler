class BWT:

	def __init__(self, string):
		assert '\002' not in string and '\003' not in string, "STX and ETX characters should not be included in input string."
		self.string = '\002' + string + '\003'
		self.bwt = self._burrows_wheeler_transform(string)

	def _burrows_wheeler_transform(self, string):
		pass