import util

addressWhitelistAbi = util.read_json("./uma/abi/AddressWhitelist.json")
designatedVotingFactoryAbi = util.read_json("./uma/abi/DesignatedVotingFactory.json")
expiringMultiPartyAbi = util.read_json("./uma/abi/ExpiringMultiParty.json")
expiringMultiPartyCreatorAbi = util.read_json(
    "./uma/abi/ExpiringMultiPartyCreator.json"
)
financialContractsAdminAbi = util.read_json("./uma/abi/FinancialContractsAdmin.json")
finderAbi = util.read_json("./uma/abi/Finder.json")
governorAbi = util.read_json("./uma/abi/Governor.json")
identifierWhitelistAbi = util.read_json("./uma/abi/IdentifierWhitelist.json")
registryAbi = util.read_json("./uma/abi/Registry.json")
storeAbi = util.read_json("./uma/abi/Store.json")
tokenFactoryAbi = util.read_json("./uma/abi/TokenFactory.json")
votingAbi = util.read_json("./uma/abi/Voting.json")
votingTokenAbi = util.read_json("./uma/abi/VotingToken.json")
weth9Abi = util.read_json("./uma/abi/WETH9.json")

contracts = {
    "addressWhitelist": {
        "abi": addressWhitelistAbi,
        "address": "0xdBF90434dF0B98219f87d112F37d74B1D90758c7",
    },
    "designatedVotingFactory": {
        "abi": designatedVotingFactoryAbi,
        "address": "0xE81EeE5Da165fA6863bBc82dF66E62d18625d592",
    },
    "expiringMultiParty": {
        "abi": expiringMultiPartyAbi,
    },
    "expiringMultiPartyLib": {
        "abi": [],
        "address": "0xCb08678e4381Be3E264E6A0037E3297Ca56a583e",
    },
    "expiringMultiPartyCreator": {
        "abi": expiringMultiPartyCreatorAbi,
        "address": "0xad8fD1f418FB860A383c9D4647880af7f043Ef39",
    },
    "financialContractsAdmin": {
        "abi": financialContractsAdminAbi,
        "address": "0x4E6CCB1dA3C7844887F9A5aF4e8450d9fd90317A",
    },
    "finder": {
        "abi": finderAbi,
        "address": "0x40f941E48A552bF496B154Af6bf55725f18D77c3",
    },
    "governor": {
        "abi": governorAbi,
        "address": "0x592349F7DeDB2b75f9d4F194d4b7C16D82E507Dc",
    },
    "identifierWhitelist": {
        "abi": identifierWhitelistAbi,
        "address": "0xcF649d9Da4D1362C4DAEa67573430Bd6f945e570",
    },
    "registry": {
        "abi": registryAbi,
        "address": "0x3e532e6222afe9Bcf02DCB87216802c75D5113aE",
    },
    "store": {
        "abi": storeAbi,
        "address": "0x54f44eA3D2e7aA0ac089c4d8F7C93C27844057BF",
    },
    "tokenFactory": {
        "abi": tokenFactoryAbi,
        "address": "0x7c96d6235CfaaCcAc5d80fCe74E6032B25dd1F03",
    },
    "voting": {
        "abi": votingAbi,
        "address": "0x9921810C710E7c3f7A7C6831e30929f19537a545",
    },
    "votingToken": {
        "abi": votingTokenAbi,
        "address": "0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828",
    },
    "weth9": {
        "abi": weth9Abi,
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    },
}