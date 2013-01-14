# Copyright (C) 2012 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Volume Backups interface (1.1 extension).
"""

from cinderclient import base


class VolumeBackup(base.Resource):
    """A volume backup is a block level backup of a volume to swift."""
    def __repr__(self):
        return "<VolumeBackup: %s>" % self.id

    def delete(self):
        """
        Delete this volume backup.
        """
        return self.manager.delete(self)


class VolumeBackupManager(base.ManagerWithFind):
    """Manage :class:`VolumeBackup` resources."""
    resource_class = VolumeBackup

    def create(self, volume_id, container=None,
               display_name=None, display_description=None):
        """Backup a volume to swift.

        :param volume_id: The ID of the volume to backup.
        :param container: The name of the swift container.
        :param display_name: The name of the volume backup.
        :param display_description: The description of the volume backup.
        :rtype: :class:`VolumeBackup`
        """
        body = {'backup': {'volume_id': volume_id,
                           'container': container,
                           'display_name': display_name,
                           'display_description': display_description}}
        return self._create('/backups', body, 'backup')

    def get(self, backup_id):
        """Get a volume backup.

        :param backup_id: The ID of the backup backup to display.
        :rtype: :class:`VolumeBackup`
        """
        return self._get("/backups/%s" % backup_id, "backup")

    def list(self, detailed=True):
        """Get a list of all volume backups.

        :rtype: list of :class:`VolumeBackup`
        """
        if detailed is True:
            return self._list("/backups/detail", "backups")
        else:
            return self._list("/backups", "backups")

    def delete(self, backup):
        """Delete a volume backup.

        :param backup: The :class:`VolumeBackup` to delete.
        """
        self._delete("/backups/%s" % base.getid(backup))
