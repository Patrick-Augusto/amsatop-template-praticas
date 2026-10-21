import os
from collections.abc import Iterator
from typing import NamedTuple

from amsatop import Htop, Process, TaskType
from amsatop.utils import StatFile, get_stat_file_from_path

PF_KTHREAD = 0x00200000


class Task(NamedTuple):
    pid: int
    folder: str
    stat: StatFile
    type: TaskType


class Amsatop(Htop):
    def get_processes(self) -> list[Process]:
        return [self._to_process(task) for task in self._tasks()]

    def get_priorities(self) -> list[Process]:
        return [self._to_process(task, task.stat.priority) for task in self._tasks()]

    def get_hup(self) -> list[Process]:
        raise NotImplementedError("Prac-2.3 implementation needed")

    def _tasks(self) -> Iterator[Task]:
        for entry in os.listdir(self.proc_folder):
            if not entry.isdigit():
                continue
            pid = int(entry)
            pid_folder = os.path.join(self.proc_folder, entry)
            stat = get_stat_file_from_path(os.path.join(pid_folder, "stat"))
            if stat is None:
                continue
            is_kthread = stat.flags & PF_KTHREAD != 0
            task_type = TaskType.KTHREAD if is_kthread else TaskType.PROCESS
            yield Task(pid, pid_folder, stat, task_type)
            if not is_kthread:
                yield from self._threads_of(pid_folder, pid)

    @staticmethod
    def _threads_of(pid_folder: str, pid: int) -> Iterator[Task]:
        task_folder = os.path.join(pid_folder, "task")
        try:
            entries = os.listdir(task_folder)
        except OSError:
            return
        for entry in entries:
            if not entry.isdigit() or int(entry) == pid:
                continue
            thread_folder = os.path.join(task_folder, entry)
            stat = get_stat_file_from_path(os.path.join(thread_folder, "stat"))
            if stat is None:
                continue
            yield Task(int(entry), thread_folder, stat, TaskType.THREAD)

    @staticmethod
    def _to_process(task: Task, priority: int | None = None) -> Process:
        return Process(
            pid=task.pid, command=task.stat.command, type=task.type, priority=priority
        )
