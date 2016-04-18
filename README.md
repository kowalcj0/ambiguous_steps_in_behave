Ambiguous Step definitions in behave
------------------------------------


# Requirements:
* behave (1.2.5)
* python 2.7.6


# Installation notes:

```bash
mkvirtualenv ambiguous
pip install -r requirements.txt
```

# Reproduce:
```bash
behave
Exception AmbiguousStep: @given('a resource with "{field_1} {operator_1} {value_1}" in "{property_1}" and "{field_2} {operator_2} {value_2}" in "{property_2}"') has already been defined in
  existing step @given('a resource with "{field_1} {operator_1} {value_1}" in "{property_1}"') at features/steps/steps.py:6
Traceback (most recent call last):
  File "/home/jk/.virtualenvs/ambigous/bin/behave", line 11, in <module>
    sys.exit(main())
  File "/home/jk/.virtualenvs/ambigous/local/lib/python2.7/site-packages/behave/__main__.py", line 109, in main
    failed = runner.run()
  File "/home/jk/.virtualenvs/ambigous/local/lib/python2.7/site-packages/behave/runner.py", line 672, in run
    return self.run_with_paths()
  File "/home/jk/.virtualenvs/ambigous/local/lib/python2.7/site-packages/behave/runner.py", line 678, in run_with_paths
    self.load_step_definitions()
  File "/home/jk/.virtualenvs/ambigous/local/lib/python2.7/site-packages/behave/runner.py", line 658, in load_step_definitions
    exec_file(os.path.join(path, name), step_module_globals)
  File "/home/jk/.virtualenvs/ambigous/local/lib/python2.7/site-packages/behave/runner.py", line 304, in exec_file
    exec(code, globals, locals)
  File "features/steps/steps.py", line 11, in <module>
    @given(u'a resource with "{field_1} {operator_1} {value_1}" in "{property_1}" and "{field_2} {operator_2} {value_2}" in "{property_2}"')
  File "/home/jk/.virtualenvs/ambigous/local/lib/python2.7/site-packages/behave/step_registry.py", line 85, in wrapper
    self.add_step_definition(step_type, step_text, func)
  File "/home/jk/.virtualenvs/ambigous/local/lib/python2.7/site-packages/behave/step_registry.py", line 49, in add_step_definition
    raise AmbiguousStep(message % (new_step, existing_step))
behave.step_registry.AmbiguousStep: @given('a resource with "{field_1} {operator_1} {value_1}" in "{property_1}" and "{field_2} {operator_2} {value_2}" in "{property_2}"') has already been defined in
  existing step @given('a resource with "{field_1} {operator_1} {value_1}" in "{property_1}"') at features/steps/steps.py:6
```
