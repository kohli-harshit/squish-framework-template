def find_all_objects(obj_real_name):
    if "occurrence=" in obj_real_name:
        test.warning("Real name must not contain the occurrence property on the actual object (but it is okay for containers): %s" % obj_real_name)
 
    objects = []
    try:
        one_object = findObject(obj_real_name)
        objects.append(one_object)
 
        # Occurrence of second instance for Java, MFC, UIA:
        occurrence = 1
 
        # Occurrence of second instance for Qt, Web:
        if hasattr(one_object, "metaObject") or hasattr(one_object, "nextSibling"):
            occurrence = 2
 
        while True:
            backup = testSettings.objectNotFoundDebugging
            testSettings.objectNotFoundDebugging = False
            try:
                obj_real_name_n = "{occurrence='%s' %s}" % (occurrence, obj_real_name[1:-1])
                one_object = findObject(obj_real_name_n)
                objects.append(one_object)
                occurrence += 1
            finally:
                testSettings.objectNotFoundDebugging = backup
    except LookupError:
        # No more occurrences found
        pass
    return objects