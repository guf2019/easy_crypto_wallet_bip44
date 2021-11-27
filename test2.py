import binascii
from bip_utils import Bip44Changes, Bip44Coins, Bip44Levels, Bip44, Bip39MnemonicGenerator, Bip39Languages, \
    Bip39WordsNum, Bip39SeedGenerator

# Seed bytes
mnemonic = Bip39MnemonicGenerator(Bip39Languages.ENGLISH).FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
print("mnemonic phrase = " + mnemonic.ToStr())
seed_bytes = Bip39SeedGenerator(mnemonic).Generate("536775")
# Create from seed
bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.TRON)

print("-----seed-----")
# Print master key in extended format
print("extented private key: " + bip44_mst_ctx.PrivateKey().ToExtended())
# Print master key in hex format
print("hex private key: " + bip44_mst_ctx.PrivateKey().Raw().ToHex())

# Print public key in extended format
print("extented public key: " + bip44_mst_ctx.PublicKey().ToExtended())
# Print public key in raw uncompressed format
print("uncompressed hex public key: " + bip44_mst_ctx.PublicKey().RawUncompressed().ToHex())
# Print public key in raw compressed format
print("compressed hex public key: " + bip44_mst_ctx.PublicKey().RawCompressed().ToHex())

# Print the master key in WIF
print("\n\n\n-----wif-----")
print(bip44_mst_ctx.IsLevel(Bip44Levels.MASTER))
print(bip44_mst_ctx.PrivateKey().ToWif())

print("\n\n\n-----Derive account 0 for Bitcoin: m/44'/0'/0'-----")
# Derive account 0 for Bitcoin: m/44'/0'/0'
bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)
# Print keys in extended format
print(bip44_acc_ctx.IsLevel(Bip44Levels.ACCOUNT))
print("extended private key: " + bip44_acc_ctx.PrivateKey().ToExtended())
print("extended public key: " + bip44_acc_ctx.PublicKey().ToExtended())
# Address of account level
print("address: " + bip44_acc_ctx.PublicKey().ToAddress())


print("\n\n\n-----Derive the external chain: m/44'/0'/0'/0-----")
# Derive the external chain: m/44'/0'/0'/0
bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)
# Print again keys in extended format
print(bip44_chg_ctx.IsLevel(Bip44Levels.CHANGE))
print("extended private key: " + bip44_chg_ctx.PrivateKey().ToExtended())
print("extended public key: " + bip44_chg_ctx.PublicKey().ToExtended())
# Address of change level
print("address: " + bip44_chg_ctx.PublicKey().ToAddress())


print("\n\n\n-----Derive the first 20 addresses of the external chain: m/44'/0'/0'/0/i-----")
# Derive the first 5 addresses of the external chain: m/44'/0'/0'/0/i
for i in range(5):
    print('{' + str(i + 1) + '}')
    bip44_addr_ctx = bip44_chg_ctx.AddressIndex(i)

    print(bip44_addr_ctx.IsLevel(Bip44Levels.ADDRESS_INDEX))
    # Print extended keys and address
    print("extended private key: " + bip44_addr_ctx.PrivateKey().ToExtended())
    print("extended public key: " + bip44_addr_ctx.PublicKey().ToExtended())
    print("address: " + bip44_addr_ctx.PublicKey().ToAddress())
