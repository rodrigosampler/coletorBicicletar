# -*- coding: utf-8 -*-
from datetime import datetime

import core
import sys
import csv


import time




if __name__ == "__main__":
    _estacoes = core._busca(sys.argv[1]) if len(sys.argv) > 1 else core._get()
    i=0
    with open("DadosBicicletarUT.csv", "wb") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        print "PROJETO BICICLETAR - FORTALEZA/BR"
        while True:
            for _estacao in _estacoes:
                now = datetime.now()
                data= now.strftime('%Y-%m-%d %H:%M:%S')
                _nome, _lat, _long, _endereco, _linha, _statusOnline, _StatusOperacional, _disp1, _disp2, _total, _internalStatus, _img, _id = _estacao
                spamwriter.writerow([data, _id, _nome.encode('utf8'), _lat, _long, _linha.encode('utf8'), _endereco.encode('utf8'), _statusOnline, _StatusOperacional, _internalStatus, _disp1, _disp2, _total])
                #print 'estacao id %d:' % _id, _nome, '-', _linha, '-', _endereco, ' / bikes disponiveis: %d, vagas livres: %d' % (int(_disp2),int(_total))
                #i+=1
            #print 'foram mostradas %d estacoes' % i
            time.sleep(60)
