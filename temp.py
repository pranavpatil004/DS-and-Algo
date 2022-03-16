@pytest.fixture(params=['John', 'Janine']) 
def name(request):
    return request.param


@pytest.mark.parametrize('greeting', [
'Welcome',
'Bienvenue',
])
def test_greeter(greeting, name):
    greeter_output = greeter(greeting, name)

    assert name in greeter_output
    assert greeting in greeter_output
