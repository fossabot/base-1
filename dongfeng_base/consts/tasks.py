from aenum import Enum, unique, skip


@unique
class TaskName(Enum):
    @skip
    @unique
    class OverWatch(Enum):
        GET_WORKER_STATS = "overwatch.misc.get_worker_stats"
        RESOURCE_USAGE = "overwatch.misc.resource_usage"
        REPORT_UP_HOSTS = "overwatch.report.up_hosts"
        REPORT_OPEN_PORTS = "overwatch.report.open_ports"
        REPORT_SERVICE = "overwatch.report.service"

    @skip
    @unique
    class Scout(Enum):
        DETECT_HOST = "scout.host.detect_host"
        DETECT_PORT = "scout.host.detect_port"
        DETECT_SERVICE = "scout.host.detect_service"
