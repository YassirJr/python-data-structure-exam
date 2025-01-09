from utils import Employes , Salaires , Services

def list_to_dict():
    return {f"Emp" + str(Employes.index(item["nom"]) + 1): item for item in
            (map(lambda x, y, z: {"nom": x, "salaire": y, "service": z}, Employes, Salaires, Services))}
