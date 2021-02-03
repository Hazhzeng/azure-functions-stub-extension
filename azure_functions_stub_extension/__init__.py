from azure.functions import ExtensionManager, Context
from logging import Logger
from azure.functions.extension import ExtensionManager

def before_invocation_stub(logger: Logger, context: Context):
    logger.info(f'BEFORE INVOCATION STUB {context.function_directory}')

def after_invocation_stub(logger: Logger, context: Context):
    logger.info(f'AFTER INVOCATION STUB {context.function_directory}')


ExtensionManager.register_before_invocation(
    'azure.functions.stub.extension.before_invocation_stub',
    before_invocation_stub
)
ExtensionManager.register_after_invocation(
    'azure.functions.stub.extension.after_invocation_stub',
    after_invocation_stub
)