
def test_it(cookies, capfd):
    result = cookies.bake(extra_context={
        'project_name': 'Test Project',
        'authentication_random': '123',
        'authomatic_random': '456',
        'session_random': '789',
    })

    out, err = capfd.readouterr()
    assert 'See README.rst for further information' in out

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_project'
    assert result.project.isdir()
    root_files = [
        f.basename for f in result.project.listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert root_files == [
        '.gitignore',
        'CHANGES.rst',
        'MANIFEST.in',
        'README.rst',
        'setup.cfg',
        'setup.py',
    ]
    alembic_files = [
        f.basename for f in result.project.join('alembic').listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert alembic_files == ['env.py', 'script.py.mako']

    project_dir = result.project.join('test_project')
    project_files = [
        f.basename for f in project_dir.listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert project_files == ['__init__.py', 'admins.py', 'models.py', 'views.py']
    conf_files = [
        f.basename for f in project_dir.join('conf').listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert conf_files == [
        'base.ini',
        'development-secrets.ini',
        'development.ini',
        'production-secrets.ini',
        'production.ini',
        'staging-secrets.ini',
        'staging.ini',
        'test-secrets.ini',
        'test.ini',
    ]
    static_files = [
        f.basename for f in project_dir.join('static').listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert static_files == ['logo.png', 'theme.css']
    email_files = [
        f.basename for f in project_dir.join('templates', 'email').listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert email_files == ['header.html']
    site_files = [
        f.basename for f in project_dir.join('templates', 'site').listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert site_files == ['css.html', 'logo.html']
    template_files = [
        f.basename for f in project_dir.join('templates', 'test_project').listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert template_files == ['home.html']
    tests_files = [
        f.basename for f in project_dir.join('tests').listdir()
        if f.isfile() and f.basename != '.DS_Store'
    ]
    assert tests_files == ['__init__.py', 'test_login.py']


def test_it_invalid_module_name(cookies, capfd):
    result = cookies.bake(extra_context={
        'repo_name': '0invalid',
    })
    assert result.exit_code == -1
