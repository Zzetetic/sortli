import builtins
import gettext

gettext.bindtextdomain('sort')
gettext.textdomain('sort')

builtins._ = gettext.gettext


from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import SortError
from .controllers.base import Base

# configuration defaults
CONFIG = init_defaults('sort')
CONFIG['sort']['foo'] = 'bar'


class Sort(App):
    """Sort App primary application."""

    class Meta:
        label = 'sort'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        #log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base
        ]


class SortTest(TestApp,Sort):
    """A sub-class of Sort that is better suited for testing."""

    class Meta:
        label = 'sort'


def main():
    with Sort() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except SortError as e:
            print('SortError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
