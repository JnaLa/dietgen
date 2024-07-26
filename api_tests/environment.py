import logging

def setup_logging():
    handlers = [
        logging.FileHandler('test.log'),
        logging.StreamHandler()
    ]
    
    logging.basicConfig(level=logging.DEBUG, handlers=handlers)
    logger = logging.getLogger(__name__)
    logger.info("Logging setup complete.")

## Call the function to set up logging
setup_logging()

def before_all(context):
    # Set up global state, initialize databases, start services, etc.
    context.base_url = 'http://localhost:5000'
    print("Setting up global state before all tests")


def after_all(context):
    # Clean up global state, close databases, stop services, etc.
    print("Cleaning up global state after all tests")

def before_feature(context, feature):
    # Set up feature-specific state
    print(f"Setting up before feature: {feature.name}")

def after_feature(context, feature):
    # Clean up feature-specific state
    print(f"Cleaning up after feature: {feature.name}")

def before_scenario(context, scenario):
    # Reset context attributes before each scenario
    context.response = None
    context.food_id = None
    print(f"Setting up before scenario: {scenario.name}")