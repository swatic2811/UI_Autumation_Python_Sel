import pytest



@pytest.mark.usefixtures("setup","logger_init","test_data")
class BaseTest:

    def getData(self, name):
        valid_data = self.data[name]
        return valid_data
