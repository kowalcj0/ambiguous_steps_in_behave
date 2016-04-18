Feature: Ambiguous step definitions


    Scenario: Test Ambiguous step definitions
        Given a resource with "field_1 == value_1" in "property_1"
        And a resource with "field_1 == value_1" in "property_1" and "field_2 == value_2" in "property_2"
        And a resource with "field_1 == value_1" in "property_1" and "field_2 == value_2" in "property_2" and "field_3 == value_3" in "property_3"
