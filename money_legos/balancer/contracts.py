import util

BActions = util.read_json("./balancer/abi/BActions.json")
ExchangeProxy = util.read_json("./balancer/abi/ExchangeProxy.json")
BFactory = util.read_json("./balancer/abi/BFactory.json")
BPool = util.read_json("./balancer/abi/BPool.json")

contracts = {
    "PoolFactory": {
        "abi": BFactory,
        "address": "0x9424B1412450D0f8Fc2255FAf6046b98213B76Bd",
    },
    "BActions": {
        "abi": BActions,
        "address": "0xde4A25A0b9589689945d842c5ba0CF4f0D4eB3ac",
    },
    "ExchangeProxy": {
        "abi": ExchangeProxy,
        "address": "0x6317C5e82A06E1d8bf200d21F4510Ac2c038AC81",
    },
    "BPool": {
        "abi": BPool,
    },
}
