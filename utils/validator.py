import re
from PyQt6.QtGui import QValidator


class ValidateTimer(QValidator):
    def validate(self, str , index):
        pattern = re.compile("^(?:[1-9]?[0-9]|1[01][0-9]|120)$")
        
        if str == "":
            return QValidator.State.Acceptable, str, index
        
        if pattern.fullmatch(str):
            return QValidator.State.Acceptable, str, index
        else:
            return QValidator.State.Invalid, str, index

class ValidatePauseTimer(QValidator):
    def validate(self, str , index):
        pattern = re.compile("^(?:[0-5]?[0-9]|60)$")
        
        if str == "":
            return QValidator.State.Acceptable, str, index
        
        if pattern.fullmatch(str):
            return QValidator.State.Acceptable, str, index
        else:
            return QValidator.State.Invalid, str, index