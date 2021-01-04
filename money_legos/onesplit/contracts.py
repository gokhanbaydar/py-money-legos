from .. import util

oneSplitAbi = util.read_json("./onesplit/abi/OneSplit.json")

contracts = {
    "address": "0xC586BeF4a0992C495Cf22e1aeEE4E446CECDee0E",  # Alternatively 1split.eth
    "abi": oneSplitAbi,
}
