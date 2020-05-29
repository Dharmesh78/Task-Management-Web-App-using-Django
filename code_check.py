from datetime import datetime
def checkDate(pDate):
    s=datetime.today().strftime('%Y-%m-%d')
    if pDate>=s:
        return True
    return False

checkDate()
