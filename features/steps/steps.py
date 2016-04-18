# -*- coding: utf-8 -*-

from behave import given


@given(u'a resource with "{field_1} {operator_1} {value_1}" in "{property_1}"')
def step_impl(context, **kwargs):
    pass


@given(u'a resource with "{field_1} {operator_1} {value_1}" in "{property_1}" and "{field_2} {operator_2} {value_2}" in "{property_2}"')
def step_impl(context, **kwargs):
    pass


@given(u'a resource with "{field_1} {operator_1} {value_1}" in "{property_1}" and "{field_2} {operator_2} {value_2}" in "{property_2}" and "{field_3} {operator_3} {value_3}" in "{property_3}"')
def step_impl(context, **kwargs):
    pass
