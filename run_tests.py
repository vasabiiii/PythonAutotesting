
import sys
import tests
import unittest


test_files =[
    tests.AuthTests,
    tests.MainPageTests
]

def run_tests(test_files):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for test_file in test_files:
        try:
            test = loader.loadTestsFromName(test_file)
            suite.addTests(test)
        except Exception as e:
            print(f"Не удалось загрузить {test_file}: {e}")

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    run_tests(test_files)