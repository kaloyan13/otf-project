# -*- coding: utf-8 -*-

"""
***************************************************************************
    OTF QGIS Project
    ---------------------
    Date                 : June 2016
    Copyright            : (C) 2016 by Etienne Trimaille
    Email                : etienne at kartoza dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.core import *
from . filters.style_manager import StyleManager
from . filters.map_composition import MapComposition
from . filters.layer_definition import LayerDefinition

__author__ = 'Etienne Trimaille'
__date__ = '25/05/2016'


class OtfProjectServer(object):

    """Plugin to create QGIS Project on the server."""

    def __init__(self, server_iface):
        QgsMessageLog.logMessage(
            'SUCCESS - OTF Project init', 'plugin', Qgis.MessageLevel.Info)

        #filters = [MapComposition, StyleManager, LayerDefinition]
        filters = [MapComposition]
        for i, f in enumerate(filters):
            name = f.__name__
            try:
                reg = server_iface.serviceRegistry()
                reg.registerService(MapComposition())
                QgsMessageLog.logMessage('OTF Project - loading %s' % name)
            except Exception as e:
                QgsMessageLog.logMessage(
                    'OTF Project - Error loading %s : %s' % (name, e))
