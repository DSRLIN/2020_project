class ConfigError(Exception):
    def __init__(self, error_info):
        self.errorInfo = error_info

    def __str__(self):
        return self.errorInfo
