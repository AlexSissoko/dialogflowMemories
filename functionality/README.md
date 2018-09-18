# Function explanations
## General Information
These are just simple illustrations of functions that execute basic Dialogflow functionality. They are not necessarily the most efficient.

The relatively useless `try/except` blocks are added as an illustration of how to handle exceptions that will be thrown by errors due to connections with dialogflow. It's simply a matter of import the proper module `from google.api_core import exceptions` and then treating these `exceptions` in the same way that you would in-built ones.

## Entity Type Manager
+ [get_entity_types](#GetEntityTypes)
+ [list_entity_types](#ListEntityTypes)
+ [get_entity_type](#GetEntityType)
+ [get_entity_type_path](#GetEntityTypePath)
+ [get_entity_type_id](#GetEntityTypeId)
+ [create_entity_type](#CreateEntityType)
+ [delete_entity_type](#DeleteEntityType)
+ [clear_entity_types](#ClearEntityTypes)

## Entity Manager
+ [check_entity_type](#CheckEntityType)
+ [get_entities](#GetEntities)
+ [list_entities](#ListEntities)
+ [get_entity](#GetEntity)
+ [add_entity](#AddEntity)
+ [add_entities](#AddEntities)
+ [update_entities](#Update_entities)
+ [delete_entity](#DeleteEntity)
+ [delete_entities](#DeleteEntities)
+ [get_entity_synonyms](#GetEntitySynonyms)

## Intent Manager
+ [get_intents](#GetIntents)
+ [list_intents](#ListIntents)
+ [get_intent_path](#GetIntentPath)
+ [create_blank_intent](#CreateBlankIntent)
+ [delete_intent](#DeleteIntent)
+ [get_intent](#GetIntent)
+ [add_intent_phrases](#AddIntentPhrases)
+ [update_intent_phrases](#UpdateIntentPhrases)
+ [delete_training_phrases](#DeleteTrainingPhrases)
+ [add_output_context](#AddOutputContext)
+ [add_input_context](#AddInputContext)
+ [add_parameter](#AddParameter)
+ [clear_intents](#ClearIntents)
+ [Creating an Update Mask Example](#UpdateMask)


## Entity Type Manager

<a name="GetEntityTypes"></a>
### get_entity_types
Retrieves a list of the entity types defined for the specified agent.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
Returns `google.api_core.page_iterator.GRPCIterator`

<a name="ListEntityTypes"></a>
### list_entity_types
Prints out the entity types defined for the specified agent.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
No return type.

<a name="GetEntityType"></a>
### get_entity_type
Retrieves the specified entity type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the desired entity type. |
Returns `dialogflow.types.EntityType`

<a name="GetEntityTypePath"></a>
### get_entity_type_path
Retrieves the path (or full name) of the specified entity type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the desired entity type |
Returns `str` of the form `projects/{project_id}/agent/entityTypes/{entity_type_id}`.

<a name="GetEntityTypeId"></a>
### get_entity_type_id
Retrieves the id number of the specified entity type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the desired entity type |
Returns `str`, a permutation of numbers, lowercase letters and hyphens.

<a name="CreateEntityType"></a>
### create_entity_type
Creates an entity type with the specified name, kind, and entities.
The entity type _kind_ can be only one of two values: KIND_MAP and KIND_LIST.

A `KIND_MAP` entity type allows entities to have multiple synonyms that will be mapped to that value if recognized. You would use this value if you have an entity type where different values are functionally the same.
E.g. We have a simple Temperature entity type for an agent that asks people to describe the temperature outside. For all intents and purposes, it being "cold" outside is pretty much the same as it being "freezing" outside. You probably need to put on a jacket. So, we make the Temperature Entity a KIND_MAP entity and then the "Cold" value would have "Cold" and "Freezing as synonyms".

A `KIND_LIST` entity type allows entities to have only a single synonym that must be the same as the entity's value. So, you would make an entity type a KIND_LIST if each value is unique (has no relevant synonyms). Think something like a Name entity type where each name is unique. Even if they're close, Steven and Stephen are still different.


| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the desired entity type |
| kind | `dialogflow.enums.EntityType.Kind` | Describes how the entity mapping will work for this entity type |
| entities | `list` | A list of entities that belong to the entity type. Default value is empty list. |
Returns `dialogflow.types.EntityType`, the newly created entity type.

<a name="DeleteEntityType"></a>
### delete_entity_type
Deletes an entity type with the specified name.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the desired entity type |
Returns `True` on success, `False` on failure.

<a name="ClearEntityTypes"></a>
### clear_entity_types
Clears all entity types belonging to the specified agent.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the desired entity type |
Returns `google.api_core.operation.Operation`.

So, when there are calls to the api that can take a decent amount of time, then the api will return an `Operation` instance so that you can handle them either synchronously or asynchronously. Deciding how you want to handle them is entirely up to you.


## Entity Manager
<a name="CheckEntityType"></a>
### check_entity_type
Checks that an entity type exists before attempting any operations on it.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being checked.|
Returns `dialogflow.types.EntityType`

<a name="GetEntities"></a>
### get_entities
Retrieves entities that belong to a specified Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type whose entities are being retrieved.|
Returns `google.protobuf.pyext._message.RepeatedCompositeContainer`.

<a name="ListEntities"></a>
### list_entities
List the entities belonging to the specified Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type whose entities are being listed.|
No return type.

<a name="GetEntity"></a>
### get_entity
Retrieves an entity with the specified value belonging to the specified Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being searched.|
| value | `str` | The entity value being searched for. |
Returns `dialogflow.types.EntityType.Entity` on success. `None` on failure.

<a name="AddEntity"></a>
### add_entity
Adds an entity to the specified Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being modified.|
| entity | `dialogflow.types.EntityType.Entity` | The entity value being added. |
Returns `google.api_core.operation.Operation`.

<a name="AddEntities"></a>
### add_entities
Adds multiple entities to the specified Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being modified.|
| entities | `list` | The list of entities to be added. |
Returns `google.api_core.operation.Operation`.

<a name="UpdateEntities"></a>
### update_entities
Updates the entity values of the specified Entity Type. This differs from [add_entities](#AddEntities) in that it removes pre-existing entity values from the Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being modified.|
| entities | `list` | The list of entity values that will replace the existing ones. |
Returns `google.api_core.operation.Operation`.

<a name="DeleteEntity"></a>
### delete_entity
Deletes an entity from the specified Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being modified.|
| entity_value | `str` | The entity value being deleted. |
Returns `google.api_core.operation.Operation`.

<a name="DeleteEntities"></a>
### delete_entities
Deletes multiple entities from the specified Entity Type.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being modified.|
| entity_values | `list` | The list of entity values being deleted. |
Returns `google.api_core.operation.Operation`.

<a name="GetEntitySynonyms"></a>
### get_entity_synonyms
Retrieves the synonyms of a entity with the specified value.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| type_name | `str` | The display name of the entity type being searched through.|
| entity_value | `str` | The entity value whose synonyms are being checked for. |
Returns `google.protobuf.pyext._message.RepeatedScalarContainer`.


## Intent Manager
<a name="GetIntents"></a>
### get_intents
Retrieves the intents in the specified project.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
Returns `google.api_core.page_iterator.GRPCIterator`.

<a name="ListIntents"></a>
### list_intents
Lists the intents in the specified project.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
No return type.

<a name="GetIntentPath"></a>
### get_intent_path
Retrieves full path name of the intent with the specified display name.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent who's path we want. |
Returns `str`.

<a name="CreateBlankIntent"></a>
### create_blank_intent
Creates a blank intent. The only thing specified is the intent name.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to create. |
Returns `dialogflow.types.Intent`.

<a name="DeleteIntent"></a>
### delete_intent
Deletes the intent with the specified intent name.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to delete. |
Returns `bool` (The actual delete operation on a dialogflow client returns `None`).

<a name="GetIntent"></a>
### get_intent
Retrieves the intent with the specified intent name. To be able to retrieve the full intent object (with training phrases), you need to make sure that you use the proper view.
The view parameter can have two possible values : `INTENT_VIEW_FULL` and `INTENT_VIEW_UNSPECIFIED`.

`INTENT_VIEW_UNSPECIFIED` is the default value, where training phrases are omitted from the returned intent. If you don't want to see training phrases, leave view as its default value of `None` because this will default to the above value.

`INTENT_VIEW_FULL` includes training phrases in the returned intent.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent who's path we want. |
| view | `str` | The view that we is used when the specified intent is returned. Default value: `None`|
Returns `dialogflow.types.Intent`.

<a name="AddIntentPhrases"></a>
### add_intent_phrases
Adds training phrases to the specified intent.
##### Creating a training phrase
Training phrases aren't just strings. Yay!
A training phrase is composed primarily of training phrase parts and the training phrase type.

**Note**: The parts variable that belongs to a training phrase instance is an instance of `google.protobuf.pyext._message.RepeatedCompositeContainer`, so certain `list` operations you might think of using won't work on it.

###### Training phrase Part
+ Type: `dialogflow.types.Intent.TrainingPhrase.Part`
+ Variables :
    - `text` of type `str`. The string the part corresponds to e.g. **"I like pie"**. Required.
    - `entity_type` of type `str`. The display name of the Entity Type that the Part corresponds to e.g. **"@PieLovingAssertion"**. Optional. _Note_: Must have **@** prepended to it if used.
    - `alias` of type `str`. The display name of the intent parameter that the Part corresponds to e.g.  **"LikesPie"**. Optional.

###### Training phrase Type
+ Type: `int`
+ The type of the training phrase has two pertinent values:
    - `1` which is equivalent to `EXAMPLE`.

    This means that the training phrase does not contain entity type names prefixed with **@** signs (so **@Fruit** can't be a Part).

    But, parts can be annotated with entity types (so a part like "_watermelon_" can be labeled as belonging to the **@Fruit** Entity Type by setting `entity_type="@Fruit"`).
    - `2` which is equivalent to `TEMPLATE`.

    This means that the training phrase is not annotated with entity types ("_watermelon"_ **cannot** be labeled as a **@Fruit**).

    However, the training phrase can contain **@** prefixed entity type names as substrings ("I like **@Fruit**" is A-OK).

    _Note_: If you try to label a part in a `TEMPLATE` training phrase with an entity type (e.g. `entity_type="@Course"`), then
    a bug can occur in which one of the entity type's entity values becomes a reference to itself (as in _Entity Type_=`Course` with _Entity Values_= `{@Course, ...}`), causing an infinite loop . All subsequent dialogflow interactions will fail until this entity value is deleted. This should only really happen if you try to set the entity type of a substring that is a prefixed entity type, so don't do that.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to modify. |
| training_phrases | `list` | The list of training phrases that we want to add to the intent. Training phrases are of the type `dialogflow.types.Intent.TrainingPhrase` |
Returns `dialogflow.types.Intent`.

<a name="UpdateIntentPhrases"></a>
### update_intent_phrases
Updates training phrases in the specified intent. Differs from [add_intent_phrases](#AddIntentPhrases) in that it deletes existing training_phrases.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to modify. |
| training_phrases | `list` | The list of training phrases that we want to update the intent with |
Returns `dialogflow.types.Intent`.

<a name="DeleteTrainingPhrases"></a>
### delete_intent_phrases
Deletes all training phrases in the specified intent.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to modify. |
Returns `dialogflow.types.Intent`.

<a name="AddOutputContext"></a>
### add_output_context
Adds an output context to the specified intent.

_Note_: A context must have a lifespan between 0 and 5 (inclusive). A lifespan of 0 means that if that particular context is present when the intent is fulfilled/finished, then that context will be erased.

Also, a context's full name is of the form `projects/{project_id}/agent/sessions/-/contexts/{context_display_name}`

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to modify. |
| context | `dialogflow.types.Context` | The context to be added to the intent. |
Returns `dialogflow.types.Intent`.

<a name="AddInputContext"></a>
### add_input_context
Adds an input context to the specified intent. This context will need to be present amongst the agent during a session for the intent to be invoked.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to modify. |
| context_name | `str` | The name of the input context to be added to the intent. This is expanded to a full context name in the function to be added to the intent. |
Returns `dialogflow.types.Intent`.

<a name="AddParameter"></a>
### add_parameter
Adds a parameter to the specified intent.

_Notes_: The parameter's `entity_type_display_name` value must be an existing entity type with a preceding **@** character. It also has `mandatory` and `isList` values that are pretty self-explanatory.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |
| intent_name | `str` | The display name of the intent we want to modify. |
| parameter | `df.types.Intent.Parameter` | The parameter to be added to the intent. |
Returns `dialogflow.types.Intent`.
<a name="ClearIntents"></a>
### clear_intents
Deletes all intents belonging to the agent in the specified project.

| Param | Type | Description |
| --- | --- | --- |
| project_id | `str` | The id name of the agent's project. |

Returns `google.api_core.operation.Operation`.

<a name="UpdateMask"></a>
### Creating an Update Mask Example
Just something useful that can come in handy if you want to just update a single specific part of an intent by creating a `dict` object.
```
from google.protobuf import field_mask_pb2

update_mask = field_mask_pb2.FieldMask(paths=['training_phrases'])

#Insert Update Here
```
