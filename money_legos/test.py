# from money_legos.uniswap.contracts import contracts
# from web3 import Web3, HTTPProvider

# _TOKENS = {
#     "ETH": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
#     "MKR": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
#     "DAI": "0x6b175474e89094c44da98b954eedeac495271d0f",
#     "KNC": "0xdd974d5c2e2928dea5f71b9825b8b646686bd200",
#     "LINK": "0x514910771af9ca656af840dff83e8264ecf986ca",
# }
# web3 = Web3(
#     HTTPProvider("https://mainnet.infura.io/v3/{YOUR INFURA PROJECT ID}")
# )
# inputTokenSymbol = "ETH"
# inputTokenAddress = Web3.toChecksumAddress(_TOKENS[inputTokenSymbol])
# outputTokenSymbol = "DAI"
# outputTokenAddress = Web3.toChecksumAddress(_TOKENS[outputTokenSymbol])
# inputAmount = Web3.toWei("1", "ETHER")
# factory_abi = contracts["factory"]["abi"]
# factory_adr = Web3.toChecksumAddress(contracts["factory"]["address"])
# factory_ctr = web3.eth.contract(abi=factory_abi, address=factory_adr)
# exch_abi = contracts["exchange"]["abi"]
# exch_adr = factory_ctr.caller.getExchange(outputTokenAddress)
# exch_ctr = web3.eth.contract(abi=exch_abi, address=exch_adr)
# exch_rate = exch_ctr.caller.getEthToTokenInputPrice(inputAmount)
# exch_rate_eth = Web3.fromWei(exch_rate, "Ether")
# print(
#     inputAmount,
#     exch_rate,
#     f"1 {inputTokenSymbol} = {exch_rate_eth} {outputTokenSymbol}",
# )
