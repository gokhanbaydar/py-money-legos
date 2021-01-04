from .. import util

curveAbi = util.util.read_json("./curvefi/abi/Curve.json")
poolTokenAbi = util.util.read_json("./curvefi/abi/PoolToken.json")
zapAbi = util.util.read_json("./curvefi/abi/Zap.json")

# Reference: https://github.com/curvefi/curve-contract/

contracts = {
    "poolTokenAbi": poolTokenAbi,
    "curveAbi": curveAbi,
    "zapAbi": zapAbi,
    "cDai_cUsdc": {
        "nCoins": 2,
        "indexes": {
            "dai": 0,
            "usdc": 1,
        },
        "zap": {
            "address": "0xeB21209ae4C2c9FF2a86ACA31E123764A3B6Bc06",
        },
        "curve": {
            "address": "0xa2b47e3d5c44877cca798226b7b8118f9bfb7a56",
        },
        "poolToken": {
            "address": "0x845838df265dcd2c412a1dc9e959c7d08537f8a2",
        },
    },
    "cDai_cUsdc_Usdt": {
        "nCoins": 3,
        "indexes": {
            "dai": 0,
            "usdc": 1,
            "usdt": 2,
        },
        "zap": {
            "address": "0xac795D2c97e60DF6a99ff1c814727302fD747a80",
        },
        "curve": {
            "address": "0x52ea46506b9cc5ef470c5bf89f17dc28bb35d85c",
        },
        "poolToken": {
            "address": "0x9fc689ccada600b6df723d9e47d84d76664a1f23",
        },
    },
    "yDai_yUsdc_yUsdt_ytUsd": {
        "nCoins": 4,
        "indexes": {
            "dai": 0,
            "usdc": 1,
            "usdt": 2,
            "tusd": 3,
        },
        "zap": {
            "address": "0xbBC81d23Ea2c3ec7e56D39296F0cbB648873a5d3",
        },
        "curve": {
            "address": "0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51",
        },
        "poolToken": {
            "address": "0xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8",
        },
    },
}
