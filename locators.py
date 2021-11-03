class Error_Codes:
    error_codes = [10, 11, 13, 49, 50, 51, 64, 100, 101, 102, 105, 108, 109, 110, 113, 114, 115, 116, 150, 151, 152,
                   200, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214]
    error_codes_messages = ['HashMismatch', 'RoundNotFound', 'AsyncResponseNotFound', 'GambleInfoNotFound',
                            'GambleCalculationError', 'InternalServiceError', 'MySQLRequestFailed', 'MongoSaveError',
                            'CachePartnerNotFound', 'RequestToPartnerFailed', 'PartnerError', 'WrongParamError',
                            'MongoUserSessionNotFound', 'MySQLRoundCreationError', 'PartnerBlocked', 'UserBlocked',
                            'CacheGameNotFound', 'InsufficientFunds', 'DemoUserNotFound', 'DemoUserCreateError',
                            'DemoUserUpdateError', 'GameBlocked', 'SpinslotInvalidMethod', 'GameEnded',
                            'UnavailableAction', 'JackpotError', 'GameNotFound', 'WrongBetSum',
                            'WrongLogic', 'NoAvailableFreeSpins', 'UserNotFound', 'TokenError']
    error_codes_dictionary = dict(zip(error_codes, error_codes_messages))

class Api_data_mm7:
    gameURL = 'https://test-games-api.carhenge.space/'
    frontURL = 'https://stest.zhdun.space/'
    partnerURL = 'https://test-partners-api.carhenge.space/'
    main_URL = "https://test-mm7n-api.carhenge.space/"

    AuthorizationGame_Url = '/auth/AuthorizationGame'
    GetSlotInfo_Url = '/games/GetSlotInfo'
    CreditDebit_Url = '/games/CreditDebit'
    GetAsyncResponse_Url = '/games/GetAsyncResponse'
    FreeSpin_Url = '/games/FreeSpin'
    Get_history_URL = "/games/GetHistory"

    partnerID = '360'
    gameID = '20001'
    userID = '532'
    currency = 'USD'
    gameKey = 'TestKey'
    betSum = '1'
    cntLineBet = '20'
    limit = "1"
    offset = "0"