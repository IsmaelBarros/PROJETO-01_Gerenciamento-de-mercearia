class FullName:
    sobrenome = 'barros'

    @classmethod
    def do_some(cls):
        cls.nome = 'ismael'
        nome_completo = cls.nome + cls.sobrenome
        print(nome_completo)


teste = FullName()
teste.do_some()


class FullName1:
    sobrenome = 'barros'

    def do_some(self):
        self.nome = 'ismael'

        nome_completo = self.nome + self.sobrenome
        print(nome_completo)


# teste = FullName1()
# teste.do_some()
