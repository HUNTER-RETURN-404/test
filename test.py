# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))