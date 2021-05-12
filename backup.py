import os
from datetime import datetime
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, instance_ip_grouping_key

backupFolderName = datetime.now().strftime("%Y-%m-%d-%H-%M-%S");

cmd = "pg_basebackup -D /tmp/backup/{0} -U postgres".format(backupFolderName)

registry = CollectorRegistry()
g = Gauge('backup_status', 'Backup Status', registry=registry)
g.set(os.system(cmd) == 0 if 1 else 0)
push_to_gateway('pushgateway:9091', job='pg_basebackup', registry=registry)
