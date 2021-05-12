import os
from datetime import datetime
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

backupFolderName = datetime.now().strftime("%Y-%m-%d-%H-%M-%S");

cmd = "pg_basebackup -D /tmp/backup/{0} -U postgres".format(backupFolderName)

exit_code = os.system(cmd)

registry = CollectorRegistry()
g = Gauge('backup_status', 'Backup Status', registry=registry)
g.set(1 if exit_code == 0 else 0)
push_to_gateway('pushgateway:9091', job='pg_basebackup', registry=registry)
