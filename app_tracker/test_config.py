import os

def verify_test_env_or_error():
    """Verify the required TESTING env variable is found.
    - If not found, raises RuntimeError.
    - The application config relies on this variable to set the appropriate
    database url.
    """

    if 'TESTING' not in os.environ:
        raise RuntimeError(
            "TESTING environment variable required." +
            " Are you correctly running tests?"
        )
