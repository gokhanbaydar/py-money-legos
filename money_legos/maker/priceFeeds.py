from .. import util

medianizerAbi = util.read_json("./maker/abi/Medianizer.json")

priceFeeds = {
    "ethUsdPriceFeed": {
        "address": "0x729d19f657bd0614b4985cf1d82531c67569197b",
        "abi": medianizerAbi,
    }
}