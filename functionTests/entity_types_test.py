import dialogflow as df 
import argparse
import sys
from google.api_core import page_iterator, exceptions, operation

sys.path.insert(0, '../functionality')
from entity_type_manager import *

"""
Simple test suite for the entity type abstraction.
"""

"""
Entity Types: Pie, Name
"""

def test_create_type(project_id):
    """Returns True when both EntityTypes are created."""
    try: 
        resp_one = create_entity_type(
                project_id, 'Pie', df.enums.EntityType.Kind.KIND_MAP)
        assert isinstance(resp_one, df.types.EntityType)
        resp_two = create_entity_type(
                project_id, 'Name', df.enums.EntityType.Kind.KIND_LIST)
        assert isinstance(resp_two, df.types.EntityType)
        print('Create Entity Type: Success')
        return True
    except AssertionError:
        print('Create Entity Type: Success')
        return False

def test_get_types(project_id):
    """Returns True when a GRPCIterator is returned by get_entity_types."""
    try: 
        assert isinstance(get_entity_types(project_id), page_iterator.GRPCIterator)
        print('Get Entity Types: Success')
        return True
    except AssertionError:
        print('Get Entity Types: Failed')
        return False

def test_get_type(project_id):
    try: 
        pie_type = get_entity_type(project_id, 'Pie')
        assert isinstance(pie_type, df.types.EntityType)
        imaginary_type = get_entity_type(project_id, 'SadisticNuclearUnicorn')
        assert imaginary_type == None
        print('Get Entity Type: Success')
        return True
    except AssertionError:
        print('Get Entity Type: Failed')
        return False

def test_delete_type(project_id):
    try: 
        pie_exists = delete_entity_type(project_id, 'Pie')
        assert pie_exists == True
        pie_still_exists = delete_entity_type(project_id, 'Pie')
        assert pie_still_exists == False
        print('Delete Entity Type: Success')
        return True
    except AssertionError:
        print('Delete Entity Type: Failed')
        return False

def test_clear_types(project_id):
    try:
        assert isinstance(clear_entity_types(project_id), operation.Operation)
        print('Clear Entity Types: Success')
        return True
    except AssertionError:
        print('Clear Entity Types: Failed')
        return False

def evaluate_type_functions(project_id):
    tests_passed = 0

    tests_passed += test_create_type(project_id)
    tests_passed += test_get_types(project_id)
    tests_passed += test_get_type(project_id)
    tests_passed += test_delete_type(project_id)
    tests_passed += test_clear_types(project_id)

    print('Entity Types working functions: {}/5'.format(tests_passed))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
            '--project-id',
            help='Project/agent id. Required.',
            required=True)

    args = parser.parse_args()

    evaluate_type_functions(args.project_id)
