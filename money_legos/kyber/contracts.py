from .. import util

networkProxyAbi = util.read_json("./kyber/abi/KyberNetworkProxy.json")

contracts = {
    "network": {
        "address": "0x818E6FECD516Ecc3849DAf6845e3EC868087B755",
        "abi": networkProxyAbi,
    },
}
