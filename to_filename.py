import unicodedata
import string

valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

def clean_filename(filename, whitelist=valid_filename_chars, replace=' '):
    # replace spaces
    for r in replace:
        filename = filename.replace(r,'_')

    # keep only valid ascii chars
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()

    # keep only whitelisted chars
    return ''.join(c for c in cleaned_filename if c in whitelist)

# test
s='fake_folder/\[]}{}|~`"\':;,/? abcABC 0123 !@#$%^&*()_+ clᐖﯫⅺຶ 讀ϯՋ㉘ ⅮRㇻᎠ⍩ 𝁱C ℿ؛ἂeuឃC ᅕ ᑉﺜͧ bⓝ s⡽Հᛕ\ue063 牢𐐥er ᐛŴ n წş .ھڱ!zip'
clean_filename(s) # 'fake_folder_abcABC_0123_____clxi_28_DR_C_euC___bn_s_er_W_n_s_.zip'
