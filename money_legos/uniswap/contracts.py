import util

exchangeAbi = util.read_json("./uniswap/abi/Exchange.json")
factoryAbi = util.read_json("./uniswap/abi/Factory.json")

contracts = {
    "factory": {
        "address": "0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95",
        "abi": factoryAbi,
    },
    "exchange": {
        "abi": exchangeAbi,
    },
}
