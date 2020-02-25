from setuptools import setup

setup(name='blir',
      version='0.0.1',
      python_requires='>=3.7.3',
      description='blir - balancing load of intermittent renewables: A characteristic-based linear optimization model',
      url='https://github.com/EnergyModels/blir',
      author='Jeff Bennett',
      author_email='jab6ft@virginia.edu',
      license = 'MIT',
      packages=['blir'],
      zip_safe=False,
      install_requires=['pyomo', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'joblib'])