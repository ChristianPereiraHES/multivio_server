#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Main script for WSGI apache module.
"""

# ==============================================================================
#  This file is part of the Multivio software.
#  Project  : Multivio - https://www.multivio.org/
#  Copyright: (c) 2009-2011 RERO (http://www.rero.ch/)
#  License  : See file COPYING
# ==============================================================================


# ---------------------------- Modules -----------------------------------------

import sys
#sys.stdout = sys.stderr
import os

# mvo_config.py is in the same directory than the main wsgi application
#script_dir = os.path.dirname(__file__)
sys.path.insert(0, "/var/www/multivio/server")
import mvo_config

# library location
#[sys.path.insert(0, p) for p in MVOConfig.General.sys_pathes]

from multivio.dispatcher_app import DispatcherApp

application = DispatcherApp()
