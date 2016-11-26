# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desiutil.plots.
"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
# The line above will help with 2to3 support.
import unittest
import os
import numpy as np
import sys
# Set non-interactive backend for Travis
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from ..plots import plot_slices
#from ..plots import plot_sky

try:
    basestring
except NameError:  # For Python 3
    basestring = str


class TestPlots(unittest.TestCase):
    """Test desiutil.plots
    """

    @classmethod
    def setUpClass(cls):
        cls.plot_file = 'test.png'
    #    cls.plot_file2 = 'test_sky.png'
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.plot_file):
            os.remove(cls.plot_file)
    #    if os.path.exists(cls.plot_file2):
    #        os.remove(cls.plot_file2)

    def test_slices(self):
        """Test plot_slices
        """
        # Random data
        x = np.random.rand(10000)
        y = np.random.randn(10000)
        # Run
        ax = plot_slices(x,y,0.,1.,0.)
        ax.set_ylabel('N sigma')
        ax.set_xlabel('x')
        plt.savefig(self.plot_file)
    @unittest.skipIf('mpl_toolkits.basemap' not in sys.modules or 'TRAVIS_JOB_ID' in os.environ, 'Skipping tests of plot_sky that require basemap and conflict with Travis')
    def test_plot_sky(self):
        """Test plot_sky
        """ 
        ra = 360.*np.random.rand(200)
        dec = 360.*np.random.rand(200)
        ax = plot_sky(ra,dec,discrete_colors=False,test_travis=True,pix_shape='square')
        plt.savefig(self.plot_file2)

def test_suite():
    """Allows testing of only this module with the command::

        python setup.py test -m <modulename>
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
