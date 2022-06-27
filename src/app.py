from web3 import Web3, HTTPProvider
from ca import *
import json
from time import sleep
import random 
from SendEmail import *

owneremail='parvathanenimadhu@gmail.com'

def connect_with_blockchain(acc):
    web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
    if(acc==0):
        web3.eth.defaultAccount = web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=acc
    compiled_contract_path='../build/contracts/insurance.json'
    deployed_contract_address=insuranceContractAddress

    with open(compiled_contract_path) as file:
        contract_json=json.load(file)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=deployed_contract_address,abi=contract_abi)
    return contract, web3

count=0
while True:
    contract,web3=connect_with_blockchain(0)
    bp,pulse,bodytemp,glucose=contract.functions.viewFeed().call()
    l=len(bp)
    if l>count:
        for i in range(count,l):
            if(bp[i]<60 or bp[i]>140) or (pulse<40) or (bodytemp>107) or (glucose>8):
                verifyIdentity(owneremail)
                amount=random.randint(199999,2999999)

                while True:
                    try:
                        a=sendmessage('Insurance is Needed as the vitals showing emergency',bp[i],pulse[i],bodytemp[i],glucose[i],amount,owneremail)
                        if(a):
                            break
                        else:
                            continue
                    except:
                        sleep(10)

            payload='{"BP":'+str(bp[i])+',"Pulse":'+str(pulse[i])+',"Body Temp": '+str(bodytemp)+', "Glucose": '+str(glucose)+'}'
            print(payload)
            sleep(4)
        else:
            count=l