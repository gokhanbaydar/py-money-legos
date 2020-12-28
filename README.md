# py-money-legos

`money-legos` is an NPM package that provides you with the **mainnet addresses**, **ABIs**, and **Solidity interfaces** for popular DeFi protocols.

`py-money-legos` is its Python version

## Install
```bash
pip install py-money-legos
```

## Usage

Please check the main javascript repo for more on how to use: https://github.com/studydefi/money-legos

Docs of javascript version: https://money-legos.studydefi.com/
Discord for javascript version: https://discord.gg/rBr3U32

test.py includes a sample to get MKR price from UNISWAP using the Web3, you will need to pip install web3 for this to work, it is commented to remove dependency with this library.

## Sample Import
```bash
from money_legos.uniswap.contracts import contracts
factory_abi = contracts["factory"]["abi"]
exch_abi = contracts["exchange"]["abi"]
```

## Help

Feel free to contribute or contact me for any help or comments
