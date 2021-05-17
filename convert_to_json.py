from ada_status import AdaStatus
from lista_sat_hora import ListaSatHora
import json


class JsonAda:
    def __init__(self):
        self.__lista_passagens = ListaSatHora()
        self.__status_ada = AdaStatus()
        self.__dict_sat_list2 = {}
        self.__dict_status_ada2 = {}
        self.__dict_sat_list = {}
        self.__dict_status_ada = {}
        self.__dict_status_sistema = {}

    def json_passagens(self):
        lista_passagens, hostname = self.__lista_passagens.sat_hora_list()
        for sat in lista_passagens:
            sat = sat.split('---')
            self.__dict_sat_list2.update({sat[1].strip(): sat[0].strip()})
        return json.dumps({f'Passagens {hostname}': self.__dict_sat_list2}, sort_keys=False, indent=2)

    def json_status(self):
        hostname, posicao_ada, ssd_usado, temperatura_processador, hora, armazenamento, cpu_load = self.__status_ada.get_status_ada()
        #self.__dict_status_ada2.update({'Nome_ADA': hostname})
        self.__dict_status_ada2.update({'Temp_CPU': temperatura_processador})
        self.__dict_status_ada2.update({'SSD_used': ssd_usado})
        self.__dict_status_ada2.update({'Posicao_Atual': posicao_ada})
        self.__dict_status_ada2.update({'Hora_Atual': hora})

        return json.dumps({f'Status {hostname}': self.__dict_status_ada2}, sort_keys=False, indent=2)

    def json_completo(self):
        lista_passagens, hostname = self.__lista_passagens.sat_hora_list()
        for sat in lista_passagens:
            sat = sat.split('---')
            self.__dict_sat_list.update({sat[1].strip(): sat[0].strip()})
        hostname, posicao_ada, ssd_usado, temperatura_processador, hora, armazenamento, cpu_load = self.__status_ada.get_status_ada()

        self.__dict_status_ada.update(
            {'Temp_CPU': temperatura_processador})
        self.__dict_status_ada.update({'Posicao_Atual': posicao_ada})
        self.__dict_status_ada.update({'Hora_Atual': hora})
        self.__dict_status_ada.update({'CPU_Load': round(cpu_load, 3)})
        __dict_discos = {}
        for item in armazenamento:
            item.split(' ')
            __dict_discos.update(
                {item.split()[0]: f'{item.split()[1]} de {item.split()[2]}'})
        self.__dict_status_ada.update({'Discos': __dict_discos})
        self.__dict_status_sistema.update({'Passagens': self.__dict_sat_list})
        self.__dict_status_sistema.update({'Status': self.__dict_status_ada})

        return json.dumps({f'{hostname}': self.__dict_status_sistema}, sort_keys=False, indent=2)
