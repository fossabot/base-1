from aenum import Enum, unique, skip


@unique
class TaskName(Enum):
    @skip
    @unique
    class OverWatch(Enum):
        GET_WORKER_STATS = "overwatch.misc.get_worker_stats"
