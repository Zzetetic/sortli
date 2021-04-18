from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
from sort import lib

VERSION_BANNER = get_version()


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = _('Sorting list app')

        # text displayed at the bottom of --help output
        epilog = _('Usage: sortli asc -l 2 1 3 -t bubble')

        # controller level arguments. ex: 'sort --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help=_('sorts numbers in ascending order'),

        # sub-command level arguments. ex: 'sort command1 --foo bar'
        arguments=[
            ( [ '-l', '--list' ],
              { 'help' : _('space-separated numbers for sorting'),
                'action'  : 'store',
                'type':float,
                'nargs':'*',
                'dest' : 'list' } ),
                
            ( [ '-t', '--type' ],
              { 'help' : _('type of sorting algorithm'),
                'action'  : 'store',
                'choices' : ['bubble', 'insertion'],
                'dest' : 'type' } ),
        ],
    )
    def asc(self):
        """Example sub-command."""

        ### do something with arguments
        if self.app.pargs.list is not None:
            if self.app.pargs.type == "insertion":
                lib.bubble_sort_asc(self.app.pargs.list)
            else:
                lib.insertion_sort_asc(self.app.pargs.list)
            
            data = dict()
            data['sorted_list'] = self.app.pargs.list
            self.app.render(data, 'sort.jinja2')        
        
    @ex(
        help=_('sorts numbers in descending order'),

        # sub-command level arguments. ex: 'sort command1 --foo bar'
        arguments=[
            ( [ '-l', '--list' ],
              { 'help' : _('space-separated numbers for sorting'),
                'action'  : 'store',
                'type':float,
                'nargs':'*',
                'dest' : 'list' } ),
                
            ( [ '-t', '--type' ],
              { 'help' : _('type of sorting algorithm'),
                'action'  : 'store',
                'choices': ['bubble', 'insertion'],
                'dest' : 'type' } ),
        ],
    )
    def desc(self):
        """Example sub-command."""

        ### do something with arguments
        if self.app.pargs.list is not None:
            if self.app.pargs.type == "insertion":
                lib.bubble_sort_desc(self.app.pargs.list)
            else:
                lib.insertion_sort_desc(self.app.pargs.list)
            data = dict()
            data['sorted_list'] = self.app.pargs.list
            self.app.render(data, 'sort.jinja2')
        
