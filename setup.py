from setuptools import setup, find_packages

setup(
    name='vastcap',  # Replace with the desired package name
    version='0.0.1',  # A minimal version
    packages=find_packages(),
    # Add a minimal description
    description='VastCap Python SDK',
    # Add an author and email (optional but good practice)
    author='vastien',
    author_email='contact@vast.sh',
    # Specify a license (important!)
    license='MIT',  # Or another appropriate license
    # Add a URL (optional)
    url='https://github.com/vastien/vastcap-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', # Specify minimal Python version
)
