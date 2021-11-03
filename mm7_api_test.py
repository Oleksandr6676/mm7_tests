import requests
import hashlib
import json
from locators import Error_Codes as Errors
from locators import Api_data_mm7 as Api


def generate_auth_token():

    #Generating authorization token via testpartner
    global token
    payload_token = {'gameURL': Api.gameURL, 'frontURL': Api.frontURL, 'partnerURL': Api.partnerURL,
                        "partnerID": Api.partnerID, "gameID": Api.gameID, "userID": Api.userID,
                        'currency': Api.currency}
    test_partner_request = requests.get("https://testpartnerservice.carhenge.space/setup/",
                                            params=payload_token).text
    token = test_partner_request.split("token=")[1].split("&")[0]


def authorization():
    #Authorize user
    hash_AuthorizationGame = hashlib.md5(("AuthorizationGame/" + token + Api.gameKey).encode()).hexdigest()
    payload_authorization = json.dumps({"Hash": hash_AuthorizationGame, "Token": token, "MobilePlatform": False})
    Authorization_response = requests.post(Api.main_URL + Api.AuthorizationGame_Url,
                                            data=payload_authorization).json()
    print(Authorization_response)
    balance = int(Authorization_response["Balance"])


def get_slot_info():
    git 


def base_game_flow(max_spin_count):
    spin_count = 0
    while spin_count < max_spin_count:

        #Sending CreditDebit request
        hash_CreditDebit = hashlib.md5(
            ("CreditDebit/" + token + Api.betSum + Api.cntLineBet + Api.gameKey).encode()).hexdigest()
        payload_CreditDebit = json.dumps(
            {"Token": token, "CntLineBet": Api.cntLineBet, "BetSum": Api.betSum, "Hash": hash_CreditDebit})
        creditDebit_response = requests.post(Api.main_URL + Api.CreditDebit_Url,
                                                data=payload_CreditDebit).json()
        token_async = creditDebit_response["TokenAsync"]

        #Sending GetAsyncResponse for CreditDebit
        hash_GetAsyncResponse = hashlib.md5(
            ("GetAsyncResponse/" + token + token_async + Api.gameKey).encode()).hexdigest()
        payload_GetAsyncResponse = json.dumps(
            {"Token": token, "TokenAsync": token_async, "Hash": hash_GetAsyncResponse})
        GetAsyncResponse = requests.post(Api.main_URL + Api.GetAsyncResponse_Url,
                                            data=payload_GetAsyncResponse).json()

        while "Error" in GetAsyncResponse: # If error 13 ---> send request again, if any other error - exit script and show error message
            if GetAsyncResponse['Error'] == 13:
                GetAsyncResponse = requests.post(Api.main_URL + Api.GetAsyncResponse_Url,
                                                     data=payload_GetAsyncResponse).json()
            else:
                for key in Errors.error_codes_dictionary:
                    if GetAsyncResponse['Error'] == key:
                        print(f"Script ended with error: {Errors.error_codes_dictionary[key]}")
                        exit()

        freespins_count = GetAsyncResponse["GameFreeSpins"][0]["RemainingFreeSpinsCount"]
        result_id = GetAsyncResponse["ResultId"]
        spin_id = GetAsyncResponse['SpinResult']['Id']
        spin_count+=1
        print(f"Spin Result: {spin_id} \nResult ID: {result_id} \nBalance: {GetAsyncResponse['WinInfo']['Balance']} \n"
              f"Current Spin Win: {GetAsyncResponse['WinInfo']['CurrentSpinWin']} \nTotal freespins count: {freespins_count}")
        print("======================== << End of the round >> ===========================")

        if freespins_count > 0:
            print("===================== << Starting Freespins >> ========================")

            for i in range(freespins_count):

                #Sending freespin requests
                hash_freespin = hashlib.md5(
                    ("FreeSpin/" + token + result_id + spin_id + Api.gameKey).encode()).hexdigest()
                payload_freespin = json.dumps(
                    {"Hash": hash_freespin, "Token": token, "ResultId": result_id, "SpinId": spin_id})
                freespin_response = requests.post(Api.main_URL + Api.FreeSpin_Url,
                                                data=payload_freespin).json()
                token_async_freespin = freespin_response["TokenAsync"]
                print(token_async_freespin)

                #Sending GetAsyncResponse request for freespins
                hash_GetAsyncResponse_freespin = hashlib.md5(
                     ("GetAsyncResponse/" + token + token_async_freespin + Api.gameKey).encode()).hexdigest()
                payload_GetAsyncResponse_freespin = json.dumps(
                     {"Hash": hash_GetAsyncResponse_freespin, "Token": token, "TokenAsync": token_async_freespin})
                GetAsyncResponse_freespin = requests.post(Api.main_URL + Api.GetAsyncResponse_Url,
                                                data=payload_GetAsyncResponse_freespin).json()

                while "Error" in GetAsyncResponse_freespin:  # If error 13 ---> send request again, if any other error - exit script and show error message
                    if GetAsyncResponse_freespin['Error'] == 13:
                        GetAsyncResponse_freespin = requests.post(Api.main_URL + Api.GetAsyncResponse_Url,
                                                data=payload_GetAsyncResponse_freespin).json()
                    else:
                        for key in Errors.error_codes_dictionary:
                            if GetAsyncResponse_freespin['Error'] == key:
                                print(f"Script ended with error: {Errors.error_codes_dictionary[key]}")
                                exit()

                result_id = GetAsyncResponse_freespin["ResultId"]
                spin_id = GetAsyncResponse_freespin['SpinResult']['Id']
                freespins_count = GetAsyncResponse_freespin["GameFreeSpins"][0]["RemainingFreeSpinsCount"]
                print(f"Spin Result: {spin_id} \nResult ID: {result_id} \nBalance: {GetAsyncResponse_freespin['WinInfo']['Balance']}"
                      f"\nTotal freespins count: {freespins_count} \nTotal freespins win: {GetAsyncResponse_freespin['WinInfo']['TotalWin']}")
                print("===================== << End of the freespin >> =====================")



session_count = 0
while session_count < 3:
    generate_auth_token()
    authorization()
    base_game_flow(250)
    session_count += 1
