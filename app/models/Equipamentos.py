class Equipamento:
    def __init__(self, id, nome, status):
        self.id = id
        self.nome = nome
        self.status = status

    def mudar_status(self, novo_status):
        self.status = novo_status
