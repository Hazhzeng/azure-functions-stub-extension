from logging import Logger
from azure.functions import ExtensionManager, Context

# Good extension
def before_invocation_stub(logger: Logger, context: Context, *args, **kwargs):
    logger.info(f'BEFORE INVOCATION STUB {context.function_directory}')

def after_invocation_stub(logger: Logger, context: Context, *args, **kwargs):
    logger.info(f'AFTER INVOCATION STUB {context.function_directory}')


ExtensionManager.register_before_invocation(
    'azure.functions.stub.extension.before_invocation_stub',
    before_invocation_stub
)
ExtensionManager.register_after_invocation(
    'azure.functions.stub.extension.after_invocation_stub',
    after_invocation_stub
)

# Extension in bad state
def bad_before_invocation(logger: Logger, context: Context, *args, **kwargs):
    raise Exception('bad_before_invocation is throwing exception')


def bad_after_invocation(logger: Logger, context: Context, *args, **kwargs):
    raise Exception('bad_after_invocation is throwing exception')


ExtensionManager.register_before_invocation(
    'azure.functions.stub.extension.bad_before_invocation',
    bad_before_invocation
)
ExtensionManager.register_after_invocation(
    'azure.functions.stub.extension.bad_after_invocation',
    bad_after_invocation
)