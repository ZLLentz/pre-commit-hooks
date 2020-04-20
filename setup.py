import versioneer
from setuptools import setup, find_packages

# with open('requirements.txt') as f:
#     requirements = [f.read().split()]
requirements = []

hook_names = ['twincat-lineids-remover',
              'leading-tabs-remover']
console_scripts = []
for name in hook_names:
    module = name.replace('-', '_')
    console_scripts.append(f'{name}=pre_commit_hooks.{module}:main')

setup(name='pre-commit-hooks',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='SLAC National Accelerator Laboratory',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
      description='SLAC LCLS custom pre-commit-hooks',
      entry_points={'console_scripts': console_scripts},
      )
