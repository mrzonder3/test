import os
from datetime import datetime
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, instance_ip_grouping_key

backupFolderName = datetime.now().strftime("%Y-%m-%d-%H-%M-%S");

cmd = "pg_basebackup -D /tmp/backup/{0} -U postgres".format(backupFolderName)
os.system(cmd)

registry = CollectorRegistry()
g = Gauge('metrics', 'Backup has been created successfully', registry=registry)
g.set_to_current_time()
push_to_gateway('pushgateway:9091', job='pg_basebackup', registry=registry)
