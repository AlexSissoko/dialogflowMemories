import dialogflow as df
from google.api_core import exceptions

def get_intents(project_id):
    try:
        client = df.IntentsClient()
        path = client.project_agent_path(project_id)
        return client.list_intents(path)
    except exceptions.ServiceUnavailables as e:
        print('An error occurred when connecting to peer: {}'.format(e))
        return []

def list_intents(project_id):
    intents = get_intents(project_id)
    for intent in intents:
        print('=' * 20)
        print('Intent name: {}'.format(intent.name))
        print('Intent display name: {}'.format(intent.display_name))
        print('Action: {}\n'.format(intent.action))
        print('Input contexts:')
        for name in intent.input_context_names:
            print('\tName: {}'.format(name))

        print('Output contexts:')
        for output_context in intent.output_contexts:
            print('\tName: {}'.format(output_context.name))

def get_intent_path(project_id, intent_name):
    for intent in get_intents(project_id):
        if intent.display_name == intent_name: return intent.name
    return ''

def create_blank_intent(project_id, intent_name):
    try:
        client = df.IntentsClient()
        path = client.project_agent_path(project_id)
        intent = df.types.Intent(display_name=intent_name)
        response = client.create_intent(path, intent)
        print('Intent created: {}'.format(response))
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None

def delete_intent(project_id, intent_name):
    try:
        client = df.IntentsClient()
        intent_path = get_intent_path(project_id, intent_name)
        if intent_path == '': raise ValueError("Intent does not exist!")
        response = client.delete_intent(intent_path)
        print(response)
        return True
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return False

def get_intent(project_id, intent_name, view=None):
    try:
        client = df.IntentsClient()
        intent_path = get_intent_path(project_id, intent_name)
        if intent_path == '': raise ValueError("Intent does not exist!")
        response = client.get_intent(intent_path, intent_view=view)
        print(response)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None

def create_tf_part(text, entity_type=None, alias=None):
    return df.types.Intent.TrainingPhrase.Part(
            text=text, entity_type=entity_type, alias=alias)

#TEMPLATE=2, Example=1
def create_tf(parts, tf_type=1):
    tf = df.types.Intent.TrainingPhrase(parts=parts)
    tf.type = tf_type
    return tf

def add_intent_phrases(project_id, intent_name, training_phrases):
    try:
        client = df.IntentsClient()
        intent = get_intent(project_id, intent_name, view='INTENT_VIEW_FULL')
        intent.training_phrases.extend(training_phrases)
        response = client.update_intent(
                    intent,
                    language_code='en',
                    intent_view='INTENT_VIEW_FULL')
        print(response)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None

def update_intent_phrases(project_id, intent_name, training_phrases):
    try:
        client = df.IntentsClient()
        intent = get_intent(project_id, intent_name)
        intent.training_phrases.extend(training_phrases)
        response = client.update_intent(
                    intent,
                    language_code='en',
                    intent_view='INTENT_VIEW_FULL')
        print(response)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None
    
def delete_training_phrases(project_id, intent_name):
    try:
        client = df.IntentsClient()
        intent = get_intent(project_id, intent_name)
        response = client.update_intent(
                    intent,
                    language_code='en',
                    intent_view='INTENT_VIEW_FULL')
        print(response)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None

def create_context_name(project_id, context_name):
    return 'projects/{}/agent/sessions/-/contexts/{}'.format(
            project_id, context_name)

def create_context(project_id, context_name, lifespan=0):
    if lifespan < 0 or lifespan > 5: raise ValueError('Invalid lifespan!')
    return df.types.Context(
                name=create_context_name(project_id, context_name),
                lifespan_count=lifespan)

#Add batch versions of these functions
def add_output_context(project_id, intent_name, context):
    try:
        client = df.IntentsClient()
        intent = get_intent(project_id, intent_name, view='INTENT_VIEW_FULL')
        intent.output_contexts.extend([context])
        response = client.update_intent(intent, language_code='en')
        print(response)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None

def add_input_context(project_id, intent_name, context_name):
    try:
        client = df.IntentsClient()
        intent = get_intent(project_id, intent_name, view='INTENT_VIEW_FULL')
        name = create_context_name(project_id, context_name)
        if name not in intent.input_context_names:
            intent.input_context_names.extend([name])
        response = client.update_intent(intent, language_code='en')
        print(response)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None
        
def add_event(project_id, intent_name, event_name):
    try:
        client = df.IntentsClient()
        intent = get_intent(project_id, intent_name, view='INTENT_VIEW_FULL')
        if event_name not in intent.events: intent.events.extend([event_name])
        response = client.update_intent(intent, language_code='en')
        print(response)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None

def create_basic_parameter(name, entity_type, mandatory=False):
    if entity_type[0] != '@': 
        raise ValueError('Parameter entity type is invalid')
    return df.types.Intent.Parameter(
            display_name=name,
            entity_type_display_name=entity_type,
            mandatory=mandatory)
                                    
def add_parameter(project_id, intent_name, parameter):
    try:
        client = df.IntentsClient()
        intent = get_intent(project_id, intent_name, view='INTENT_VIEW_FULL')
        intent.parameters.extend([parameter])
        response = client.update_intent(intent, language_code='en')
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None


def clear_intents(project_id):
    try:
        client = df.IntentsClient()
        intents = get_intents(project_id)
        intent_names =[{'name': intent.name} for intent in intents]
        print(intent_names)
        path = client.project_agent_path(project_id)
        response = client.batch_delete_intents(path, intent_names)
        return response
    except exceptions.ServiceUnavailable as e:
        print('An error occurred when connecting to peer" {}'.format(e))
        return None
