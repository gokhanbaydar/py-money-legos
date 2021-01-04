from .. import util

makerProxyRegistryAbi = util.read_json("./maker/abi/ProxyRegistry.json")
dssCdpManagerAbi = util.read_json("./maker/abi/DssCdpManager.json")
dssProxyActionsAbi = util.read_json("./maker/abi/DssProxyActions.json")

# Reference: https://changelog.makerdao.com/

contracts = {
    "proxyRegistry": {
        "address": "0x4678f0a6958e4D2Bc4F1BAF7Bc52E8F3564f3fE4",
        "abi": makerProxyRegistryAbi,
    },
    "dssCdpManager": {
        "address": "0x5ef30b9986345249bc32d8928B7ee64DE9435E39",
        "abi": dssCdpManagerAbi,
    },
    "dssProxyActions": {
        "address": "0x82ecd135dce65fbc6dbdd0e4237e0af93ffd5038",
        "abi": dssProxyActionsAbi,
    },
    "jug": {
        "address": "0x19c0976f590D67707E62397C87829d896Dc0f1F1",
    },
    "daiJoin": {
        "address": "0x9759A6Ac90977b93B58547b4A71c78317f391A28",
    },
    "batAJoin": {
        "address": "0x3D0B1912B66114d4096F48A8CEe3A56C231772cA",
    },
    "ethAJoin": {
        "address": "0x2F0b23f53734252Bda2277357e97e1517d6B042A",
    },
    "usdcJoin": {
        "address": "0xA191e578a6736167326d05c119CE0c90849E84B7",
    },
}