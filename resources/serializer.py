from model.convites import Convites

def response_serializer(convites: Convites):
    response = []
    for convite in convites:
        convite_dict = {
            "email": convite.email,
            "mensagem": convite.mensagem
        }

        response.append(convite_dict)
    return response