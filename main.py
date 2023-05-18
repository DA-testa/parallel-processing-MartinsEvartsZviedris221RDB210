# python3

from collections import namedtuple
AssignedJob = namedtuple('AssignedJob', ['worker', 'started_at'])
class JobQueue:
    
    def __init__(self, workers,job):
        self.workers = workers
        self.job = job
        self.EndTime = []
        self.AsignedJobs = []
        for i in range(self.workers):
            self.EndTime.append([i,0])
            
    def ShiftDown(self,i):
        Index = i
        left = 2*i+1
        right = 2*i+2
        if Left < self.workers:
            if self.EndTime[Index][1] >self.EndTime[Left][1]:
                Index= Left
            elif self.EndTime[Index][1] ==self.EndTime[Left][1]:
                if self.EndTime[Index][0]> self.EndTime[Left][0]:
                    Index =Left
        if Right< self.workers:
            if self.EndTime[Index][1] > self.EndTime[Right][1]:
                Index = Right
            elif self.EndTime[Index][1] == self.EndTime[Right][1]:
                if self.EndTime[Index][0] > self.EndTime[Right][0]:
                    Index = Right
        if Index != i:
            self.EndTime[i],self.EndTime[Index] = self.EndTime[Index], self.EndTime[i]
            self.ShiftDown(Index)
            
    def NextWorker(self,job):
        root = self.EndTime[0]
        next_worker = root[0]
        started_at = root[1]
        self.AsignedJobs.append(AssignedJob(next_worker,started_at))
        self.EndTime[0][1] += job
        self.ShiftDown(0)
        
def main():
    n_Workers, n_work = map(int, input().split())
    work = list(map(int, input().split()))
    assert len(work) == n_work
    work_queue = JobQueue(n_Workers, work)
    for job in work:
        work_queue.NextWorker(job)
    AsignedJobs = work_queue.assigned_jobs
    for job in AsignedJobs:
        print(job.worker, job.started_at)

if __name__ == "__main__":
    main()
