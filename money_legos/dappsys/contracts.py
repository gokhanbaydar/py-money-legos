from .. import util

dsProxyAbi = util.util.read_json("./dappsys/abi/DSProxy.json")
dsProxyFactoryAbi = util.util.read_json("./dappsys/abi/DSProxyFactory.json")

contracts = {
    "dsProxy": {
        "abi": dsProxyAbi,
    },
    "dsProxyFactory": {
        "abi": dsProxyFactoryAbi,
    },
}
