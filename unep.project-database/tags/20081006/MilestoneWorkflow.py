#
# Generated by dumpDCWorkflow.py written by Sebastien Bigaret
# Original workflow id/title: MilestoneWorkflow/Milestone Workflow [Plone]
# Date: 2006/09/18 07:04:46.685 GMT+3
#
# WARNING: this dumps does NOT contain any scripts you might have added to
# the workflow, IT IS YOUR RESPONSABILITY TO MAKE BACKUPS FOR THESE SCRIPTS.
#
# No script detected in this workflow
#
"""
Programmatically create a workflow type.
"""
__version__ = "$Id: dumpDCWorkflow.py 25723 2006-07-04 08:41:22Z b_mathieu $"

from Products.CMFCore.WorkflowTool import addWorkflowFactory
from Products.DCWorkflow.DCWorkflow import DCWorkflowDefinition
from Products.PythonScripts.PythonScript import PythonScript
from Products.ExternalMethod.ExternalMethod import ExternalMethod

def setup_MilestoneWorkflow(wf):
    """Setup the workflow
    """
    wf.setProperties(title='Milestone Workflow')

    for s in ('pending', 'private', 'published', 'visible'):
        wf.states.addState(s)
    for t in ('hide', 'publish', 'reject', 'retract', 'show', 'submit'):
        wf.transitions.addTransition(t)
    for v in ('action', 'actor', 'comments', 'review_history', 'time'):
        wf.variables.addVariable(v)
    for l in ('reviewer_queue',):
        wf.worklists.addWorklist(l)
    for p in ('Access contents information',
              'Modify portal content',
              'View',
              'Change portal events'):
        wf.addManagedPermission(p)

    # Initial State
    wf.states.setInitialState('visible')

    # State Initialization
    sdef = wf.states['pending']
    sdef.setProperties(title='Pending',
                       description='',
                       transitions=('hide', 'publish', 'reject', 'retract'))
    sdef.setPermission('Access contents information', 1,
                       ['Manager', 'Owner', 'Reviewer'])
    sdef.setPermission('Modify portal content', 0,
                       ['Manager', 'Reviewer'])
    sdef.setPermission('View', 1,
                       ['Manager', 'Owner', 'Reviewer'])
    sdef.setPermission('Change portal events', 0,
                       ['Manager', 'Reviewer'])

    sdef = wf.states['private']
    sdef.setProperties(title='Private',
                       description='',
                       transitions=('show',))
    sdef.setPermission('Access contents information', 0,
                       ['Manager', 'Owner'])
    sdef.setPermission('Modify portal content', 0,
                       ['Manager', 'Owner'])
    sdef.setPermission('View', 0,
                       ['Manager', 'Owner'])
    sdef.setPermission('Change portal events', 0,
                       ['Manager', 'Owner'])

    sdef = wf.states['published']
    sdef.setProperties(title='Published',
                       description='',
                       transitions=('reject', 'retract'))
    sdef.setPermission('Access contents information', 1,
                       ['Anonymous', 'Manager'])
    sdef.setPermission('Modify portal content', 0,
                       ['Manager'])
    sdef.setPermission('View', 1,
                       ['Anonymous', 'Manager'])
    sdef.setPermission('Change portal events', 0,
                       ['Manager'])

    sdef = wf.states['visible']
    sdef.setProperties(title='Public Draft',
                       description='',
                       transitions=('hide', 'publish', 'submit'))
    sdef.setPermission('Access contents information', 1,
                       ['Anonymous', 'Manager', 'Reviewer', 'MilestoneEdit'])
    sdef.setPermission('Modify portal content', 1,
                       ['Manager', 'Owner', 'MilestoneEdit'])
    sdef.setPermission('View', 1,
                       ['Anonymous', 'Manager', 'Reviewer', 'MilestoneEdit'])
    sdef.setPermission('Change portal events', 0,
                       ['Manager', 'Owner', 'MilestoneEdit'])

    # Transition Initialization
    tdef = wf.transitions['hide']
    tdef.setProperties(title='Member makes content private',
                       description='',
                       new_state_id='private',
                       trigger_type=1,
                       script_name='',
                       after_script_name='',
                       actbox_name='Make private',
                       actbox_url='%(content_url)s/content_hide_form',
                       actbox_category='workflow',
                       props={'guard_roles': 'MilestoneEdit'},
                       )

    tdef = wf.transitions['publish']
    tdef.setProperties(title='PO publishes content',
                       description='',
                       new_state_id='published',
                       trigger_type=1,
                       script_name='',
                       after_script_name='',
                       actbox_name='Publish',
                       actbox_url='%(content_url)s/content_publish_form',
                       actbox_category='workflow',
                       props={'guard_permissions': 'Review portal content',
                              'guard_roles': 'MilestoneEdit'},
                       )

    tdef = wf.transitions['reject']
    tdef.setProperties(title='PO rejects submission',
                       description='',
                       new_state_id='visible',
                       trigger_type=1,
                       script_name='',
                       after_script_name='',
                       actbox_name='Reject',
                       actbox_url='%(content_url)s/content_reject_form',
                       actbox_category='workflow',
                       props={'guard_permissions': 'Review portal content',
                              'guard_roles': 'MilestoneEdit'},
                       )

    tdef = wf.transitions['retract']
    tdef.setProperties(title='Member retracts submission',
                       description='',
                       new_state_id='visible',
                       trigger_type=1,
                       script_name='',
                       after_script_name='',
                       actbox_name='Retract',
                       actbox_url='%(content_url)s/content_retract_form',
                       actbox_category='workflow',
                       props={'guard_permissions': 'Request review'},
                       )

    tdef = wf.transitions['show']
    tdef.setProperties(title='Member makes content visible',
                       description='',
                       new_state_id='visible',
                       trigger_type=1,
                       script_name='',
                       after_script_name='',
                       actbox_name='Make visible',
                       actbox_url='%(content_url)s/content_show_form',
                       actbox_category='workflow',
                       props={'guard_roles': 'MilestoneEdit'},
                       )

    tdef = wf.transitions['submit']
    tdef.setProperties(title='Member requests publishing',
                       description='',
                       new_state_id='pending',
                       trigger_type=1,
                       script_name='',
                       after_script_name='',
                       actbox_name='Submit',
                       actbox_url='%(content_url)s/content_submit_form',
                       actbox_category='workflow',
                       props={'guard_permissions': 'Request review'},
                       )

    # State Variable
    wf.variables.setStateVar('review_state')

    # Variable Initialization
    vdef = wf.variables['action']
    vdef.setProperties(description='The last transition',
                       default_value='',
                       default_expr='transition/getId|nothing',
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    vdef = wf.variables['actor']
    vdef.setProperties(description='The ID of the user who performed the last transition',
                       default_value='',
                       default_expr='user/getId',
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    vdef = wf.variables['comments']
    vdef.setProperties(description='Comments about the last transition',
                       default_value='',
                       default_expr="python:state_change.kwargs.get('comment', '')",
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    vdef = wf.variables['review_history']
    vdef.setProperties(description='Provides access to workflow history',
                       default_value='',
                       default_expr='state_change/getHistory',
                       for_catalog=0,
                       for_status=0,
                       update_always=0,
                       props={'guard_permissions': 'Request review; Review portal content'})

    vdef = wf.variables['time']
    vdef.setProperties(description='Time of the last transition',
                       default_value='',
                       default_expr='state_change/getDateTime',
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    # Worklist Initialization
    ldef = wf.worklists['reviewer_queue']
    ldef.setProperties(description='Reviewer tasks',
                       actbox_name='Pending (%(count)d)',
                       actbox_url='%(portal_url)s/search?review_state=pending',
                       actbox_category='global',
                       props={'guard_permissions': 'Review portal content',
                              'guard_roles': 'MilestoneEdit',
                              'var_match_review_state': 'pending'})

def create_MilestoneWorkflow(id):
    """Create, setup and return the workflow.
    """
    ob = DCWorkflowDefinition(id)
    setup_MilestoneWorkflow(ob)
    return ob

addWorkflowFactory(create_MilestoneWorkflow,
                   id='MilestoneWorkflow',
                   title='Milestone Workflow')


