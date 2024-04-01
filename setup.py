from setuptools import setup

setup(name='jupyter_c_kernel_wio',
      version='1.2.1',
      description='Minimalistic C kernel for Jupyter with input',
      author='Brendan Rius',
      author_email='ping@brendan-rius.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/brendan-rius/jupyter-c-kernel/',
      download_url='https://github.com/brendan-rius/jupyter-c-kernel/tarball/1.2.1',
      packages=['jupyter_c_kernel_wio'],
      scripts=['jupyter_c_kernel_wio/install_c_kernel_wio'],
      keywords=['jupyter', 'notebook', 'kernel', 'c', 'c_wio'],
      include_package_data=True
      )
