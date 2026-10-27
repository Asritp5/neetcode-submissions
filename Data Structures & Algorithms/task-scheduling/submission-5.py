class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:  
        task_len=len(tasks)

        if n==0:
            return task_len
        c=list(Counter(tasks).values())
        c.sort(reverse=True)
        size=len(c)
        idle_slots=(c[0]-1)*n

        for i in range(1,size):
            slots=min(c[i],c[0]-1)
            idle_slots-=slots

            if idle_slots<=0:
                break

        return task_len+max(idle_slots,0)