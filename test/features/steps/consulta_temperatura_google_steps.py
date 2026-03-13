#Autora: Beatriz
from behave import *

@given(u'que eu estou no site do google')
def step_impl(context):
    ...

@when(u'eu pesquiso a temperatura de hoje')
def step_impl(context):
    ...

@then(u'o navegador deve trazer a temperatura de hoje')
def step_impl(context):
    ...

@then(u'fecho o navegador')
def step_impl(context):
    ...