import requests
import unittest

def TestRunner(testcase):
    suite = unittest.TestLoader().loadTestsFromModule(testcase())
    return unittest.TextTestRunner().run(suite)

def RetrievePuzzleData(day):
    r = requests.get("http://adventofcode.com/2017/day/{}/input".format(day))
    return r.text