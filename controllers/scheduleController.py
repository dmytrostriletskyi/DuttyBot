class scheduleController():
	def __init__(self, data):
		self.data = data.split(' ')

	def compactData(self):
		for i in range(4, len(self.data), 7):
			if len(self.data[i]) == 3:
				self.data[i] += ' '

		self.lesson = self.data[0] + ' ' + self.data[1]
		self.subject = self.data[2]
		self.cabinet = self.data[3] + ' ' + self.data[4]
		self.teacher = self.data[5] + ' ' + self.data[6]

		return '{0} | {1}  | {2} — {3}'.format(self.lesson, self.cabinet, self.subject, self.teacher)



