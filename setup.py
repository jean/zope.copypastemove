##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.copypastemove package

$Id$
"""

import os

try:
    from setuptools import setup, Extension
except ImportError, e:
    from distutils.core import setup, Extension

setup(name='zope.copypastemove',
      version='3.4-dev',
      url='http://svn.zope.org/zope.copypastemove',
      license='ZPL 2.1',
      description='Zope copypastemove',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description="Copy, Paste and Move support for content components.",

      packages=['zope',
                'zope.copypastemove',
                'zope.copypastemove.tests'],
      package_dir = {'': 'src'},

      namespace_packages=['zope',],
      tests_require = ['zope.testing',
                       'zope.app.component',
                       'zope.app.principalannotation'],
      install_requires=['zope.interface',
                        'zope.exceptions',
                        'zope.component',
                        'zope.event',
                        'zope.location',
                        'zope.annotation',
                        'zope.lifecycleevent',
                        'zope.app.container'],
      include_package_data = True,

      zip_safe = False,
      )
