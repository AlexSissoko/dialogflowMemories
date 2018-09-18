import dialogflow as df
import argparse
import sys
from google.api_core import page_iterator, operation

sys.path.insert(0, '../functionality')
from intent_manager import *
from entity_type_manager import create_entity_type, clear_entity_types
from entity_manager import create_entity

def add_name_type(project_id):
    entities = [create_entity('Celdryn', ['Celdryn'])]
    create_entity_type(
            project_id, 'Name', df.enums.EntityType.Kind.KIND_LIST, entities)

def test_get_intents(project_id):
    try:
        intents = get_intents(project_id)
        assert isinstance(intents, page_iterator.GRPCIterator)
        print('Get Intents: Success')
        return True
    except AssertionError:
        print('Get Intents: Failed')
        return False

def test_get_intent_path(project_id):
    try:
        path = get_intent_path(project_id, 'Elantris')
        assert isinstance(path, str)
        assert path
        print('Get Intent Path: Success')
        return True
    except AssertionError:
        print('Get Intent Path: Failed')
        return False

def test_blank_intent(project_id):
    try:
        intent = create_blank_intent(project_id, 'Elantris')
        assert isinstance(intent, df.types.Intent)
        create_blank_intent(project_id, 'Calimer')
        print('Create Blank Intent: Success')
        return True
    except AssertionError:
        print('Create Blank Intent: Failed')
        return False

def test_delete_intent(project_id):
    try:
        resp = delete_intent(project_id, 'Elantris')
        assert resp == True
        print('Delete Intent: Success')
        return True
    except AssertionError:
        print('Delete Intent: Failed')
        return False

def test_get_intent(project_id):
    try:
        intent = get_intent(project_id, 'Calimer')
        assert isinstance(intent, df.types.Intent)
        print('Get Intent: Success')
        return True
    except AssertionError:
        print('Get Intent: Failed')
        return False

def test_add_phrases(project_id):
    try:
        part_one = create_tf_part(
                'Erythria', entity_type='@Name', alias='Felys')
        part_two = create_tf_part(' is beautiful!')
        tf = create_tf([part_one, part_two])
        resp = add_intent_phrases(project_id, 'Calimer', [tf])
        assert isinstance(resp, df.types.Intent)
        print('Add Intent Phrases: Success')
        return True
    except AssertionError:
        print('Add Intent Phrases: Failed')
        return False

def test_update_phrases(project_id):
    try:
        part_one = create_tf_part('Get replaced extras!')
        tf = create_tf([part_one])
        resp = update_intent_phrases(project_id, 'Calimer', [tf])
        assert isinstance(resp, df.types.Intent)
        assert len(resp.training_phrases) == 1
        print('Update Intent Phrases: Success')
        return True
    except AssertionError:
        print('Update Intent Phrases: Failed')
        return False

def test_delete_phrases(project_id):
    try:
        resp = delete_training_phrases(project_id, 'Calimer')
        assert isinstance(resp, df.types.Intent)
        assert len(resp.training_phrases) == 0
        print('Delete Intent Training Phrases: Success')
        return True
    except AssertionError:
        print('Delete Intent Training Phrases: Failed')
        return False

def test_add_output_context(project_id):
    try:
        context = create_context(project_id, 'ilikepie')
        resp = add_output_context(project_id, 'Calimer', context)
        assert isinstance(resp, df.types.Intent)
        print('Add output context: Success')
        return True
    except AssertionError:
        print('Add output context: Failed')
        return False

def test_add_input_context(project_id):
    try:
        resp = add_input_context(project_id, 'Calimer', 'applecranberrypie')
        assert isinstance(resp, df.types.Intent)
        print('Add input context: Success')
        return True
    except AssertionError:
        print('Add input context: Failed')
        return False

def test_add_event(project_id):
    try:
        resp = add_event(project_id, 'Calimer', 'blublub')
        assert isinstance(resp, df.types.Intent)
        print('Add event: Success')
        return True
    except AssertionError:
        print('Add event: Failed')
        return False

def test_add_parameter(project_id):
    try:
        param = create_basic_parameter('Felys', '@Name', True)
        resp = add_parameter(project_id, 'Calimer', param)
        assert isinstance(resp, df.types.Intent)
        print('Add Intent Parameter: Success')
        return True
    except AssertionError:
        print('Add Intent Parameter: Failed')
        return False

def test_clear_intents(project_id):
    try:
        resp = clear_intents(project_id)
        assert isinstance(resp, operation.Operation)
        print('Clear Intents: Success')
        return True
    except AssertionError:
        print('Clear Intents: Failed')
        return False

def add_name_type(project_id):
    entities = [create_entity('Celdryn', ['Celdryn'])]
    create_entity_type(
            project_id, 'Name', df.enums.EntityType.Kind.KIND_LIST, entities)

def evaluate_functions(project_id):
    add_name_type(project_id)
    tests_passed = 0
    tests_passed += test_blank_intent(args.project_id)
    tests_passed += test_get_intents(args.project_id)
    tests_passed += test_get_intent_path(args.project_id)
    tests_passed += test_delete_intent(args.project_id)
    tests_passed += test_get_intent(args.project_id)
    tests_passed += test_add_output_context(args.project_id)
    tests_passed += test_add_input_context(args.project_id)
    tests_passed += test_add_event(args.project_id)
    tests_passed += test_add_parameter(args.project_id)
    tests_passed += test_add_phrases(args.project_id)
    tests_passed += test_update_phrases(args.project_id)
    tests_passed += test_delete_phrases(args.project_id)
    tests_passed += test_clear_intents(args.project_id)

    clear_entity_types(project_id)
    print('Intent Working functions: {}/13'.format(tests_passed))

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
