import unittest
import helper
import verification
import main

# Class to test the command line input.
class UnitTestHelper(unittest.TestCase):

    def testCompanyExist(self):
        """Unit Test to check if companyExist method works"""

        # Edge Case : file name does not end in csv
        dummyData = "dummyData.c"
        self.assertFalse(dummyData[-3:] == ".v")

        # Check if file name ends in csv
        dummyData = "dummyData.csv"
        self.assertEqual(dummyData[-3:], "csv")
        
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.companyExist('REDDY GI ASSOCIATES', dummyData))
        self.assertFalse(verification.companyExist('NO SUCH COMPANY', dummyData))

    def integrationColumnExist(self):
        """Integration Test for ColumnExist"""
        dummyData = "dummyData.csv"
        data = helper.readFile(dummyData)
        command = "--state"
        target = "CA"
        visaData = data[0]
        
        pass

    def testColumnExist(self):
        """Unit Test to check if columnExistt method works"""

        # Get dummyData and testVisaData for the test
        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        testVisaData = readFileResult[0]
        
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.columnExist("company", testVisaData))
        self.assertTrue(verification.columnExist("City", testVisaData))
        self.assertTrue(verification.columnExist("NAICS", testVisaData))
        self.assertFalse(verification.columnExist("None", testVisaData))

    def testContainsNum(self):
        """Unit Test to check if containsNumber method works"""

        # Edge case : arg is not string
        testArgList = [193]
        self.assertFalse(verification.commandLen(testArgList))
        testArgInt = 12345678
        self.assertFalse(verification.commandLen(testArgInt))

        # Check if arg is a string
        # Normally, command line changes into argument in main.py. It saves the command line as a list, starting after "python3".
        testStr = "2"
        self.assertTrue(type(testStr) == str)

        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.containsNum(testStr))
        self.assertTrue(verification.containsNum("19"))
        self.assertFalse(verification.containsNum("1 9"))
        self.assertFalse(verification.containsNum("Yes"))
        self.assertFalse(verification.containsNum("he11o"))
    
    def testcommandLen(self):
        """Unit Test to check if commandLen method works"""
        # Edge case : arg is not list
        testArgStr = "python3 main.py dummyData.csv --company PULMONICS PLUS PLLC"
        self.assertFalse(verification.commandLen(testArgStr))
        testArgInt = 12345678
        self.assertFalse(verification.commandLen(testArgInt))

        # Check if arg is a list
        # Normally, command line changes into argument in main.py. It saves the command line as a list, starting after "python3".
        testArg = ["main.py", "dummyData.csv", "--company", "PULMONICS PLUS PLLC"]
        self.assertTrue(type(testArg) == list)

        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.commandLen(testArg))
        self.assertTrue(verification.commandLen(["main.py", "dummyData.csv", "--state", "CA"]))
        self.assertTrue(verification.commandLen(["main.py", "dummyData.csv", "--minInitApproval", "2"]))
        self.assertFalse(verification.commandLen(["main.py", "dummyData.csv"]))
        self.assertFalse(verification.commandLen(["main.py", "dummyData.csv", "--minInitApproval"]))
    
    def testInputValid(self):
        """Unit Test to check if inputValid method works"""

        # No need to check for empty commands because we check the command line len before 
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.inputValid("PULMONICS PLUS PLLC", "--company"))
        self.assertTrue(verification.inputValid("CA", "--state"))
        self.assertTrue(verification.inputValid("2", "--minInitApproval"))
        self.assertFalse(verification.inputValid("None", "--minInitApproval"))

    


if __name__ == '__main__':
    unittest.main()

