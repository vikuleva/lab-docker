try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Moon Landing Game',
    'version': 1.0,
    'install_requires': ['nose'],
    'packages': ['moonlanding'],
    'scripts': [],
    'entry_points': {
        "console_scripts": [
            "moonlanding-game = moonlanding.main:main"
        ]
    },
    'name': 'MoonLanding'
}

setup(**config)
