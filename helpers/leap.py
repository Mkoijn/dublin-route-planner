from pyleapcard import LeapSession


def get_leap_balance(username, password):
    try:
        session = LeapSession()
        session.try_login(username, password)
        overview = session.get_card_overview()
        leap_balance = overview.balance
        # print(leap_balance)
        return leap_balance
    except IOError:
        return False
