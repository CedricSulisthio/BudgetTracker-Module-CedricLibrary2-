from setuptools import setup, find_packages

setup(
    name="CedricLibrary2",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',  # For managing environment variables (if needed)
    ],
)