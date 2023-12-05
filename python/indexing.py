def multilevel_index(documents, keys):
    # Inicializar el diccionario resultante
    dict_result = {}

    # Iterar sobre cada documento en la lista
    for document in documents:
        # Obtener el valor de la primera llave
        key1 = document[keys[0]]
        # Obtener el valor de la segunda llave
        key2 = document[keys[1]]

        # Si el valor de la primera llave no está en el diccionario resultante, agregarlo
        if key1 not in dict_result:
            dict_result[key1] = {}

        # Si el valor de la segunda llave no está en el diccionario correspondiente, agregarlo
        if key2 not in dict_result[key1]:
            dict_result[key1][key2] = []

        # Agregar el documento al grupo correspondiente en el diccionario resultante
        dict_result[key1][key2].append(document)

    # Retornar el diccionario resultante
    return dict_result


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
