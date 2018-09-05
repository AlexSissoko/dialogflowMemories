import dialogflow as df
from entity_type_manager import get_entity_type

def check_entity_type(project_id, type_name):
    entity_type = get_entity_type(project_id, type_name)
    if entity_type == None: 
        raise ValueError("EntityType '{}' doesn't exist!".format(type_name))
    else: return entity_type

def get_entities(project_id, type_name):
    try:
        entity_type = check_entity_type(project_id, type_name)
        return entity_type.entities
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return None

def list_entities(project_id, type_name):
    entities = get_entities(project_id, type_name)
    for entity in entities:
        print('Entity value: {}'.format(entity.value))
        print('Entity synonyms: {}\n'.format(entity.synonyms))

def get_entity(project_id, type_name, value):
    try:
        for entity in get_entities(project_id, type_name):
            if entity.value == value : return entity
        return None
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return None

def create_entity(value, synonyms):
    return df.types.EntityType.Entity(value=value, synonyms=synonyms)

def add_entity(project_id, type_name, entity):
    try:
        entity_type = check_entity_type(project_id, type_name)
        client = df.EntityTypesClient()
        response = client.batch_create_entities(entity_type.name, [entity])
        print('Entity created: {}'.format(response))
        return response
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return None

def add_entities(project_id, type_name, entities):
    try: 
        entity_type = check_entity_type(project_id, type_name)
        client = df.EntityTypesClient()
        response = client.batch_create_entities(entity_type.name, entities)
        print('Entities created: {}'.format(response))
        return response
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return None

def update_entities(project_id, type_name, entities):
    try:
        entity_type = check_entity_type(project_id, type_name)
        client = df.EntityTypesClient()
        response = client.batch_update_entities(entity_type.name, entities)
        print('Entity created: {}'.format(response))
        return response
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return None

def delete_entity(project_id, type_name, entity_value):
    try:
        entity_type = check_entity_type(project_id, type_name)
        client = df.EntityTypesClient()
        response = client.batch_delete_entities(entity_type.name, [entity_value])
        print('Entity deleted: {}'.format(entity_value))
        return response
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return None

def delete_entities(project_id, type_name, entity_values):
    try: 
        entity_type = check_entity_type(project_id, type_name)
        client = df.EntityTypesClient()
        response = client.batch_delete_entities(entity_type.name, entity_values)
        print('Entities deleted: {}'.format(entity_values))
        return response
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return None

def get_entity_synonyms(project_id, type_name, entity_value):
    entity = get_entity(project_id, type_name, entity_value)
    if entity == None: return []
    else: return entity.synonyms
