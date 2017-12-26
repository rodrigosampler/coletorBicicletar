# -*- coding: utf-8 -*-
from datetime import datetime

import core
import sys
import csv
import os


import time




if __name__ == "__main__":
    while True:
        _estacoes = core._busca(sys.argv[1]) if len(sys.argv) > 1 else core._get()

        for _estacao in _estacoes:
            now = datetime.now()
            data= now.strftime('%Y-%m-%d %H:%M:%S')
            minha_data = data[:10]
            _nome, _lat, _long, _endereco, _linha, _statusOnline, _StatusOperacional, _disp1, _disp2, _total, _internalStatus, _img, _id = _estacao

            nome_arquivo = minha_data+'/ESTACAO_'+str(_id)+'.csv'
            if not os.path.exists(minha_data):
                os.makedirs(minha_data)

            with open(nome_arquivo, "a") as csvfile:
                try:
                    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([data, _id, _nome.encode('utf8'), _lat, _long, _linha.encode('utf8'), _endereco.encode('utf8'), _statusOnline, _StatusOperacional, _internalStatus, _disp1, _disp2, _total])
                finally:
                    csvfile.close()
        print("proximo")
        time.sleep(60)
