class TestPlugin(object):
    passed_tests = []

    def pytest_runtest_logreport(self, report):
        if report.outcome == 'passed' and report.when == 'call':
            self.passed_tests.append(report.outcome)