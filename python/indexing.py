def multilevel_index(documents, keys):
    # Inicializar el diccionario resultante
    result_dict = {}

    # Iterar sobre cada documento en la lista
    for document in documents:
        # Obtener el valor de la primera llave
        key1 = document[keys[0]]
        # Obtener el valor de la segunda llave
        key2 = document[keys[1]]

        # Si el valor de la primera llave no está en el diccionario resultante, agregarlo
        if key1 not in result_dict:
            result_dict[key1] = {}

        # Si el valor de la segunda llave no está en el diccionario correspondiente, agregarlo
        if key2 not in result_dict[key1]:
            result_dict[key1][key2] = []

        # Agregar el documento al grupo correspondiente en el diccionario resultante
        result_dict[key1][key2].append(document)

    # Retornar el diccionario resultante
    return result_dict


# Ejemplo de uso con la lista de objetos y las llaves proporcionadas
objects = [
    {
        "age": 12,
        "name": "Mateo",
        "last_name": "González",
    },
    {
        "age": 25,
        "name": "Arturo",
        "last_name": "González",
    },
    {
        "age": 12,
        "name": "Julián",
        "last_name": "Fernández",
    },
]

result = multilevel_index(objects, ["age", "last_name"])
print(result)
