import dialogflow as df 
from google.api_core import exceptions

def get_entity_types(project_id):
    try: 
        client = df.EntityTypesClient()
        project_path = client.project_agent_path(project_id)
        return client.list_entity_types(project_path)
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connection to peer: {}'.format(e))

def list_entity_types(project_id):
    entity_types = get_entity_types(project_id)

    for entity_type in entity_types:
        print('Entity type name: {}'.format(entity_type.name))
        print('Entity type display name: {}'.format(entity_type.display_name))
        print('Number of entities: {}\n'.format(len(entity_type.entities)))

def get_entity_type(project_id, type_name):
    try:
        for entity_type in get_entity_types(project_id):
            if type_name == entity_type.display_name: return entity_type
        return None
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connection to peer: {}'.format(e))

def get_entity_type_path(project_id, type_name):
    entity_type = get_entity_type(project_id, type_name)
    if entity_type == None: 
        raise ValueError("EntityType '{}' does not exist!".format(type_name))
    return entity_type.name

def get_entity_type_id(project_id, type_name):
    entity_type_path = get_entity_type_path(project_id, type_name)
    return entity_type_path.split('/')[-1]

def create_entity_type(project_id, type_name, kind, entities=[]):
    try:
        client = df.EntityTypesClient()
        parent = client.project_agent_path(project_id)
        entity_type = df.types.EntityType(
                display_name=type_name, kind=kind, entities=entities)

        response = client.create_entity_type(parent, entity_type)
        print('Entity type created: \n{}'.format(response))
        return response
    except exceptions.FailedPrecondition as e:
        print('Invalid EntityType name: {}'.format(e))
        return None
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer: {}'.format(e))
        return None

def delete_entity_type(project_id, type_name):
    try: 
        client = df.EntityTypesClient()

        #Not particularly efficient, but good for abstraction
        path = get_entity_type_path(project_id, type_name) 
        #Returns None, even on success
        client.delete_entity_type(path)
        print('Entity Type deleted: {}'.format(type_name))
        return True
    except ValueError as e:
        print('We encountered a problem: {}'.format(e))
        return False
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer: {}'.format(e))
        return False

def clear_entity_types(project_id):
    try:
        client = df.EntityTypesClient()
        path = client.project_agent_path(project_id)
        entity_type_names = []

        for entity_type in get_entity_types(project_id):
            entity_type_names.append(entity_type.name)

        response = client.batch_delete_entity_types(path, entity_type_names) 
        print('Entity types deleted: {}'.format(entity_type_names))
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connection to peer: {}'.format(e))
        return None
