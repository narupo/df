#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Df:

    def __init__(self):
        self.root_use_percent = None

    def exec(self):
        import subprocess

        output = subprocess.check_output(['df', '-h'])
        output = output.decode('utf-8')
        lines = output.split('\n')

        for l in lines:
            toks = l.split(' ')
            toks = self.merge_toks(toks)
            if self.is_root_toks(toks):
                self.root_use_percent = self.get_per_from_toks(toks)
                break

    def get_per_from_toks(self, toks):
        return int(toks[-2].replace('%', ''))

    def is_root_toks(self, toks):
        return len(toks) >= 6 and toks[-1] == '/'

    def merge_toks(self, toks):
        dst = []
        for t in toks:
            if len(t) == 0:
                continue
            dst.append(t)
        return dst

if __name__ == '__main__':
    df = Df()
    df.exec()
    print(df.root_use_percent)
