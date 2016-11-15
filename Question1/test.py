import solution
import sys

class CheckSolution:
	__inputFilePath = "resources/input.txt"
	__outputFilePath = "resources/output.txt"
	__expectedFilePath = "resources/expected.txt"

	def readInputFromFile(self):
		inputFile = open(self.__inputFilePath, "r")
		inputString = inputFile.read()
		inputFile.close()
		return inputString

	def writeResultToFile(self, string):
		'''Don't modify this function'''
		output = open(self.__outputFilePath, "w")
		output.write(string)
		output.close()

	def compareFile(self):
		outputFile = open(self.__outputFilePath, "r")
		expectedFile = open(self.__expectedFilePath, "r")
		output = outputFile.read()
		expected = expectedFile.read()

		if output.strip() == expected.strip():
			print("Your solution passed test")
		else:
			print("Your solution did not pass test. Please compare {} with {}".format(self.__outputFilePath, self.__expectedFilePath))

		outputFile.close()
		expectedFile.close()

	def checkSolution(self):
		inputString = self.readInputFromFile()
		outputString = solution.countFingerPresses(inputString)
		self.writeResultToFile(outputString)
		self.compareFile()

#test begins
print("test starting...")
test = CheckSolution()
test.checkSolution()
print("test finished.")