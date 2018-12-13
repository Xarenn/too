def splits():
    print ("\nHEX_DUMP " + "_"*57 + " HEX_DUMP\n")


def n_bytes(chunk, n_byte):
    outp = ""
    lend = 0
    lens = n_byte
    end = 2 if n_byte == 8 else n_byte
    for n in xrange(0, end):
        outp += " ".join("{:02X}".format(ord(c)) for c in chunk[lend:lens])
        outp += " | "
        lens += n_byte
        lend += n_byte
        if(len(chunk)%16 != 0):
            return outp

    return outp



def hex_dump_func(n_file, split_byte):
    offset = 0
    with open(n_file, "rb") as hf:
        while True:
            chunk = hf.read(16)

            if(len(chunk) == 0):
                break

            txt = str(chunk)
            txt = ''.join([i if ord(i) < 128 and ord(i) > 32 else '.' for i in txt])

            outp = "{:#07x}".format(offset)+ ": "
            outp += n_bytes(chunk, split_byte)

            if len(chunk) % 16 != 0:
                outp += ("   "*(16-len(chunk)+1)) + txt

            else:
                outp += "" + txt
            print outp
            offset += 16



def hexdump(file_name, split_byte):
    splits()
    hex_dump_func(file_name, split_byte)
    splits()
