from bip_utils import Bip39MnemonicGenerator, Bip39Languages, Bip39WordsNum, Bip39SeedGenerator, Bip44, Bip44Coins

def generate_mnemonic_phrase():
    mnemonic = Bip39MnemonicGenerator(Bip39Languages.ENGLISH).FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
    return mnemonic.ToList()