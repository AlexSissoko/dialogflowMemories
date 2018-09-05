project=`gcloud config list --format 'value(core.project)'`

testerMan () {
    typesResult=`python entity_types_test.py --project-id $project | tail -1`
    echo $typesResult
    entityResult=`python entity_tests.py --project-id $project | tail -1`
    echo $entityResult
    intentResult=`python intent_tests.py --project-id $project | tail -1`
    echo $intentResult
}

#Run testerMan
testerMan
