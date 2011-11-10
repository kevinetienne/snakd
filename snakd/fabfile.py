from fabric.api import local

def clean():
    local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)

def test():
    clean()
    local('python test/runtest.py')
