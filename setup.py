from setuptools import setup
import re

version = ''
with open('sup/__init__.py') as f:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if match is not None:
        version = match.group(1)
    else:
        raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
with open('README.md') as f:
    readme = f.read()

packages = [
    'sup'
]

setup(name='psup',
      author='EnokiUN',
      url='https://github.com/EnokiUN/sup',
      project_urls={
        "Documentation": "https://sup.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/enokiun/sup/issues",
      },
      download_url='https://github.com/EnokiUN/sup/archive/refs/tags/Release-0-1-1-5a.tar.gz',
      version=version,
      license='MIT',
      packages=packages,
      description='A simple library for making complex stories and games.',
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      python_requires='>=3.8.0',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
      ]
)
