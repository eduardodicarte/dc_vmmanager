"""
Exibe a tela de ajuda no sistema
"""


class MainHelp(object):

    def __init__(self):
        self.printhelp()

    def printhelp(self):
        self.print_info_author()
        self.print_info_install()
        self.print_gerar_ambientes()
        self.print_obtendo_informacoes()
        self.print_destruir_vms()

    def print_info_author(self):
        print("\nPrograma desenvolvido por Eduardo Dicarte\nContato: eduardo_dicarte@yahoo.com.br\n")
        print("==" * 67)

    def print_info_install(self):
        print("\nInstalação")
        print("\tDescrição")
        print("\t\tFaz a instalação da infraestrutura necessária para a utilização do Vagrant")
        print("\tComandos")
        print("\t\tinstallenvironment => Faz a instalação de um ambiente default contendo o vagrant e o virtual box, também faz um init ")
        print("\t\tinstallvagrant => Faz a instalação do vagrant, ignorando caso já esteja instalado. ")
        print("\t\tuninstallvagrant => Faz a desinstalação do vagrant sem excluir quaisquer arquivos de configuração")
        print("\t\tpurgevagrant => Faz a desinstalação do vagrant e exclui todos os arquivos de configuração")
        print("\t\tuninstallvirtualbox => Faz a desinstalação do virtualbox")

    def print_gerar_ambientes(self):
        print("\nGerando novos ambientes")
        print("\tDescrição")
        print("\t\tFaz a geração de novos ambientes, gerando as pastas necessárias e um Vagrantfile com configuração default")
        print("\tComandos")
        print("\t\tinit => Gera um novo ambiente com VagrantFile padrão")
        print("\t\tinitall => Faz um init para todos os usuários encontrador no sistema")
        print("\t\tinituser [users] => Faz um init para todos os usuários passados via parâmetro, os usuários devem estar separados por virgula")

    def print_obtendo_informacoes(self):
        print("\nObtendo informações")
        print("\tDescrição")
        print("\t\tExibe a tela de ajuda para a obtenção de informações das vms em execução e que estão desligadas. ")
        print("\t\tCaso não seja passado o usuário ou o nome da vm serão apresentadas informações para todos os usuários, ")
        print("\t\to sistema irá percorrer todos os arquivos de configuração de usuários e exibirá as informações encontradas.")
        print("\tComandos")
        print("\t\tshowvmsuser => Mostra as vms que estão em execução para o usuário corrente")
        print("\t\tshowvms => Mostra as vms que estão em execução para todos os usuários")

    def print_destruir_vms(self):
        print("\nDestruindo vms (Atenção: Todos os dados serão excluídos e não poderão ser recuperados")
        print("\tdropvmsuser => Destrói todas as vms do usuário corrente")
        print("\tdropvms => Destrói todas as vms existentes no sistema operacional")


if __name__ == "__main__":
    MainHelp()