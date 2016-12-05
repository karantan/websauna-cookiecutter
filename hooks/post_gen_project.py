from textwrap import dedent


vars = dict(
    separator='=' * 79,
)
msg = dedent(
    """
    %(separator)s
    Documentation: https://websauna.org/docs/
    Github:        https://github.com/websauna
    Twitter:       https://twitter.com/websauna9000
    Welcome to Websauna. See README.rst for further information.
    %(separator)s
    """ % vars)
print(msg)
