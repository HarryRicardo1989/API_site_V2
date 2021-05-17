from request_os import RequestCommands


class ListaSatHora:
    def __init__(self):
        self.__comando = RequestCommands()
        self.hostname = ''
        self.__lista = []
        self.__lista_sat = []

    def sat_hora_list(self):
        try:
            self.hostname = self.__comando.comand('hostname').replace("\n", '')
            self.__lista = self.__comando.comand("ada-list").split('\n')
            for sat in self.__lista[:-2]:
                sat = satsat = sat.split('|')

                self.__lista_sat.append(
                    '{}---{}'.format(sat[1], sat[4][:-3]))
        except:
            pass

        return self.__lista_sat, self.hostname
