import dialogflow as df
import argparse
import sys
from google.protobuf.pyext import _message
from google.api_core import operation

sys.path.insert(0, '../functionality')
from entity_manager import *
from entity_type_manager import create_entity_type, clear_entity_types

"""
Simple test suite for entity abstraction functions
"""

def test_get_entities(project_id):
    try: 
        entities = get_entities(project_id, 'Name')
        assert isinstance(entities, _message.RepeatedCompositeContainer)
        print('Get Entities: Success')
        return True
    except AssertionError:
        print('Get Entities: Failed')
        return False

def test_get_entity(project_id):
    try:
        entity = get_entity(project_id, 'Name', 'Alex')
        assert isinstance(entity, df.types.EntityType.Entity)
        print('Get Entity: Success')
        return True
    except AssertionError:
        print('Get Entity: Failed')
        return False

def test_add_entity(project_id):
    try:
        entity = create_entity('Sissoko', ['Sissoko'])
        response = add_entity(project_id, 'Name', entity)
        assert isinstance(response, operation.Operation)
        print('Add Entity: Success')
        return True
    except AssertionError:
        print('Add Entity: Failed')
        return False

def test_add_entities(project_id):
    try:
        entities = []
        entities.append(create_entity('Alex', ['Alex']))
        entities.append(create_entity('Faedryn', ['Faedryn']))
        entities.append(create_entity('Krasich', ['Krasich']))
        response = add_entities(project_id, 'Name', entities)
        assert isinstance(response, operation.Operation)
        print('Add Entities: Success')
        return True
    except AssertionError:
        print('Add Entities: Failed')
        return False

def test_update_entities(project_id):
    """
    CURRENTLY UPDATE ENTITIES FUNCTION from dialogflow library does not
    function correctly. So testing this is useless.
    """
    try:
        entities = []
        entities.append(create_entity('Get', ['Get']))
        entities.append(create_entity('Replaced', ['Replaced']))
        response = update_entities(project_id, 'Name', entities)
        assert isinstance(response, operation.Operation)
        return True
    except AssertionError:
        return False

def test_delete_entity(project_id):
    try:
        response = delete_entity(project_id, 'Name', 'Replaced')
        assert isinstance(response, operation.Operation)
        print('Delete Entity: Success')
        return True
    except AssertionError:
        print('Delete Entity: Failed')
        return False

def test_delete_entities(project_id):
    try:
        response = delete_entities(project_id, 'Name', ['Alex', 'Sissoko'])
        assert isinstance(response, operation.Operation)
        print('Delete Entities: Success')
        return True
    except AssertionError:
        print('Delete Entities: Failed')
        return False

def test_get_entity_synonyms(project_id):
    try:
        synonyms = get_entity_synonyms(project_id, 'Name', 'Celdryn')
        assert isinstance(synonyms, _message.RepeatedScalarContainer)
        print('Get Entity Synonyms: Success')
        return True
    except AssertionError:
        print('Get Entity Synonyms: Failed')
        return False

def add_name_type(project_id):
    entities = [create_entity('Celdryn', ['Celdryn'])]
    create_entity_type(
            project_id, 'Name', df.enums.EntityType.Kind.KIND_LIST, entities)

def evaluate_functions(project_id):
    add_name_type(project_id)
    tests_passed = 0

    tests_passed += test_add_entity(project_id)
    tests_passed += test_add_entities(project_id)
    tests_passed += test_get_entity(project_id)
    tests_passed += test_get_entities(project_id)
    tests_passed += test_delete_entity(project_id)
    tests_passed += test_delete_entities(project_id)
    tests_passed += test_get_entity_synonyms(project_id)

    clear_entity_types(project_id)
    print('Entities working functions: {}/7'.format(tests_passed))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
            '--project-id',
            help='Project/agent id. Required.',
            required=True)

    args = parser.parse_args()

    evaluate_functions(args.project_id)
