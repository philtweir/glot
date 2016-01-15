# This file is part of the Go-Smart Simulation Architecture (GSSA).
# Go-Smart is an EU-FP7 project, funded by the European Commission.
#
# Copyright (C) 2013-  NUMA Engineering Ltd. (see AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import gosmart_sf_config
import yaml

# CMake generated module
git_revision = gosmart_sf_config.git_revision
etc_location = gosmart_sf_config.etc_location

__config = None


def init_config(config_file=None):
    global __config

    if config_file is None:
        config_file = os.path.join(etc_location, 'gssa.yml')

    try:
        __config = yaml.safe_load(config_file)
    except IOError:
        print("[no config file found]")
        __config = {}


def get_global_config(key, default=None):
    if __config is None:
        init_config()

    try:
        value = __config
        for key_level in key.split('.'):
            value = value[key_level]
        return value
    except KeyError:
        return default
